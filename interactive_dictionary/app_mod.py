"""
import json
import sys

# Function to prompt the user to continue or exit the application
def quit_app():
    user_input = input("Do you wish to continue: (Y/n) ")
    if user_input == "Y":
        return
    elif user_input == "n":
        sys.exit()
    else:
        print("Brother, do as you're told (-_-)")
        quit_app()

# Function to search for a word in the dictionary and handle user input
def file_search(word):
    if word in dictionary:
        # Print the definition if the word exists in the dictionary
        print(dictionary[word])
    else:
        # Notify the user if the word doesn't exist and prompt for another word
        print("Word doesn't exist (^_^). Search for another word!")
        word = input("Enter another word: ")
        file_search(word)
        return
    
    # Ask the user if they want to know more
    replace_word = input("What more do you want to know? ")
    file_search(replace_word)
    quit_app()

# Function to search for a repeated word in the dictionary
def repeat_search(repeat):
    if repeat in dictionary:
        # Print the definition if the word exists in the dictionary
        print(dictionary[repeat])
    else:
        # Notify the user if the word doesn't exist and prompt for another word
        print("Word doesn't exist (^_^). Search for another word!")
        repeat = input("Enter another word: ")
        repeat_search(repeat)
    quit_app()

# Load the dictionary from the JSON file
dictionary = json.load(open("/mnt/23C62AAA2960B420/PY_REPO/interactive_dictionary/data.json"))

# Prompt the user to enter a word to understand
word = input("What word do you wish to understand today? ")
file_search(word)

# Prompt the user for any additional words they want to know
repeat = input("What else do you want to know? ")
repeat_search(repeat)

quit_app()
"""
import json
import sys

# Function to prompt the user to continue or exit the application
def quit_app():
    while True:
        user_input = input("Do you wish to continue: (Y/n) ").strip().lower()
        if user_input == "y":
            return
        elif user_input == "n":
            sys.exit()
        else:
            print("Brother, do as you're told (-_-)")

# Function to search for a word in the dictionary and handle user input
def search_word(word):
    while True:
        if word in dictionary:
            print(dictionary[word])
            quit_app()
            
        else:
            print("Word doesn't exist (^_^). Search for another word!")
        word = input("Enter another word: ")

# Load the dictionary from the JSON file
dictionary = json.load(open("/mnt/23C62AAA2960B420/PY_REPO/interactive_dictionary/data.json"))

# Prompt the user to enter a word to understand and search for it
word = input("What word do you wish to understand today? ")
search_word(word)

# Prompt the user for any additional words they want to know and search for them
repeat = input("What else do you want to know? ")
search_word(repeat)

quit_app()
