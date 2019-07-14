"""
Student code for Word Wrangler game
"""

import urllib2
import codeskulptor
import poc_wrangler_provided as provided

codeskulptor.set_timeout(60)

WORDFILE = "assets_scrabble_words3.txt"


# Functions to manipulate ordered word lists

def remove_duplicates(list1):
    """
    Eliminate duplicates in a sorted list.

    Returns a new sorted list with the same elements in list1, but
    with no duplicates.

    This function can be iterative.
    """
    answer = list1[::]
    for idx in range(len(list1) - 1):
        if list1[idx] == list1[idx + 1]:
            answer.remove(list1[idx])
    return answer

def intersect(list1, list2):
    """
    Compute the intersection of two sorted lists.

    Returns a new sorted list containing only elements that are in
    both list1 and list2.

    This function can be iterative.
    """
    answer = []
    for element in list1:
        if element in list2:
            answer.append(element)     
    return remove_duplicates(answer)

# Functions to perform merge sort

def merge(list1, list2):
    """
    Merge two sorted lists.

    Returns a new sorted list containing those elements that are in
    either list1 or list2.

    This function can be iterative.
    """  
    answer = []
    list2_copy = list2[::]
    for idx in range(len(list1)):
        while len(list2_copy) > 0 and list1[idx] >= list2_copy[0]:
            answer.append(list2_copy[0])
            list2_copy.pop(0)
        answer.append(list1[idx])
    answer += list2_copy
    return answer

def merge_sort(list1):
    """
    Sort the elements of list1.

    Return a new sorted list with the same elements as list1.

    This function should be recursive.
    """
    list_copy = list1[::]
    if len(list_copy) <= 1:
        return list_copy
    else:
        return merge(merge_sort(list_copy[:len(list_copy)/2]), 
                     merge_sort(list_copy[len(list_copy)/2:]))

   
# Function to generate all strings for the word wrangler game

def gen_all_strings(word):
    """
    Generate all strings that can be composed from the letters in word
    in any order.

    Returns a list of all strings that can be formed from the letters
    in word.

    This function should be recursive.
    """
    answer = []
    if len(word) == 0:
        return [""]
    else:
        first = word[0]
        rest = word[1:]
        rest_strings = gen_all_strings(rest)
        for rest_string in rest_strings:
            for idx in range(len(rest_string) + 1):
                answer.append(rest_string[:idx] + first + rest_string[idx:])            
        return gen_all_strings(rest) + answer

# Function to load words from a file

def load_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """
    word_list = []

    url = codeskulptor.file2url(filename)
    netfile = urllib2.urlopen(url)
    
    for line in netfile.readlines():
        word_list.append(line[:-1])
    return word_list

def run():
    """
    Run game.
    """
    words = load_words(WORDFILE)
    wrangler = provided.WordWrangler(words, remove_duplicates, 
                                     intersect, merge_sort, 
                                     gen_all_strings)
    provided.run_game(wrangler)

# Uncomment when you are ready to try the game
run()
