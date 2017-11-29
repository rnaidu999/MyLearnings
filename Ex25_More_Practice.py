from sys import argv
script, sentence=argv
#sentence="Sateesh Naidu Dhanvi Soujanya Avirneni Raja Gagana Ashok";

def break_words(sentence):
    words=sentence.split(' ')
    return words

def sort_words(words):
    return sorted(words)

def print_first_word(words):
    fword=words.pop(0)
    print (fword)

def print_last_word(words):
    lword=words.pop (-1)
    print (lword)

def sort_sentence(sentence):
    words=break_words(sentence)
    return sort_words(words)

def print_first_last_word(sentence):
    words=break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    words1 = sort_sentence(sentence)
    print_first_word(words1)
    print_last_word(words1)

print (break_words(sentence))
words=break_words(sentence)
print (sort_words(words))
print_first_word(words)
print_last_word(words)
print (sort_sentence(sentence))
print_first_last_word(sentence)
print_first_and_last_sorted(sentence)
