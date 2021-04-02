class Rules:
    def __init__(self):
        self.rules = """
            Trivioboros

            Kierretään ympyränmuotoista pelilautaa.
            Mitä pienempi lauta, sitä haastavampi peli (jatkokehitysjuttu).

            Jos pelaaja ei saa oikeita vastauksia johonkin kategoriaan kierroksen aikana, 
            pelaaja menettää kategorian pisteen.
            Jos pistettä ei vielä kategoriassa ole, pelaaja ei menetä mitään.
            HUOM: Pisteitä voisi seurata siten, että lasketaan oikeat vastaukset kategoriassa
            ja kierroksen loputtua verrataan määrää tyyliin 
            'if correct_answers_in_category_x == 0: remove_category_point'.
        """
