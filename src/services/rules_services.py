def get_game_rules_title():
    title = "Trivioboros"
    return title

def get_game_rules_text():
    text = """ Yleistä:

- Pelaajat aloittavat mustasta ruudusta ('aloitusruutu').
- Pelin aloittaa Pelaaja 1, ja vuorot vaihtuvat järjestyksessä.
- Jokaista peliin valittua kategoriaa edustaa yksi kategoriapiste.
- Pistetilannetta voi seurata pelilaudan vasemmasta ylälaidasta löytyvän pistetaulukon avulla.


Pelin kulku:

1. Vuorossa oleva pelaaja heittää noppaa.
2. Pelaaja siirtyy laudalla myötäpäivään nopan osoittaman silmäluvun verran.
3. Pelaajalle esitetään kysymys kategoriasta, jonka edustamaan ruutuun tämä on siirryttyään päätynyt.
    - Mikäli pelaaja vastaa oikein, hän saa pisteen kyseisestä kategoriasta.
    - Mikäli pelaajalla on jo kategoriasta piste, tämä ei saa uutta pistettä.
    - Mikäli pelaaja vastaa väärin, hän menettää kategoriapisteen.
    - Mikäli pelaajalla ei ole kategoriassa pistettä, tämä ei menetä mitään.
4. Vuoro vaihtuu.


Pelin päättyminen:

- Pelin voittaa se, joka ensimmäisenä pääsee aloitusruutuun tai sen yli kaikkien kategoriapisteiden kanssa.
- Mikäli samalla kierroksella useampi pelaaja onnistuu tässä, voitto jaetaan.


Vaikeustaso:

- Pelin vaikeustasoon voi vaikuttaa monella tapaa, ja yhdistelmiä on useita. 
- Pääsääntöisesti vaikeustaso kasvaa pelilaudan kokoa tai kysymyskategorioiden määrää kasvattamalla.
- Erilaisia yhdistelmiä kannattaa rohkeasti kokeilla! """

    return text
