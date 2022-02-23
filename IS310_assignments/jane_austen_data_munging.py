# jane_austen_data_munging.py
import re


def main():
    sentence = clean_sentence()
    print(sentence)
    word_to_replace = input("Please input a word to replace: ")
    while sentence.lower().find(word_to_replace) == -1:
        print("Word is not found")
        word_to_replace = input("Please input a word to replace: ")
    new_word = input("Please enter a new word: ")
    compiled = re.compile(re.escape(word_to_replace), re.IGNORECASE)
    sentence_replaced = compiled.sub(new_word, sentence)
    print(sentence_replaced)



def clean_sentence():
    jane = "The Project Gutenberg EBook of Pride and Prejudice, by Jane Austen This eBook is for the use of anyone anywhere at no cost and with almost no restrictions whatsoever. You may copy it, give it away or re-use it under the terms of the Project Gutenberg License included with this eBook or online at www.gutenberg.org Title: Pride and Prejudice Author: Jane Austen Posting Date: August 26, 2008 Release Date: June, 1998 Last Updated: March 10, 2018 Language: English Character set encoding: UTF-8 START OF THIS PROJECT GUTENBERG EBOOK PRIDE AND PREJUDICE Produced by Anonymous Volunteers PRIDE AND PREJUDICE By Jane Austen Chapter 1 It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife."
    splitPoint = "Produced by Anonymous Volunteers"
    jane_cleaned = jane[jane.find(splitPoint):]
    jane_cleaned = jane_cleaned.replace("man", "person")
    jane_cleaned = jane_cleaned.replace("wife", "parther")
    return jane_cleaned


main()