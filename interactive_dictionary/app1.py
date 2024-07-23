import json
from difflib import get_close_matches
import sys

def quit_app():
    quit=input("\nDo you wish to continue: (Y/n)")
    if quit == "Y":
        return
    elif quit == "n":
        sys.exit()
    else:
        print("Brother do as your'e told (-_-)")
        quit_app()


def file_search(word):
    if word in dictionary:
        output= dictionary[word]
        for i in output:
            print(i)
        quit_app()
        replace_word=input("what more do you wanna know?").lower().strip()
        file_search(replace_word)
        return
    elif len(get_close_matches(word, dictionary.keys()))>0:
            print("did you mean %s instead" %get_close_matches(word, dictionary.keys())[0] )
            match_word=input("what is your corrected search?").lower().strip()#to prevent code break
            file_search(match_word)
    else:
        print("word doesn't exist(^_^).\n search for another word!!")
        replace_word=input().lower().strip()#so you aren't confused yet again: this is the input for the preceding  code
        file_search(replace_word)
        
    quit_app()
    # file_search(word)
    

# def repeat_search(repeat):
#     if repeat in dictionary:
#         print(dictionary[repeat])
#     else:
#         print("word doesn't exist(^_^).\n search for another word!!")
#         replace_repeat=input()
#         repeat_search(replace_repeat)
#     quit_app()
    



       
dictionary= json.load(open("/mnt/23C62AAA2960B420/PY_REPO/interactive_dictionary/data.json"))
# def input(word):
#     word=input("What word do you wish to understand today?:")
#     return word
word=input("What word do you wish to understand today?:").lower().strip()
file_search(word)
#repeat= input("what else do you wanna know?").lower().strip()
#repeat_search(repeat)
quit_app()