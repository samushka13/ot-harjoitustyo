# Arkkitehtuurikuvaus

## Rakenne

Sovelluksen arkkitehtuuri on kolmitasoinen:

![Arkkitehtuurikuvaus](kuvat/arkkitehtuurikuvaus.png)

- Pakkaus "ui" tarkoittaa käyttöliittymästä vastaavaa koodia.
- Pakkaus "services" tarkoittaa sovelluslogiikasta vastaavaa koodia.
- Pakkaus "repository" tarkoittaa tietojen tallennuksesta vastaavaa koodia.

Lisäksi: pakkaus "entities" kuvastaa sovelluksen käyttämien tietokohteiden luokkia.

## Käyttöliittymä

Käyttöliittymä ("ui") on eristetty sovelluslogiikasta ("services") ja tietojen pysyväistallennuksesta ("repository"). Käyttöliittymä kutsuu tarvittaessa eri "services"-luokkia ja niiden metodeja, muttei koskaan "repository"-luokkaa.

Käyttöliittymä koostuu neljästä erillisestä päänäkymästä:

- "Login or Create Username",
- "Game Settings",
- "Custom Content",
- "Game Session".

Lisäksi

- "Custom Content" sisältää erillisen "Edit"-alanäkymän,
- "Game Settings" ja "Game Session" sisältävät erillisen "Rules"-alanäkymän,
- "Game Session" sisältää erillisen "Statistics"-alanäkymän.

Kaikki pää- ja alanäkymät on toteutettu omina luokkinaan. Pääsääntöisesti vain yksi näistä näkyy käyttäjälle kerrallaan, poikkeuksena "Rules"- ja "Statistics"-alanäkymät.

## Palvelut

Palvelut koostuvat "services"-luokista, joita on yhteensä neljä:

- "LoginServices" vastaa kirjautumiseen liittyvistä palveluista.
- "SettingsServices" vastaa pelin asetuksiin liittyvistä palveluista.
- "CustomContentServices" vastaa käyttäjän luomien sisältöjen hallintaan liittyvistä palveluista.
- "GameServices" vastaa pelisessioon liittyvistä palveluista.

## Tietojen pysyväistallennus

Tietojen tallennuksesta vastaa "DatabaseServices"-luokka, joka on kaikkien "services"-luokkien käytössä. Kaikki tiedot tallennetaan SQLite-tietokantaan, joka koostuu kolmesta taulusta:

- "Users", joka säilöö käyttäjiin liittyvää tietoa,
- "Questions", joka säilöö kysymyksiin liittyvää tietoa,
- "Games", joka säilöö pelattuihin peleihin liittyvää tietoa.

Tietokantatiedoston nimi on konfiguroitavissa. 
