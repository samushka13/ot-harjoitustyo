# Vaatimusmäärittely

Tämä on sovelluksen alustava vaatimusmäärittely, joka saattaa joiltain osin muuttua työn aikana.

## Sovelluksen tarkoitus

Sovellus on Trivial Pursuitin kaltainen tietopeli, jonka pelisessiot ovat kustomoitavissa (kuvaus tarkentuu myöhemmin). Käyttäjät voivat lisäksi luoda omia kysymyksiä ja kategorioita. Sovelluksen kieli on englanti.

## Käyttäjät

Sovelluksella on sekä normaali, rekisteröitymistä vaativa käyttäjärooli että admin-rooli, joka voi poistaa muiden käyttäjätilejä ja niiden luomia sisältöjä.

## Käyttöliittymä ja toiminnallisuudet

**TODO**: Luonnos käyttöliittymästä.

### Kirjautuminen / Rekisteröityminen

  - Käyttäjä voi kirjautua sovellukseen (lokaalilla) käyttäjätunnuksella ja salasanalla.
    - Tiedot syötetään lomakkeelle.
    - Mikäli käyttäjätunnusta ei ole, sovellus luo sellaisen.
    - Sovellus ilmoittaa käyttäjälle asianmukaisesti, mikäli
      - tunnus ei täytyä ehtoja (uniikki ja pituudeltaan vähintään 3 merkkiä),
      - olemassa oleva käyttäjätunnus ja salasana eivät täsmää. 
  - Kun käyttäjä on kirjautunut onnistuneesti, tätä tervehditään asianmukaisesti, minkä jälkeen siirrytään näkymään "Pelin asetukset".
  
### Pelin asetukset

  - Käyttäjä voi siirtyä näkymään "Omat kysymykset ja kategoriat" asianmukaisen painikkeen avulla.
  - Käyttäjä voi muokata pelin asetuksia valitsemalla
    - pelaajien lukumäärän (2-6, oletusarvona 2),
    - kysymysten kategoriat (yhteensä 5, useita vaihtoehtoja, oletusarvot annettu).
  - Käyttäjä voi aloittaa pelin asianmukaisella painikkeella, jolloin siirrytään näkymään "Pelisessio".

### Omat kysymykset ja kategoriat

  - Käyttäjä voi selata kaikkien käyttäjien luomia kysymyksiä kategorioittain.
  - Käyttäjä voi muokata luomiaan kysymyksiä ja kategorioita.
  - Käyttäjä voi poistaa luomiaan kysymyksiä ja kategorioita.
    - Käyttäjältä pyydetään tällöin vahvistus. 
  - Käyttäjä voi luoda uuden kysymyksen syöttämällä asianmukaisiin tekstikenttiin
    - kategorian (joko olemassa oleva tai uusi),
    - vaikeustason,
    - kysymyksen (käyttäjälle ilmoitetaan, mikäli täsmälleen sama kysymys on olemassa),
    - vastauksen.
      - HUOM: Uusi kategoria luodaan siis luomalla kysymys kyseiseen kategoriaan.
  - Käyttäjä voi milloin tahansa palata takaisin näkymään "Pelin asetukset" asianmukaisen painikkeen avulla.

### Pelisessio

  - Käyttäjän on pystyttävä seuraamaan peliä ja sen edistymistä jonkinlaiselta (alkeelliselta) pelilaudalta.
    - Lisäksi kunkin pelaajan on pystyttävä 'heittämään' noppaa pelivuoronsa aikana.
  - Kysymykset haetaan lokaalista tietokannasta ja/tai [Open Trivia Databasesta](https://opentdb.com/api_config.php) riippuen pelin asetuksista.
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
  - noppien lukumäärän (1-2),
  - 'pikapelimoodin', joka on normaalia lyhyempi pelimuoto,
  - 'maratonimoodin', joka on normaalia pidempi pelimuoto,
  - kysymysten kategorioita vapaammin (esim. 1-12),
  - kysymysten kategorioille haluamansa värit,
  - mukaan vain esimerkiksi monivalintakysymyksiä,
  - pelilaudan koon,
  - ruutujen järjestyksen.
  - laudalle 'jokeriruutuja', joista voi tulla kysymyksiä mistä tahansa kategoriasta,
  - "Random"-pelimuodon, jolloin sovellus arpoo käyttäjälle asetukset.
- Omien kysymysten selaamiseen hakutoiminto.
- Omien kysymysten luokittelu avoimiin kysymyksiin, monivalintoihin ja kyllä-tai-ei-kysymyksiin.
- Pelilaudan kehittäminen näyttävämmäksi.
- Voitosta ilmoittavan näkymän kustomointi voittaneen pelaajan mukaiseksi.
- Pelisession tilastot (sekä kesken pelin että pelin päätyttyä), joista näkee mm. kysymysten, oikeiden vastausten ja väärien vastausten määrän per pelaaja.
- Kysymysten ja kategorioiden tuonti muualta.
- Pelaajan poistaminen kesken pelin.
- Useamman käyttäjän samanaikainen kirjautuminen ja tietojen synkkautuminen.
