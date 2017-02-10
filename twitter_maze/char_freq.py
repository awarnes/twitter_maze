"""
Use letter frequency tables to generate a list of letters as they are likely to appear in English.
"""
from math import ceil


def get_data(filename):
    with open(filename, 'r') as file:
        text = file.read()
        return text


def letter_frequency(filename):
    """
    Build a list of each letter according to the frequency table.
    """

    data = get_data(filename)
    lines = data.split('\n')
    letters = list()

    for letter in lines[:-1]:    # Why is there an extra empty string at the end of lines?
        pair = letter.split()
        times = ceil(float(pair[1]))
        freq = list(pair[0] * times)
        letters += freq

    return letters


def punc_frequency(filename):
    """
    Build a list of each punctuation mark according to the frequency table
    """

    data = get_data(filename)
    lines = data.split('\n')
    marks = list()

    for mark in lines[:-1]:
        pair = mark.split()
        times = ceil(float(pair[1]) / 5)   # Make this extensible by replacing 5 with the min of the frequencies somehow
        huh = list(pair[0] * times)
        marks += huh

    return marks


def char_frequency(letter_file, punc_file):
    """
    Combine letters, punctuation, and spaces.
    """

    letters = letter_frequency(letter_file) * 10
    marks = punc_frequency(punc_file)
    spaces = list(' ' * 30)

    all_chars = letters + marks + spaces

    return all_chars
