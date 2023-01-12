from unittest import TestCase
from app.business_object.Question.question_movie_release_date import QuestionMovieReleaseDate


class TestQuestionMovieReleaseDate(TestCase):
    def test_question_movie_release_date(self):
        # GIVEN
        question = QuestionMovieReleaseDate(
            movie_id=550,
            movie_title='The Fifth Element',
            original_movie_title='The Fifth Element',
            budget=90000000,
            genres_name=[
                'Adventure', 'Fantasy', 'Action', 'Thriller', 'Science Fiction'
            ],
            release_date=1997,
            spoken_languages=['English', 'Swedish', 'German'],
            main_actors=[
                {'name': 'Bruce Willis', 'character': 'Korben Dallas'},
                {'name': 'Milla Jovovich', 'character': 'Leeloo'},
                {'name': 'Gary Oldman', 'character': 'Jean-Baptiste Emmanuel Zorg'},
                {'name': 'Ian Holm', 'character': 'Father Vito Cornelius'},
                {'name': 'Chris Tucker', 'character': 'Ruby Rhod'},
                {'name': 'Luke Perry', 'character': 'Billy'},
                {'name': 'Brion James', 'character': 'General Munro'},
                {'name': "Tom 'Tiny' Lister Jr.", 'character': 'President Lindberg'},
                {'name': 'Lee Evans', 'character': 'Fog'},
                {'name': 'Charlie Creed-Miles', 'character': 'David'}],
            plot='In 2257, a taxi driver is unintentionally given the task of '
            'saving a young girl who is part of the key that will ensure the '
            'survival of humanity.'
        )
        # WHEN
        result = question.display_question()
        correct_answer = question.get_correct_answer()
        # THEN
        self.assertEqual(question.movie_title, 'The Fifth Element')
        self.assertEqual(question.original_movie_title, 'The Fifth Element')
        self.assertEqual(question.budget, 90000000)
        self.assertEqual(
            question.genres_name,
            ['Adventure', 'Fantasy', 'Action', 'Thriller', 'Science Fiction']
        )
        self.assertEqual(question.release_date, 1997)
        self.assertEqual(
            question.spoken_languages,
            ['English', 'Swedish', 'German']
        )
        self.assertEqual(
            question.plot,
            'In 2257, a taxi driver is unintentionally given the task of saving a young girl who is part of the key that will ensure the survival of humanity.')
        self.assertEqual(question.type_question, "movie release date")
        self.assertEqual(
            result,
            'When was the film The Fifth Element released?'
        )
        self.assertEqual(correct_answer, 1997)
        self.assertIsInstance(question, QuestionMovieReleaseDate)
