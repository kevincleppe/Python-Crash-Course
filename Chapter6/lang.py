#creates a dictionary 
favorite_lang={
    'jen':'python',
    'kevin': 'also python',
    'joon': 'c',
    'eddie': 'ruby',
}
#assign's keys to a specific....thing?
#lang= favorite_lang['joon'].title()
#print(f"sarah's favorite lang is {lang}.")

#creates a for loop that will loop through the key pairs 
for name, i in favorite_lang.items():
    print(f"{name.title()}'s favorite language is {i.title()}.")
