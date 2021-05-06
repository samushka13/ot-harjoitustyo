# Käyttöohje

## Asennus

1. Lataa uusin [release](https://github.com/samushka13/ot-harjoitustyo/releases).

2. Varmista, että koneellasi on asianmukainen Python-versio (^3.6) ja Poetry-versio (^1.1.5 suositeltu).

3. Asenna projektin riippuvuudet komennolla:

       poetry install

4. Konfiguroi tarvittaessa tallennustiedostojen nimet [tämän ohjeen](https://github.com/samushka13/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md#konfigurointi) mukaisesti (valinnainen).

5. Käynnistä sovellus komennolla:

       poetry run invoke start

### Konfigurointi

Sovellus luo käynnistymisensä yhteydessä tietojen tallennukseen käytettävät tietokantatiedostot automaattisesti juurihakemiston yläpuoleiseen kansioon, jossa esimerkiksi projektin README sijaitsee, mikäli kyseisiä tiedostoja ei vielä ole. Tiedostojen nimet voi tarvittaessa konfiguroida tiedostossa [config.py](https://github.com/samushka13/ot-harjoitustyo/blob/master/src/config.py), joka löytyy projektin juurihakemistosta ("src").

### Käyttöjärjestelmien väliset erot 

Sovelluksen ulkonäkö voi hieman vaihdella käyttöjärjestelmästä riippuen. Parhaan kokemuksen saa macOS-käyttöjärjestelmillä, mutta sovellus toimii myös Linuxilla, joskin asteen karkeamman näköisenä. Sovellus saattaa toimia myös Windowsilla, mutta tätä ei ole testattu.

## Sovelluksen käyttäminen

### Kirjautuminen

Sovellus käynnistyy kirjautumisnäkymään, josta pystyy sekä kirjautumaan olemassa olevilla tunnuksilla että luomaan uusia tunnuksia. Käyttäjänimen pituus on oltava vähintään kolme merkkiä. Salasana on vapaaehtoinen.

![Login](screenshots/login.png)

Painikkeet:

- "Proceed": kirjaa käyttäjän sisään sovellukseen syötetyillä tunnuksilla.
- "Users": näyttää listan tietokannassa olevista rekisteröityneistä käyttäjänimistä.

### Pelin asetukset

Kirjautumisen jälkeen avautuu valikkonäkymä, jossa voi esimerkiksi valita pelin asetukset. Pelin aloittamiseksi vaaditaan vähintään yksi pelaaja ja kaksi kategoriaa. Tyhjiä tai geneerisiä oletusarvoja ei huomioida, joten esimerkiksi alla oleva peli käynnistyisi neljällä pelaajalla ja viidellä kategorialla. Asetuksista voi säätää myös pelilaudan kokoa. Kokeile rohkeasti erilaisia vaihtoehtoja!

![Settings](screenshots/settings.png)

Painikkeet:

- "Rules": näyttää pelin säännöt.
- "Logout": kirjaa ulos ja avaa kirjautumisnäkymän.
- "Custom Content": avaa omien kysymysten hallinnointinäkymän.
- "Start Game": aloittaa pelin valituilla asetuksilla.

### Omat kysymykset

Omien kysymysten hallintanäkymässä on kaksi osaa. Oikeanpuoleisessa näkymän osassa voi luoda omia kysymyksiä täyttämällä vaaditut tiedot. 

Vasemmanpuoleisessa osassa voi puolestaa selata ja muokata jo luotuja kysymyksiä. Mikäli yksikään rekisteröity käyttäjä ei ole luonut omia kysymyksiä, lista olisi tyhjä. Alla olevassa kuvassa kysymyksiä on kuitenkin jo aiemmin luotu. Kullakin rivillä on ilmoitettu kysymyksen numero, kategoria, haastavuus, kysymys, vastaus ja luoja.

![Custom Content](screenshots/custom_content.png)

Painikkeet:

- "Clear": tyhjentää kenttiin täytetyt tiedot.
- "Save": tallentaa täytetyt tiedot.
- "Back to Settings": sulkee ikkunan ja avaa pelin asetusten näkymän.
- "Edit": avaa valitulle kysymykselle muokkausnäkymän.
- "Delete selected": poistaa käyttäjälle kuuluvat valitut kysymykset.
- "Delete all": poistaa kaikki käyttäjälle kuuluvat kysymykset.

### Pelin kulku

Aloitustilassa peli voi näyttää esimerkiksi tältä:

![Game Start](screenshots/game_start.png)

Pelinäkymän osat ovat

- vasemmassa yläkulmassa oleva pistetaulukko,
- vasemmassa keskiosassa oleva kysymys- ja vastaustila,
- vasemmassa alakulmassa oleva kategoriataulukko,
- oikeassa laidassa oleva pelilauta.

Pelin aloittaa vasemmassa ylälaidassa olevan osoittimen osoittama pelaaja. Peli alkaa noppaa 'heittämällä'.

Painikkeet:

- "Cast": arpoo nopan silmäluvun.
- "Quit": lopettaa pelin ja avaa pelin asetusten näkymän.
- "Rules": näyttää pelin säännöt.
- "Statistics": näyttää pelinaikaiset tilastot.

Nopan 'heittämisen' jälkeen pelivuorossa oleva pelaaja siirtyy automaattisesti nopan osoittaman silmäluvun verrran pelilaudalla. Samalla näkymän vasempaan osaan ilmestyy pelilaudan kategoriaruutua vastaava kysymys. Kun pelaaja on vastannut kysymykseen, oikea vastaus saadaan esiin "Show answer" -painikkeella.

Kun peli jatkuu jonkin aikaa, se voi näyttää esimerkiksi alla olevan kuvan kaltaiselta. Kuten huomataan, pelaajat ovat saaneet joihinkin kategorioihin pisteitä.

![Game Question](screenshots/game_question.png)

Oikean vastauksen lisäksi näkymään ilmestyy myös painikkeet, joilla pelaajan vastaus vahvistetaan joko oikeaksi tai vääräksi:

![Game Answer](screenshots/game_answer.png)

Painikkeet:

- "Player's answer was correct": pelaaja saa kategoriapisteen, mikäli kategoriassa ei vielä ole pistettä.
- "Player's answer was incorrect": pelaaja menettää kategoriapisteen, mikäli kategoriassa on piste.

Peli päättyy, kun yksi pelaajista pääsee aloitusruutuun tai sen yli kaikkien kategoriapisteiden kera. Esimerkiksi alla olevassa kuvassa pelaaja nimeltä "samushka" on voittanut pelin.

![Game End](screenshots/game_end.png)

Pelin päätyttyä sovellus ilmoittaa, kuka voitti, ja antaa mahdollisuuden palata pelin asetusten näkymään.
