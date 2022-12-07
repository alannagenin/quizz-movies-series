from unittest import TestCase
from BusinessObject.Question.question_movie_genre import QuestionMovieGenre

class TestQuestionMovieGenre(TestCase):
    def test_question_movie_genre(self):
        # GIVEN
        question = QuestionMovieGenre(
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
        all_correct_answers = question.get_all_correct_answer()
        # THEN
        self.assertEqual(result, 'What is the main genre of the movie The Fifth Element?')
        self.assertEqual(correct_answer, 'Adventure')
        self.assertEqual(all_correct_answers, ['Adventure', 'Fantasy', 'Action', 'Thriller', 'Science Fiction'])
        self.assertIsInstance(question, QuestionMovieGenre)

