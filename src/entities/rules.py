class Rules:
    def __init__(self):
        self.rules = """

            Trivioboros

            Kierretään ympyränmuotoista pelilautaa.

            Pelaaja saa kategoriapisteen vastattuaan kategoriaan oikein.
            Jokaista kategoriaa vastaa yksi (tai useampi) piste.
            Mikäli pelaaja vastaa väärin kategoriaan, tämä menettää kyseisen kategorian pisteen.
            Mikäli pelaajalla ei ole kategoriassa pistettä, tämä ei menetä mitään.

            Aloitusruutu toimii myös erikoiskategoriana, josta täytyy saada myös piste.

            Se pelaaja voittaa, joka ensimmäisenä pääsee aloitusruutuun
            tai sen yli kaikkien kategoriapisteiden kanssa.

            Vaikeustasoon voi vaikuttaa monella tapaa. Vaikeustaso kasvaa, kun
            -laudan koko kasvaa,
            -kategorioiden määrä kasvaa,
            -noppien määrä pienenee,
            -kategoriapisteiden määrä kasvaa.

        """
