from unittest import TestCase
from Object.Question.question_people_is_dead import QuestionPeopleIsDead


class TestQuestionPeopleIsDead(TestCase):
    def test_people_is_not_dead(self):
        # GIVEN
        question = QuestionPeopleIsDead(
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
        self.assertEqual(question.type_question, 'people is dead')
        self.assertEqual(result, 'Is Anthony Daniels dead?')
        self.assertEqual(correct_answer, False)
        self.assertIsInstance(question, QuestionPeopleIsDead)

    def test_people_is_dead(self):
        # GIVEN
        question = QuestionPeopleIsDead(
            name='Judith Barsi',
            main_role='Acting',
            place_birth='Los Angeles, California, USA',
            date_birth='1978-06-06',
            date_death='1988-07-25',
            is_dead=True
        )
        # WHEN
        result = question.display_question()
        correct_answer = question.get_correct_answer()
        # THEN
        self.assertEqual(question.name, 'Judith Barsi')
        self.assertEqual(question.main_role, 'Acting')
        self.assertEqual(question.place_birth, 'Los Angeles, California, USA')
        self.assertEqual(question.date_birth, '1978-06-06')
        self.assertEqual(question.date_death, '1988-07-25')
        self.assertEqual(question.is_dead, True)
        self.assertEqual(question.type_question, 'people is dead')
        self.assertEqual(result, 'Is Judith Barsi dead?')
        self.assertEqual(correct_answer, True)
        self.assertIsInstance(question, QuestionPeopleIsDead)
