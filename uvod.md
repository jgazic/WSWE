# Povzetek

## Uvod
V okviru predmeta Seminar iz načrtovanja in razvoja programske opreme v telekomunikacijah je bila razvita storitev WSWE (What Should We Eat?). Storitev je namenjena reševanju povsem praktičnega in preprostega problema - kam na kosilo s sodelavci. WSWE omogoča dodajanje predlogov nato pa izmed vseh izbere končno odločitev, ki se je neda več spremeniti. Na ta način dobimo povsem pošteno odločitev, brez da bi se uporabniki morali sami dogovarjati, čigav predlog se upošteva


## Cilj Seminarske naloge

Glavni cilj seminarske naloge je bilo učenje razvoja full-stack storitve. Naloga je zato razdeljena na backend in frontend, ki sta med seboj popolnoma ločena, komunicirata pa preko REST API vmesnika. 

## Opis delovanja storitve

### Dodajanje predlogov
 WSWE omogoča generiranje unikatne povezave, ki jo nato uporabnik lahko deli s kolegi. Na povezavi lahko vsak doda svoje predloge. Vsak lahko doda poljubno število predlogov, vendar en predlog lahko doda le enkrat. Vsi predlogi se shranijo v podatkovno bazo.

 ### Sprejemanje odločitve

Ko so vsi predlogi dodani, lahko kdorkoli izmed sodelujočih, klikne na gumb za sprejemanje končne odločitve. Sistem bo izmed vseh dodanih predlogov naključno izbral enega. Predlog, ki ga je predlagalo več uporabnikov bo na ta način imel več možnosti.

Po kliku na gumb za končno odločitev, se dodajanje novih predlogov prepreči. Za naslednjo izbiro je treba generirati novo unikatno povezavo. Ko je odločitev enkrat sprejeta, se je tudi neda več spremeniti in vsak naslednji klik na gumb izbira, bo vrnil isti rezultat.

 ## Uporabljene tehnologije

 Backend: 
 - Python 
 - Flask framework 
 - Sqlite
 - Knjižnice json, request, sqlite3, random

 Spletni odjemalec:
 - HTML
 - JavaScript
 - CSS
 - Bootsrtap

 Version Control:
 - Git
 - Github

REST API testiranje:
- Postman


