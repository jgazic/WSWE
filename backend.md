# Opis
Logika backenda je napisana v Pythonu, njegova naloga pa je, da v bazo shrani vse predloge v Sqlite datoteko. Izmed vseh predlogov pa naključno izbere enega in ga ponudi kot končno izbiro. Poskrbeti mora tudi za to, da po sprejeti odločitvi ne dovoli, da bi se dodajali novi predlogi in da se odločitve ne da spremeniti. Ker gre za spletno storitev, se morajo uporabniki med seboj ločiti. WSWE ta problem rešuje z unikatnimi povezavami. Vsak lahko generira unikatno povezavo in pri njegovih odločitvah bodo lahko sodelovali samo tisti, s katerimi je to povezavo delil. Backend vse svoje funkcionalnosti izpostavi preko REST API-ja.

# Delovanje

## Generiranje unikatne povezave

```python 
def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    lunch_id=''.join(random.choice(chars) for _ in range(10))
    link = "http://localhost/Projekt_Seminar/Frontend/wswe.html?id=" + lunch_id
    return link
```
Ko uporabnik preko odjemalca pošlje zahtevo za unikatno povezavo, funkcija id_generator ustvari unikaten niz 10 znakov. Niz znakov se nato doda povezavi na obrazec za dodajanje predlogov. Celoten URL se vrne v odgovoru na zahtevo. Uporabnik nato lahko klikne na to povezavo in odpre obrazec za dodajanje predlogov, povezavo pa lahko tudi deli s prijatelji, s katerimi želi na kosilo.

Vsak predlog se pošlje preko POST requesta in vsebuje tudi unikaten ID. Predlogi so v bazi povezani preko tega ID-ja.


### Dodajanje predloga v bazo

Dodajanje predloga v bazo je sestavljeno iz več korakov. 

1. #### Preverjanje ali je za ta ID že bila sprejeta odločitev:

Ko uporabnik pošlje POST request za dodajanje predloga, se najprej preveri, ali je za ta ID odločitev že bila sprejeta in je dodajanje onemogočeno. To naredi funkcija *check for decision()*

```python 
def check_for_decision(id):
    today = date.today()            
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute(f"SELECT * FROM decisions WHERE id = '{id}' ")
    existing_decision = c.fetchall()
    if existing_decision:
        return True
    else:
        return False
```
V primeru, da odločitev že obstaja, funkcija vrne True in nov predlog se ne doda

2. #### Preverjanje ali je uporabnik ta predlog že dodal: 

Ko uporabnik pošlje POST request za dodajanje predloga, se preveri tudi, ali je uporabnik ta predlog že dodal. Na ta način se prepreči, da bi en uporabnik dodal več istih predlogov in si na ta način močno povečal možnost, da bo izbran njegov predlog. To naredi funkcija *check_if_duplicate()*
```python 
def check_if_duplicate(name,suggestion,id):
    today = date.today()            
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute(f"SELECT * FROM suggestions WHERE user='{name}' AND suggestion = '{suggestion}' AND id = '{id}' AND timestamp = '{today}' ")
    duplicate = c.fetchall()
    if duplicate:
        return True
    else:
        return False

```

3. #### Po potrebi vpis novega predloga v bazo:

Če predlog ni duplikat in če odločitev za ta ID še ni bila sprejeta, se predlog zapiše v bazo. Za to poskrbi funkcija *add_suggestion()*

```python 
def add_suggestion(name,suggestion,id):        
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute(f"INSERT INTO suggestions VALUES ('{name}','{suggestion}', '{id}', date('now'))")
    conn.commit()
    conn.close
    print('answer added')

```
Glede na to ali je bil predlog uspešno dodan ali ne, se uporabniku vrne response:
```python 
        if duplicate:
            return 'Sorry, you already suggested this one :)'
        elif check_for_decision(id):
            return 'Sorry decision for this lunch was already made. You can always start a new session and vote again!'

        else:
            add_suggestion(name,suggestion,id)
            remove_id_data(table_name='decisions', id=id)
            return 'Thanks!', 201

```
- Če gre za duplikat se uporabniku sporoči, da je ta predlog že dodal.
- Če je bila odločitev za ta ID že sprejeta se uporabniku sporoči naj grenerira novo povezavo.
- Če je bil predlog uspešno shranjen se uporabniku zahvali.

### Sprejemanje odločitve

Ko uporabnik klikne gumb WSWE se pošlje zahtevek, naj se sprejme končna odločitev. 

Backend najprej prebere unikaten id in preveri ali odločitev za to sejo že obstaja
```python 
        if existing_decision:
            decision = existing_decision[0][1]
            name = existing_decision[0][0]
            response = f"You should eat: {decision} <br>It was suggested by: {name}"
            remove_id_data(table_name='suggestions', id=id)
            

        else:
            response = make_decision(id)
```

- Če odločitev že obstaja se ta pošlje kot odgovor zato, da vsak klik na gumb WSWE vrne isto izbiro. Tako ni važno, kdo prvi klikne WSWE, saj bodo vsi uporabniki ene seje dobili isti odgovor.

- Če odločitev še ne obstaja se 


### REST API