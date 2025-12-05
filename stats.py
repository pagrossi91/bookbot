from collections import Counter

def get_word_count(file_contents):
    print("----------- Word Count ----------")
    num_words = len(file_contents.split())
    print(f"Found {num_words} total words")
    return num_words

def get_char_count(file_contents):
    char_count = Counter(file_contents.lower())
    return dict(char_count)

def sorted_chars(dict):
    print("--------- Character Count -------")
    char_list = []
    for key in dict:
        value = dict[key]
        temp_dict = {"char": key,
                     "num": value}
        char_list.append(temp_dict)
    
    char_list.sort(key=lambda x: x['num'], reverse=True)

    for i in range(0, len(char_list) - 1):

        if char_list[i]["char"].isalpha():
            print(f"{char_list[i]["char"]}: {char_list[i]["num"]}")

    return