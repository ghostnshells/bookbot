def number_of_words(file_path):
    file_contents = ""
    with open(file_path) as f:
        file_contents = f.read()
    words = file_contents.split()
    count = 0
    for word in words:
        count+=1
    return count

def number_of_chars(text):
    file_content = ""
    dict_chars = {}
    for word in text:
        word = (word.lower())
        if word in dict_chars:
            dict_chars[word] += 1
        else:
            dict_chars[word] = 1
        
    return(dict_chars)

def sort_on(items):
    return items["num"]
    
def sorted_dictionary(dictionary):
    result = []
    for ch in dictionary:
        result.append({"char": ch, "num": dictionary[ch]})
    result.sort(reverse=True, key=sort_on)
    return result
