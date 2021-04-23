# Vaatimusmäärittely

Tämä on sovelluksen alustava vaatimusmäärittely, joka saattaa joiltain osin muuttua työn aikana.

## Sovelluksen tarkoitus

Sovellus on Trivial Pursuitin kaltainen tietopeli, jonka pelisessiot ovat kustomoitavissa (kuvaus tarkentuu myöhemmin). Käyttäjät voivat lisäksi luoda omia kysymyksiä ja kategorioita. Sovelluksen kieli on englanti.

## Käyttäjät

Sovelluksella on rekisteröitymistä vaativa käyttäjärooli.

## Käyttöliittymä ja toiminnallisuudet

### Kirjautuminen / Rekisteröityminen (KAIKKI TEHTY)

  - Käyttäjä voi kirjautua sovellukseen (lokaalilla) käyttäjätunnuksella ja salasanalla.
    - Tiedot syötetään lomakkeelle.
    - Mikäli käyttäjätunnusta ei ole, sovellus luo sellaisen.
    - Sovellus ilmoittaa käyttäjälle asianmukaisesti, mikäli
      - tunnus ei täytyä ehtoja (pituudeltaan vähintään 3 merkkiä),
      - olemassa oleva käyttäjätunnus ja salasana eivät täsmää. 
  - Käyttäjä voi nähdä listan rekisteröityneistä käyttäjistä asianmukaisen painikkeen avulla.
  - Kun käyttäjä on kirjautunut onnistuneesti, tätä tervehditään asianmukaisesti, minkä jälkeen siirrytään näkymään "Pelin asetukset".
  
### Pelin asetukset (KAIKKI TEHTY)

  - Käyttäjä voi kirjautua ulos asianmukaisen painikkeen avulla, jolloin sovellus siirtyy näkymään "Kirjautuminen / Rekisteröityminen".
  - Käyttäjä voi siirtyä näkymään "Omat kysymykset ja kategoriat" asianmukaisen painikkeen avulla.
  - Käyttäjä voi nähdä säännöt asianmukaisen painikkeen avulla.
  - Käyttäjä voi muokata pelin asetuksia valitsemalla
    - pelaajien lukumäärän ja nimet (1-6, kirjautunut käyttäjä ensimmäisenä),
    - kysymysten kategoriat (2-12, useita vaihtoehtoja),
    - pelilaudan koon (6 vaihtoehtoa, keskikoko valittuna valmiiksi)
  - Käyttäjä voi aloittaa pelin asianmukaisella painikkeella, jolloin siirrytään näkymään "Pelisessio".
    - Mikäli pelin asetukset eivät täytä ehtoja (vähintään yksi pelaaja ja kaksi kategoriaa), sovellus ilmoittaa siitä käyttäjälle.

### Omat kysymykset ja kategoriat (KAIKKI TEHTY)

  - Käyttäjä voi luoda uuden kysymyksen syöttämällä asianmukaisiin tekstikenttiin
    - kategorian (joko olemassa oleva tai uusi),
    - vaikeustason (kolme vaihtoehtoa),
    - kysymyksen,
    - vastauksen.
      - HUOM: Uusi kategoria luodaan siis luomalla kysymys kyseiseen kategoriaan.
      - Mikäli käyttäjä unohtaa kysymysmerkin kysymyksen perästä tai pisteen vastauksen perästä, sovellus lisää ne automaattisesti.
      - Käyttäjä voi tyhjentää täyttämänsä kentät asianmukaisen painikkeen avulla.
  - Käyttäjä voi selata kaikkien käyttäjien luomia kysymyksiä.
  - Käyttäjä voi muokata luomiaan kysymyksiä.
    - Mikäli käyttäjä yrittää muokata jonkun muun luomaa kysymystä, sovellus ilmoittaa siitä käyttäjälle.
  - Käyttäjä voi poistaa luomiaan kysymyksiä.
    - Käyttäjältä pyydetään tällöin vahvistus. 
    - Mikäli käyttäjä valitsee useamman kysymyksen poistettavaksi, sovellus poistaa vain ne, jotka kuuluvat käyttäjälle, ja ilmoittaa, montako kysymystä jäi poistamatta.
  - Käyttäjä voi milloin tahansa palata takaisin näkymään "Pelin asetukset" asianmukaisen painikkeen avulla.

### Pelisessio

  - Käyttäjän on pystyttävä seuraamaan peliä ja sen edistymistä jonkinlaiselta (alkeelliselta) pelilaudalta.
    - Lisäksi kunkin pelaajan on pystyttävä 'heittämään' noppaa pelivuoronsa aikana.
  - Kysymykset haetaan lokaalista tietokannasta ja/tai [Open Trivia Databasesta](https://opentdb.com/api_config.php) riippuen pelin asetuksista.
  - Käyttäjä voi tarkastella pelisession tilastoja asianmukaisen painikkeen avulla.
  - Käyttäjä voi tarkastella pelin sääntöjä asianmukaisen painikkeen avulla.
  - Käyttäjän on pystyttävä lopettamaan peli ja siirtymään takaisin näkymään "Pelin asetukset" asianmukaisen painikkeen avulla.
    - Käyttäjältä pyydetään tällöin vahvistus.
  - Kun yksi pelaajista voittaa (säännöt ja siten myös vaatimukset tarkentuvat myöhemmin), peli päättyy.
    - Käyttäjälle ilmoitetaan tyyliin "Pelaaja 1 voitti!".
    - Käyttäjä voi poistua pelistä asianmukaisella painikkeella, jolloin siirrytään takaisin näkymään "Pelin asetukset".

## Toimintaympäristön rajoitteet

- Sovelluksen tulee toimia *ainakin* Linux- ja OSX-käyttöjärjestelmissä.
  - HUOM: Sovellus täytyy pystyä suorittamaan, kääntämään ja testaamaan komentoriviltä Tietojenkäsittelytieteen laitoksen Linux-koneilla asianmukaisia ohjeita noudattamalla.
- Käyttäjien ja sisältöjen tiedot talletetaan tietokantaan, josta niitä myös luetaan.

## Jatkokehitysideoita

- Pelin asetuksissa voi valita 
  - pelaajien värit vapaasti (tai jopa omat kuvakkeet),
  - vaikeustason (Easy / Intermediate / Advanced Trivialist / Hardcore Madness),
  - kysymysten vaikeustason pelaajittain,
  - vaikeustason kategorioittain,
  - kategoriaksi "random", jolloin kategoria arvotaan pelisession aikana jokaista kysymystä varten,
  - noppien lukumäärän (1-2),
  - kategoriapisteiden lukumäärän (1 = pikapeli, 5 = maraton)
  - kysymysten kategorioille haluamansa värit,
  - mukaan vain esimerkiksi monivalintakysymyksiä,
  - "Random"-pelimuodon, jolloin sovellus arpoo käyttäjälle asetukset,
  - kysymyksiä vain joko omista tai OpenTriviaDatabasen kysymyksistä, tai molemmista,
  - pelin asetukset valmiista pohjista (valmiiksi annetut ja/tai käyttäjän luomat).

- Omien kysymysten
  - selaamiseen hakukenttä ja kategoriasuodattimet,
  - kategorioiden muokkaus ja poistaminen,
  - luokittelu avoimiin kysymyksiin, monivalintoihin ja kyllä-tai-ei-kysymyksiin,
  - lisäämiseen huomautus, mikäli täsmälleen sama kysymys on jo kategoriassa olemassa.
  - poistamisilmoitukseen listaus käyttäjistä, joiden kysymyksiä ei voitu poistaa,
  - oheen tietoa kysymyksistä, kuten kuinka monta kysymystä käyttäjät ovat yhteensä luoneet.

- Pelisessioon
  - mekanismi, joka välttää kysymästä samaa kysymystä uudelleen, ellei ole aivan pakko,
  - tuomarimoodi, joka mahdollistaa esimerkiksi virheellisesti annettujen pisteiden muokkamisen,
  - näyttävämpi pelilauta,
  - voitosta ilmoittava näkymä voittaneen pelaajan väreillä jne.,
  - kattavammat tilastot (sekä kesken pelin että pelin päätyttyä), joista selviää sekä yhteensä että pelaajittain mm. kysyttyjen kysymysten sekä oikeiden ja väärien vastausten määrät.

Muita ideoita
  - Kysymysten ja kategorioiden tuonti muualta.
  - Pelaajan poistaminen kesken pelin.
  - Useamman käyttäjän samanaikainen kirjautuminen ja tietojen synkkautuminen.
  - Pääkäyttäjäroolin lisääminen, jotta kenen tahansa profiileja ja kysymyksiä voi tarvittaessa poistaa.
  - Pelin asetukset pysyvät muistissa, vaikka näkymä vaihtuisi välissä.
  - Pelin asetuksissa näkyy kategorioiden perässä niiden sisältämät kysymysmäärät.
  - Pelin asetuksissa näkyy peliin valittujen kategorioiden sisältämät kysymykset yhteensä.
  - "Resume game" -toiminnon lisääminen.
  - Näkymien kehittäminen näyttävämmiksi.
  - Näkymien ja widgettien kehittäminen kooltaan responsiivisiksi.
