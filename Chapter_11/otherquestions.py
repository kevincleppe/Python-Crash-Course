from survey import AnnonSurvey

ques= "What do you do for work?"
new_survery=AnnonSurvey(ques)

new_survery.show_results
print("Press 'q' at any time to quit")
while True:
    response=input("Duty: ")
    if response == 'q':
        break
    new_survery.store_response(response)

print("Results are:")
new_survery.show_results()