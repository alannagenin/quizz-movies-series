from unittest import TestCase
from app.business_object.Question.question_series_nb_episodes_total import QuestionSeriesNumberEpisodesTotal


class TestQuestionSeriesNumberEpisodesTotal(TestCase):
    def test_question_series_nb_episodes_total(self):
        # GIVEN
        question = QuestionSeriesNumberEpisodesTotal(
            series_title='Gimme Gimme Gimme',
            original_series_title='Gimme Gimme Gimme',
            first_air_date='1999-01-08',
            last_air_date='2001-12-14',
            nb_episodes_per_season=[2, 6, 6, 6],
            nb_episodes_tot=20,
            nb_seasons=4,
            tv_host=['BBC One', 'BBC Two'],
            genres_name=['Comedy'],
            spoken_languages=['English'],
            plot="Linda La Hughes (Kathy Burke) shares a flat with Tom Farrell"
            " (James Dreyfus). Linda is overweight, loudmouthed and not "
            "particularly attractive. She thinks she's gorgeous and irrestible"
            ", however. She's also sex mad and obsessed with men. Tom is an "
            "aspiring actor. He's got an agent, but finds it difficult to get"
            "parts. He doesn't like Linda much, in spite of (or perhaps "
            "because of) the fact that they share a flat. She isn't completely"
            " comfortable with his homosexuality, perhaps because she finds it"
            " difficult to live with a man who doesn't find her sexually "
            "attractive."
        )
        # WHEN
        result = question.display_question()
        correct_answer = question.get_correct_answer()
        # THEN
        self.assertEqual(question.series_title, 'Gimme Gimme Gimme')
        self.assertEqual(question.original_series_title, 'Gimme Gimme Gimme')
        self.assertEqual(question.first_air_date, '1999-01-08')
        self.assertEqual(question.last_air_date, '2001-12-14')
        self.assertEqual(question.nb_episodes_per_season, [2, 6, 6, 6])
        self.assertEqual(question.nb_episodes_tot, 20)
        self.assertEqual(question.nb_seasons, 4)
        self.assertEqual(question.tv_host, ['BBC One', 'BBC Two'])
        self.assertEqual(question.genres_name, ['Comedy'])
        self.assertEqual(question.spoken_languages, ['English'])
        self.assertEqual(
            question.plot,
            "Linda La Hughes (Kathy Burke) shares a flat with Tom Farrell"
            " (James Dreyfus). Linda is overweight, loudmouthed and not "
            "particularly attractive. She thinks she's gorgeous and irrestible"
            ", however. She's also sex mad and obsessed with men. Tom is an "
            "aspiring actor. He's got an agent, but finds it difficult to get"
            "parts. He doesn't like Linda much, in spite of (or perhaps "
            "because of) the fact that they share a flat. She isn't completely"
            " comfortable with his homosexuality, perhaps because she finds it"
            " difficult to live with a man who doesn't find her sexually "
            "attractive."
        )
        self.assertEqual(
            question.type_question,
            'series number episodes total'
        )
        self.assertEqual(
            result,
            'How many episodes does the series Gimme Gimme Gimme have?'
        )
        self.assertEqual(correct_answer, 20)
        self.assertIsInstance(question, QuestionSeriesNumberEpisodesTotal)
