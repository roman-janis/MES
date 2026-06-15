#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sestaví `Seminární práce.md` z kapitolových souborů `Seminární práce 0..13.md`.

Ošetřuje poškození vznikající živým sync (Google Disk):
  1) odstraní NUL byty (0x00),
  2) pozná useknutý soubor (nekončí větnou interpunkcí),
  3) je-li pracovní soubor poškozený, použije zálohu z posledního git commitu.

Spouštět z adresáře práce:
    python3 sestavit_seminarni_praci.py

Skript NIC nemaže; jen čte kapitoly a zapíše výsledný `Seminární práce.md`.
Na konci vypíše, který zdroj pro každou kapitolu použil — zkontroluj report.
"""

import os
import sys
import subprocess

CHAPTERS = list(range(14))          # 0,1,2,...,13
OUT = "Seminární práce.md"
# znaky, jimiž smí kapitola legitimně končit (věta, URL v <...>, openxml ```, závorka)
TERMINATORS = (".", ">", "`", ")", "]", "»", "“", "”", "/")


def git_head(fn):
    """Obsah souboru z posledního commitu (záloha), nebo None když není v gitu."""
    try:
        r = subprocess.run(["git", "show", f"HEAD:{fn}"],
                           capture_output=True, check=True)
        return r.stdout.decode("utf-8")
    except Exception:
        return None


def load(fn):
    """Vrať (text_kapitoly, poznámka_o_zdroji)."""
    raw = open(fn, "rb").read()
    nul = raw.count(b"\x00")
    text = raw.replace(b"\x00", b"").decode("utf-8", "replace").rstrip("\n \t")

    truncated = bool(text) and text[-1] not in TERMINATORS
    corrupt = (nul > 0) or truncated

    if corrupt:
        head = git_head(fn)
        if head is not None:
            why = f"NUL={nul}" + (", useknuté" if truncated else "")
            return head.strip("\n"), f"ZALOHA z gitu  ({why})"
        return text.strip("\n"), f"!! POSKOZENA a BEZ git zalohy (NUL={nul})"

    return text.strip("\n"), "pracovni OK"


def main():
    parts, report = [], []
    for i in CHAPTERS:
        fn = f"Seminární práce {i}.md"
        if not os.path.exists(fn):
            sys.exit(f"CHYBI soubor: {fn}")
        text, note = load(fn)
        parts.append(text)
        report.append(f"  kap {i:>2}: {len(text):>5} zn.  [{note}]")

    out = "\n\n".join(parts) + "\n"

    if "\x00" in out:
        sys.exit("CHYBA: ve vystupu zustaly NUL byty -> zapis zrusen.")

    open(OUT, "w", encoding="utf-8").write(out)

    print(f"Sestaveno: {OUT}  ({len(out)} znaku)")
    print("\n".join(report))
    print("\nHotovo. Zkontroluj radky oznacene 'ZALOHA z gitu' nebo 'POSKOZENA'.")


if __name__ == "__main__":
    main()
