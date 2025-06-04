def word_counter(text):
    word_count = len(text.split())
    return word_count

def letter_counter(text):
    characters = {}
    for letter in text.lower():
        present_letter = letter in characters
        if present_letter == True:
            characters[letter] += 1
        else:
            characters[letter] = 1      
    return characters

def letter_sorter(letters_dict):
    sorted_letters = sorted(letters_dict.items(), key=lambda item: item[1], reverse=True)
    dict_list = [{'char': letter, 'num': count} for letter, count in sorted_letters]
    return dict_list
