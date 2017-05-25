# Python

sentence = raw_input()

# Ham tách chữ
def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

#Hàm sắp xếp chữ
def sort_words(words):
    """Sorts the words."""
    return sorted(words)

#hàm in chữ đầu tin trong chuối
def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print word

#Hàm in chữ cuối trong chuỗi
def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print word

# Hàm sort sentence
def sort_sentence(sentence):
    """Take in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

# Hàm in chứ đầu và cuối trong 1 chuỗi
def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

# Hàm in chữ đàu và cuối trong 1 chuỗi đã được sắp xếp (sort) trước đó
def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

print "The sentence returns the sorted words:"
    sort_sentence(sentence)

print "The first and last words of the sentence:"
    print_first_and_last(sentence)

print "The first and last words of sentence after sorted:"
    print_first_and_last_sorted(sentence)
