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
    with open(text) as f:
        file_content = f.read()
    for word in file_content:
        word = (word.lower())
        if word in dict_chars:
            dict_chars[word] += 1
        else:
            dict_chars[word] = 1
        
    return(dict_chars)

