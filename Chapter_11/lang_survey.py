from survey import AnnonSurvey

questions = "What language did you speak first?"
my_survey = AnnonSurvey(questions)

my_survey.show_questions()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)

print("Here are your results: ")
my_survey.show_results()