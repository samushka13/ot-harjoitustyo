# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovellus on Trivial Pursuitin kaltainen tietopeli, jonka pelisessiot ovat kustomoitavissa. Rekisteröityneet käyttäjät voivat lisäksi luoda omia kysymyksiä ja kategorioita.

## Käyttäjät

Sovelluksella on vain yksi, normaali käyttäjärooli, joka voi olla joko vieraileva tai rekisteröitynyt käyttäjä.

## Käyttöliittymä ja toiminnallisuudet

TODO: Lisää luonnos käyttöliittymästä.

### Kirjautuminen / Rekisteröityminen

  - Käyttäjä voi luoda (lokaalin) käyttäjätunnuksen (uniikki ja pituudeltaan vähintään 3 merkkiä).
    - Mikäli tunnus ei täytyä ehtoja, sovellus ilmoittaa siitä käyttäjälle.
  - Sovellukseen kirjaudutaan käyttäjätunnuksella, joka syötetään lomakkeelle.
    - Mikäli käyttäjää ei ole, sovellus ilmoittaa siitä käyttäjälle.
  - Vaiheen voi myös ohittaa, jolloin sovellus ilmoittaa, että tiettyjä ominaisuuksia ei voi käyttää kirjautumatta.
    - Toisin sanoen: omia kysymyksiä ei voi luoda eikä käyttää, jolloin pelin kysymykset haetaan yksinomaan [Open Trivia Databasesta] (https://opentdb.com/api_config.php).
  
  -> Täältä voi siirtyä vain näkymään "Pelin asetukset".
  
### Pelin asetukset

  - Pelaajien lukumäärä ja "nappuloiden" värit (2-6)
  - Kysymysten kategoriat (6)
  - Nappula: "Aloita peli"

  -> Täältä voi siirtyä joko näkymään "Pelin kulku" tai "Omat kysymykset ja kategoriat".

### Omat kysymykset ja kategoriat

  - Selaa
    - Kaikki listana tai kategorioittain.
  - Poista
    - Käyttäjältä pyydetään vahvistus. 
  - Muokkaa
    - Voi muokata kysymystä, vastausta tai kategoriaa.
  - Luo uusi
    - Uusi kysymys sisältää kentät kysymykselle, vastaukselle ja kategorialle.
    - HUOM: Uusi kategoria luodaan luomalla kysymys kyseiseen kategoriaan.

  -> Täältä voi siirtyä vain näkymään "Pelin kulku".

### Pelin kulku

  - Huomion keskipisteenä on jonkinlainen (alkeellinen) pelilauta tai muu pelin seuraamisen kannalta välttämätön asia.
  - Sivupalkissa tai vastaavassa näkyy pelaajien edistyminen.
  - Sivupalkissa on myös nappula pelin lopetukselle. 
  - Kun yksi pelaajista saa kaikki kategoriat oikein, peli päättyy.
    - Ilmoitetaan tyyliin "Pelaaja 1 voitti!".
    - Samalla ilmestyy nappula, jota painamalla pääsee takaisin pelin asetuksiin.

  -> Täältä voi siirtyä vain näkymään "Pelin asetukset".

## Toimintaympäristön rajoitteet

- Sovelluksen tulee toimia *ainakin* Linux- ja OSX-käyttöjärjestelmissä.
  - HUOM: Sovellus täytyy pystyä suorittamaan, kääntämään ja testaamaan komentoriviltä laitoksen Linux-koneilla.
- Käyttäjien tiedot talletetaan paikalliselle levylle (jatkokehityksen myötä mahdollisesti muualle)

## Jatkokehitysideoita

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
