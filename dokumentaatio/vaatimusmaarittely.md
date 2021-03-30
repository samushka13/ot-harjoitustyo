# Vaatimusmäärittely

Tämä on sovelluksen alustava vaatimusmäärittely, joka saattaa joiltain osin muuttua työn aikana.

## Sovelluksen tarkoitus

Sovellus on Trivial Pursuitin kaltainen tietopeli, jonka pelisessiot ovat kustomoitavissa (kuvaus tarkentuu myöhemmin). Rekisteröityneet käyttäjät voivat lisäksi luoda omia kysymyksiä ja kategorioita.

## Käyttäjät

Sovelluksella on vain yksi, normaali käyttäjärooli, joka voi olla joko vieraileva tai rekisteröitynyt käyttäjä.

## Käyttöliittymä ja toiminnallisuudet

**TODO**: Luonnos käyttöliittymästä.

### Kirjautuminen / Rekisteröityminen

HUOM: Nämä toiminnallisuudet voidaan toteuttaa joko samaan tai eri näkymään.

  - Käyttäjä voi luoda (lokaalin) käyttäjätunnuksen (uniikki ja pituudeltaan vähintään 3 merkkiä).
    - Mikäli tunnus ei täytyä ehtoja, sovellus ilmoittaa siitä käyttäjälle.
  - Sovellukseen kirjaudutaan käyttäjätunnuksella, joka syötetään lomakkeelle.
    - Mikäli käyttäjää ei ole, sovellus ilmoittaa siitä käyttäjälle.
  - Vaiheen voi myös ohittaa, jolloin sovellus ilmoittaa, että tiettyjä ominaisuuksia ei voi käyttää kirjautumatta.
    - Toisin sanoen: omia kysymyksiä ei voi luoda eikä käyttää, jolloin pelin kysymykset haetaan yksinomaan [Open Trivia Databasesta](https://opentdb.com/api_config.php).
  - Kun käyttäjä on kirjautunut (tai ohittanut koko vaiheen), sovellus siirtyy näkymään "Pelaa".
  
### Pelaa

  - Käyttäjä voi siirtyä näkymään "Omat kysymykset ja kategoriat" asianmukaisen painikkeen avulla.
    - Mikäli vieraileva käyttäjä yrittää tätä, ilmoitetaan, että käyttäjän on kirjauduttava siirtyäkseen kyseiseen näkymään.
  - Käyttäjä voi aloittaa pelin seuraavasti:
    - Käyttäjä valitsee pelaajien lukumäärän (2-6, oletusarvona 2).
    - Käyttäjä valitsee kysymysten kategoriat (yhteensä 5, useita vaihtoehtoja, oletusarvot annettu).
    - Käyttäjä aloittaa pelin painikkeella, jossa lukee "Aloita peli!", jolloin siirrytään näkymään "Pelin kulku".

### Omat kysymykset ja kategoriat

  - Käyttäjä voi selata luomiaan kysymyksiä kategorioittain.
  - Käyttäjä voi muokata luomiaan kysymyksiä ja kategorioita.
  - Käyttäjä voi poistaa luomiaan kysymyksiä ja kategorioita.
    - Käyttäjältä pyydetään tällöin vahvistus. 
  - Käyttäjä voi luoda uuden kysymyksen seuraavasti:
    - Käyttäjä syöttää yhteen tekstikenttään kategorian (joko olemassa oleva tai uusi).
    - Käyttäjä syöttää toiseen tekstikenttään kysymyksen.
      - Käyttäjälle ilmoitetaan, mikäli täsmälleen sama kysymys on olemassa.
    - Käyttäjä syöttää kolmanteen tekstikenttään vastauksen.
    - HUOM: Uusi kategoria luodaan siis luomalla kysymys kyseiseen kategoriaan.
  - Käyttäjä voi milloin tahansa palata takaisin näkymään "Pelin asetukset" asianmukaisen painikkeen avulla.

### Pelin kulku

  - Käyttäjän on pystyttävä seuraamaan peliä ja sen edistymistä jonkinlaiselta (alkeelliselta) pelilaudalta.
    - Lisäksi kunkin pelaajan on pystyttävä 'vierittämään' noppaa pelivuoronsa aikana.
  - Käyttäjän on pystyttävä lopettamaan peli ja siirtymään takaisin näkymään "Pelaa" milloin tahansa asianmukaisen painikkeen avulla.
    - Käyttäjältä pyydetään tällöin vahvistus.
  - Kun yksi pelaajista voittaa (säännöt ja siten myös vaatimukset tarkentuvat myöhemmin), peli päättyy.
    - Käyttäjälle ilmoitetaan tyyliin "Pelaaja 1 voitti!".
    - Käyttäjä voi poistua pelistä asianmukaisella painikkeella, jolloin siirrytään takaisin näkymään "Pelaa".

## Toimintaympäristön rajoitteet

- Sovelluksen tulee toimia *ainakin* Linux- ja OSX-käyttöjärjestelmissä.
  - HUOM: Sovellus täytyy pystyä suorittamaan, kääntämään ja testaamaan komentoriviltä Tietojenkäsittelytieteen laitoksen Linux-koneilla asianmukaisia ohjeita noudattamalla.
- Käyttäjien tiedot talletetaan tietokantaan, josta niitä myös luetaan.

## Jatkokehitysideoita

- Pelin asetuksissa voi valita pelaajien värit vapaasti (tai pelaajille voi asettaa omat kuvakkeet).
- Pelin asetuksissa voi valita vaikeustason (Helppo / Keskitaso / Haastava).
- Pelin asetuksissa voi valita vaikeustason pelaajittain (esim. lapsille kiva lisä).
- Pelin asetuksissa voi valita 'pikapelin', joka on normaalia lyhyempi pelimuoto.
- Pelin asetuksissa voi valita 'maratonimoodin', joka on normaalia pidempi pelimuoto.
- Pelin asetuksissa voi valita kysymysten kategorioita vapaammin (esim. 1-12).
- Pelin asetuksissa voi valita kysymysten kategorioille asettaa haluamansa värit.
- Pelin asetuksissa voi valita mukaan vain esimerkiksi monivalintakysymyksiä.
- Pelin asetuksissa voi valita mukaan 'jokeriruutuja', josta voi tulla kysymyksiä muistakin kuin peliin valituista kategorioista.
- Pelin asetuksissa voi muokata pelilaudan kokoa ja ruutujen järjestystä.
- Pelin asetuksissa voi valita "Random"-pelimuodon, jolloin sovellus arpoo käyttäjälle asetukset.
- Omien kysymysten selaamiseen hakutoiminto.
- Omien kysymysten luokittelu avoimiin kysymyksiin, monivalintoihin ja kyllä-tai-ei-kysymyksiin.
- Pelilaudan kehittäminen näyttävämmäksi.
- Voitosta ilmoittavan näkymän kustomointi voittaneen pelaajan mukaiseksi (esim. näytetään oikeanvärinen nappula).
- Pelisession tilastot (pelin päätyttyä), josta näkee mm. kysymysten, oikeiden vastausten ja väärien vastausten määrän per pelaaja.
- Muiden pelaajien luomien kysymysten ja kategorioiden tuonti.
- Pelaajan poistaminen (ja lisääminen?) kesken pelin.
- Useamman käyttäjän samanaikainen kirjautuminen ja tietojen synkkautuminen.
