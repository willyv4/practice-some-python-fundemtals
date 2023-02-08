
list = ["apple", "banana", "cherry", "dragon",
        'ear', "fun", "good", "hello", "lion"]

must_start_with = {"a", "b"}


def print_upper_words(word_list, start_with):
    """
    this function prints words that start with a specified letter

    we have the list at the top and variable called must start with
    we pass these as parameters in the print_upper_words function

    starting_letters takes each letter in a list and seperates it
    and makes it upper case

    then we take each word from the word_list
    and check if the word's first letter is one
    one of the staring_letters we specified

    if it is it will print the words from the list
    that start with the letters specified in the must_start_with variable.
    """

    starting_letters = [i.upper() for i in start_with]
    for word in word_list:
        if word[0].upper() in starting_letters:
            print(word.upper())


print_upper_words(list, must_start_with)
