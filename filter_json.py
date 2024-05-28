from __future__ import annotations
import json


def generate_lists(dictionary_name: str):
    with open(f"{dictionary_name}.json") as file:
        full_dictionary: dict[str, dict[str, list[str]]|str] = json.load(file)
    
    defining_words: list[str] = []
    defined_words: list[list[str]] = []
    
    words_processed = 0
    
    for word in full_dictionary.keys():
        words_processed += 1
        print(f'{words_processed}/{len(full_dictionary)}')
        definitions_list = get_definition_list(full_dictionary, word)
        formatted: list[str] = []
        for defining_word in definitions_list:
            defining_word = strip_trailing_non_letters(defining_word)
            if defining_word in full_dictionary.keys():
                formatted.append(defining_word)
        definitions_list = list(set(formatted))
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


def get_definition_list(full_dictionary: dict[str, dict[str, list[str]]|str], word: str) -> list[str]:
    if isinstance(list(full_dictionary.values())[0], str):
        return full_dictionary[word].split() # type: ignore
    else:
        definitions = full_dictionary[word]["MEANINGS"] # type: ignore
        definitions_list: list[str] = []
        for definition in definitions:
            definitions_list += definition[1].upper().split()
            definitions_list.append(definition[0].upper())
        return definitions_list
        

def strip_trailing_non_letters(defining_word: str):
    try:
        defining_word[-1]
    except IndexError:
        stripped_word = ''
    else:
        if not defining_word[-1].isalpha():
            stripped_word = defining_word[:-1]
            strip_trailing_non_letters(stripped_word)
        elif not defining_word[0].isalpha():
            stripped_word = defining_word[1:]
            strip_trailing_non_letters(stripped_word)
        else:
            stripped_word = defining_word
    return stripped_word




if __name__ == "__main__":
    print("start")
    words, defined = generate_lists("dictionary_compact")
    with open("word_dependancies.json", "w") as file:
        json.dump([words, defined], file)

    print("end")