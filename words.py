# this should print "HELLO", "HEY", "YO", and "YES"

# print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
#                    must_start_with={"h", "y"})

list = ["apple", "banana", "cherry", "dragon",
        'ear', "fun", "good", "hello", "lion"]

must_start_with = {"a", "b"}


def print_upper_words(word_list, start_with):
    starting_letters = [i.upper() for i in start_with]
    print(starting_letters)
    for word in word_list:
        if word[0].upper() in starting_letters:
            print(word.upper())


print_upper_words(list, must_start_with)
