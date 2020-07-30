import unittest
from survey import AnnonSurvey

class TestSurvey(unittest.TestCase):
    def test_store_single_response(self):
        questions = "What language did you first learn to sepeak"
        my_survey=AnnonSurvey(questions)
        my_survey.store_response('English')
        self.assertIn('English', my_survey.responses)

    def test_store_three_responses(self):
        questions= "What language did you first learn to sepeak"
        my_survey= AnnonSurvey(questions)
        responses= ['English', 'Spanish', 'Mandarin']
        for response in responses:
            my_survey.store_response(response)
        
        for response in responses:
            self.assertIn(response, my_survey.responses)


if __name__=='__main__':
    unittest.main()