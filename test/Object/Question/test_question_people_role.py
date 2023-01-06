from unittest import TestCase
from app.business_object.Question.question_people_role import QuestionPeopleRole


class TestQuestionPeopleRole(TestCase):
    def test_question_people_role(self):
        # GIVEN
        question = QuestionPeopleRole(
            name='Anthony Daniels',
            main_role='Acting',
            place_birth='Salisbury, Wiltshire, England, UK',
            date_birth='1946-02-21',
            date_death=None,
            is_dead=False
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
        self.assertEqual(question.type_question, 'people role')
        self.assertEqual(result, 'What is the main role of Anthony Daniels?')
        self.assertEqual(correct_answer, 'Acting')
        self.assertIsInstance(question, QuestionPeopleRole)
