from unittest import TestCase
from BusinessObject.Question.question_people_birth_place import QuestionPeopleBirthPlace


class TestQuestionPeopleBirthPlace(TestCase):
    def test_question_people_birth_place(self):
        # GIVEN
        question = QuestionPeopleBirthPlace(
            name='Anthony Daniels',
            main_role='Acting',
            place_birth='Salisbury, Wiltshire, England, UK',
            date_birth='1946-02-21',
            date_death=None,
            is_death=False
        )
        # WHEN
        result = question.display_question()
        correct_answer = question.get_correct_answer()
        # THEN
        self.assertEqual(question.name, 'Anthony Daniels')
        self.assertEqual(question.main_role, 'Acting')
        self.assertEqual(question.place_birth, 'Salisbury, Wiltshire, England, UK')
        self.assertEqual(question.date_birth, '1946-02-21')
        self.assertEqual(question.date_death, None)
        self.assertEqual(question.is_dead, False)
        self.assertEqual(question.type_question, 'people birth place')
        self.assertEqual(result, 'Where is Anthony Daniels born?')
        self.assertEqual(correct_answer, 'Salisbury, Wiltshire, England, UK')
        self.assertIsInstance(question, QuestionPeopleBirthPlace)
