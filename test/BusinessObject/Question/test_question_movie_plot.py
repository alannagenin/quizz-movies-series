from unittest import TestCase
from BusinessObject.Question.question_movie_plot import QuestionMoviePlot

class TestQuestionMoviePlot(TestCase):
    def test_question_movie_plot(self):
        # GIVEN
        question = QuestionMoviePlot(
        movie_title = 'The Fifth Element',
        original_movie_title = 'The Fifth Element',
        budget = 90000000,
        genres_name = ['Adventure', 'Fantasy', 'Action', 'Thriller', 'Science Fiction'],
        release_date = 1997,
        spoken_languages = ['English', 'Swedish', 'German'],
        plot = 'In 2257, a taxi driver is unintentionally given the task of saving a young girl who is part of the key that will ensure the survival of humanity.'
        )
        # WHEN
        result = question.display_question()
        correct_answer = question.get_correct_answer()
        # THEN
        self.assertEqual(result, 'Which movie best describes the description below?\nSynopsis: In 2257, a taxi driver is unintentionally given the task of saving a young girl who is part of the key that will ensure the survival of humanity.')
        self.assertEqual(correct_answer, 'The Fifth Element')
        self.assertIsInstance(question, QuestionMoviePlot)

