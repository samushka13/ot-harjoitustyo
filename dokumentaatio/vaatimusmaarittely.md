# Vaatimusmäärittely

Tämä on sovelluksen alustava vaatimusmäärittely, joka saattaa joiltain osin muuttua työn aikana.

## Sovelluksen tarkoitus

Sovellus on tietopeli, jonka pelisessiot ovat laajasti kustomoitavissa. Käyttäjät voivat lisäksi luoda omia kysymyksiä ja kategorioita. Sovelluksen kieli on englanti.

## Käyttäjät

Sovelluksella on rekisteröitymistä vaativa käyttäjärooli.

## Käyttöliittymä ja toiminnallisuudet

### Kirjautuminen / Rekisteröityminen

- Käyttäjä voi kirjautua sovellukseen (lokaalilla) käyttäjänimellä ja salasanalla.
  - Tiedot syötetään lomakkeelle.
  - Mikäli käyttäjätunnusta ei ole, sovellus luo sellaisen.
  - Sovellus ilmoittaa käyttäjälle asianmukaisesti, mikäli
    - käyttäjänimi ei täytyä ehtoja (pituudeltaan 3-25 merkkiä),
    - olemassa oleva käyttäjänimi ja salasana eivät täsmää. 
- Käyttäjä voi nähdä listan rekisteröityneistä käyttäjistä asianmukaisen painikkeen avulla.
- Kun käyttäjä on kirjautunut onnistuneesti, tätä tervehditään asianmukaisesti, minkä jälkeen siirrytään näkymään "Pelin asetukset".
  
### Pelin asetukset

- Käyttäjä voi kirjautua ulos asianmukaisen painikkeen avulla, jolloin sovellus siirtyy näkymään "Kirjautuminen / Rekisteröityminen".
- Käyttäjä voi siirtyä näkymään "Oma sisältö" asianmukaisen painikkeen avulla.
- Käyttäjä voi nähdä säännöt asianmukaisen painikkeen avulla.
- Käyttäjä voi muokata pelin asetuksia valitsemalla
  - pelaajien lukumäärän ja nimet (1-6, kirjautunut käyttäjä ensimmäisenä),
  - kysymysten kategoriat (2-12, useita vaihtoehtoja ml. "Random" [Open Trivia Databasesta](https://opentdb.com/api_config.php)),
  - pelilaudan koon (6 vaihtoehtoa, keskikoko valittuna valmiiksi)
- Käyttäjä voi nähdä lisätietoa Open Trivia Databasesta asianmukaisen painikkeen avulla.
- Käyttäjä voi aloittaa pelin asianmukaisella painikkeella, jolloin siirrytään näkymään "Pelisessio".
  - Mikäli pelin asetukset eivät täytä ehtoja (vähintään yksi pelaaja ja kaksi kategoriaa sekä internet-yhteys, mikäli Open Trivia Databasen kategorioita valittuna), sovellus ilmoittaa siitä käyttäjälle.

### Oma sisältö

- Käyttäjä voi luoda uuden kysymyksen syöttämällä asianmukaisiin tekstikenttiin
  - kategorian (joko olemassa oleva tai uusi, 1-30 merkkiä),
  - vaikeustason (kolme vaihtoehtoa),
  - kysymyksen (1-300 merkkiä),
  - vastauksen (1-100 merkkiä).
    - HUOM: Uusi kategoria luodaan siis luomalla kysymys kyseiseen kategoriaan.
    - Mikäli käyttäjän syöttämät tiedot eivät pituudeltaan täsmää, sovellus ilmoittaa asiasta käyttäjälle.
    - Mikäli käyttäjä unohtaa kysymysmerkin kysymyksen perästä tai pisteen vastauksen perästä, sovellus lisää ne automaattisesti.
    - Käyttäjä voi tyhjentää täyttämänsä kentät asianmukaisen painikkeen avulla.
- Käyttäjä voi selata kaikkien käyttäjien luomia kysymyksiä.
- Käyttäjä voi muokata luomiaan kysymyksiä.
  - Mikäli käyttäjä yrittää muokata jonkun muun luomaa kysymystä, sovellus ilmoittaa siitä käyttäjälle.
- Käyttäjä voi poistaa luomiaan kysymyksiä (yhden, useamman tai kaikki).
  - Käyttäjältä pyydetään tällöin vahvistus.
  - Mikäli käyttäjä valitsee useamman kysymyksen poistettavaksi, sovellus poistaa vain ne, jotka kuuluvat käyttäjälle, ja ilmoittaa, montako kysymystä jäi poistamatta.
- Käyttäjä voi milloin tahansa palata takaisin näkymään "Pelin asetukset" asianmukaisen painikkeen avulla.

### Pelinäkymä

- Pelinäkymän tulee sisältää
  - kategorioiden määrään mukautuva pelilauta ouroboros-symboliikalla,
  - noppa ja painike sen 'heittämiseen',
  - pistetaulu, josta näkee pelaajien pisteet ja vuorossa olevan pelaajan,
  - kategoriataulu, josta näkee pelisession kategoriat ja vuorossa olevan kategorian,
  - tila kysymykselle ja vastaukselle,
  - painikkeen, jolla voi näyttää vastauksen,
  - painikkeet, joilla voi valita, vastasiko pelaaja oikein vai väärin.
- Kysymys on esitettävä kategoriasta, jolla pelaajan pelinappula laudalla sijaitsee.
- Pistetaulun on reagoitava pisteiden muutoksiin pelaajien vastausten mukaisesti.
- Käyttäjä voi tarkastella pelisession tilastoja asianmukaisen painikkeen avulla.
- Käyttäjä voi tarkastella pelin sääntöjä asianmukaisen painikkeen avulla.
- Käyttäjän on pystyttävä lopettamaan peli ja siirtymään takaisin näkymään "Pelin asetukset" asianmukaisen painikkeen avulla.
  - Käyttäjältä pyydetään tällöin vahvistus.
- Kun yksi pelaajista voittaa, peli päättyy.
  - Käyttäjälle ilmoitetaan tyyliin "Pelaaja 1 voitti!".
  - Käyttäjä voi siirtyä asianmukaisella painikkeella näkymään "Pelin asetukset".

## Toimintaympäristön rajoitteet

- Käyttäjien, sisältöjen ja pelisessioiden tiedot talletetaan tietokantaan, josta niitä myös luetaan.
- Sovelluksen tulee toimia *ainakin* Linux- ja macOS-käyttöjärjestelmissä.
  - HUOM: Sovellus täytyy pystyä suorittamaan, kääntämään ja testaamaan komentoriviltä HY:n Tietojenkäsittelytieteen laitoksen Linux-koneilla asianmukaisia ohjeita noudattamalla.

## Jatkokehitysideoita

Pelin asetuksissa voi valita 
- pelaajien värit (ja/tai omat kuvakkeet),
- kategorioiden värit,
- vaikeustason (Easy / Intermediate / Advanced Trivialist / Hardcore Madness),
- vaikeustason kategorioittain,
- kysymysten vaikeustason pelaajittain,
- noppien lukumäärän (1-2),
- kategoriapisteiden lukumäärän (1 = pikapeli, 5 = maraton)
- mukaan vain esimerkiksi monivalintakysymyksiä,
- "random"-pelimuodon, jolloin sovellus arpoo käyttäjälle asetukset,
- pelin asetukset valmiista pohjista (valmiiksi annetut ja/tai käyttäjän luomat),
- yksilöityjä kategorioita [Open Trivia Databasesta](https://opentdb.com/api_config.php).

Omien sisältöjen
- selaamiseen hakukenttä ja kategoriasuodattimet,
- kategorioiden muokkaus ja poistaminen,
- luokittelu avoimiin, monivalinta- ja 'kyllä-vai-ei' -kysymyksiin,
- lisäämiseen huomautus, mikäli täsmälleen sama kysymys on jo kategoriassa olemassa.
- oheen tietoa kysymyksistä, kuten kuinka monta kysymystä käyttäjät ovat yhteensä luoneet,
- tuonti toisesta tietokannasta tai muusta tietolähteestä (esim. csv-tiedosto).

Pelisessioon
- mekanismi, joka välttää kysymästä samaa kysymystä uudelleen, ellei ole aivan pakko,
- tuomarimoodi, joka mahdollistaa esimerkiksi virheellisesti annettujen pisteiden muokkamisen,
- voitosta ilmoittava näkymä voittaneen pelaajan väreillä jne.,
- kattavammat tilastot (sekä kesken pelin että pelin päätyttyä), joista selviää sekä yhteensä että pelaajittain mm. kysyttyjen kysymysten sekä oikeiden ja väärien vastausten määrät.

Muita ideoita
- Pääkäyttäjäroolin lisääminen, jotta profiileja ja kysymyksiä voi tarvittaessa poistaa.
- Oman profiilin poistaminen (mahdollisuus kuitenkin säilyttää kysymykset - vaatii pääkäyttäjäroolin).
- Useamman käyttäjän samanaikainen kirjautuminen ja tietojen synkronointi.
- Pelin asetuksissa näkyy kategorioiden perässä niiden sisältämät kysymysmäärät.
- Pelin asetuksissa näkyy peliin valittujen kategorioiden sisältämät kysymykset yhteensä.
- Pelin asetukset pysyvät muistissa, vaikka näkymä vaihtuisi välissä.
- "Resume game" -toiminnon lisääminen.
- Pelaajan poistaminen kesken pelin.
- Näkymien ja widgettien kehittäminen näyttävämmiksi ja kooltaan responsiivisiksi.
