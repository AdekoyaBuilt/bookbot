def get_num_words(text):
    words = text.split()
    count = len(words)

    return count

def count_character_appear(book):
    letters = {}
    for letter in book:
        lowered = letter.lower()
        if lowered in letters:
            letters[lowered] += 1
        else:
            letters[lowered] = 1
    
    return letters

def sort_on(items):
    return items["num"]

def sort_dict(unsorted):
    input_data = [] 

    for item in unsorted:
        count = unsorted[item]
        input_data.append({"char": item, "num": count})
    
    input_data.sort(reverse=True, key=sort_on)
    return input_data
