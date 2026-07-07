# 10 Závěry a doporučení

Cíl práce, tedy zpracování teoretických a metodických východisek pro praktickou část, byl naplněn. Odpovědi na výzkumné otázky lze stručně shrnout takto:

- **K VO1:** Byly vymezeny klíčové pojmy databázových systémů (data, DBMS, schéma, instance, metadata), popsány fáze návrhu databáze (konceptuální, logický, fyzický) a vysvětleny datové modely používané v praxi, zejména ER/EER a relační model spolu s normalizací.
- **K VO2:** Metoda AHP byla popsána jak z hlediska principu (hierarchie cíl–kritéria–alternativy), tak z hlediska postupu (párové porovnání s využitím Saatyho škály, výpočet vah, kontrola konzistence pomocí CR). Bylo zdůvodněno, proč je AHP vhodná pro porovnání softwarových nástrojů.
- **K VO3:** Bylo navrženo osm hodnoticích kritérií (K1–K8) a metodický rámec navazující komparace, zahrnující sestavení hierarchie, párové porovnání kritérií, testovací scénář nad nainstalovanými nástroji, syntézu priorit a analýzu citlivosti.

Tento navržený teoretický a metodický rámec tvoří přímý základ pro navazující praktickou komparaci v následující práci. Pro realizaci této praktické části se doporučuje: a) provést testovací scénář na všech čtyřech nástrojích v jednom kalendářním týdnu, aby se minimalizovaly rozdíly ve zkušenostech hodnotitele; b) při hodnocení kvalitativních kritérií (K2, K6) doplnit slovní zdůvodnění každého párového porovnání; c) zařadit analýzu citlivosti minimálně pro váhy K1 a K8; d) zvážit modelový scénář dvou typových firem (malé a střední) s odlišnými váhami kritérií a porovnat výsledné pořadí mezi scénáři. Vedle toho bude v následující práci podrobněji popsán testovací scénář s výpočtem vah a případně bude navržena jednoduchá podpůrná aplikace.

Testovací scénář bude obsahovat vytváření logického modelu, generování DDL skriptu a, pokud to nástroj umožní, také reverzní inženýrství na produkční databáze. Na základě výsledků testování a prostudované dokumentace bude každý nástroj ohodnocen podle kritérií K1–K8. Tato hodnocení budou vstupem do párového porovnávání v metodě AHP. Hodnocení bude obsahovat výpočet Saatyho matic, výpočet vektoru priorit a ověření poměru konzistence CR. Citlivostní analýza pak ukáže, jak změna váhy jednotlivých kritérií ovlivňuje výsledné pořadí nástrojů.


```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

