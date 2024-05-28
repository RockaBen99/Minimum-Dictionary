from __future__ import annotations
import json


def generate_lists(dictionary_name: str):
    with open(f"{dictionary_name}.json") as file:
        full_dictionary: dict[str, dict[str, list[str]]] = json.load(file)
    
    defining_words: list[str] = []
    defined_words: list[list[str]] = []
    
    first_letter = ''
    
    for word in full_dictionary.keys():
        if word[0] != first_letter:
            first_letter = word[0]
            print(first_letter)
        definitions = full_dictionary[word]["MEANINGS"]
        definitions_list: list[str] = []
        for definition in definitions:
            definitions_list += definition[1].upper().split()
            definitions_list.append(definition[0].upper())
        for defining_word in definitions_list:
            defining_word = strip_trailing_non_letters(defining_word)
        definitions_list = list(set(definitions_list))
        dict()
        if not word in defining_words:
            defining_words.append(word)
            defined_words.append([])
        for definer in definitions_list:
            if not definer in defining_words:
                defining_words.append(definer)
                defined_words.append([word])
            else:
                defined_words[defining_words.index(definer)].append(word)
                
    return defining_words, defined_words
            
        
def strip_trailing_non_letters(defining_word: str):
    try:
        defining_word[-1]
    except IndexError:
        stripped_word = ''
    else:
        if not defining_word[-1].isalnum():
            stripped_word = defining_word[:-1]
            strip_trailing_non_letters(stripped_word)
        else:
            stripped_word = defining_word
    return stripped_word




if __name__ == "__main__":
    print("start")
    words, defined = generate_lists("test_section")
    with open("word_dependancies.json", "w") as file:
        json.dump([words, defined], file)

    print("end")