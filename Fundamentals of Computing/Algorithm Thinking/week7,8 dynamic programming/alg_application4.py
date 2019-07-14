# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 16:40:23 2018

@author: Saki
"""


# =============================================================================
# Provide code and solution for Application 4
# =============================================================================

DESKTOP = True

import math
import random
import urllib2

if DESKTOP:
    import matplotlib.pyplot as plt
    import ComputingAlignmentsOfSequences as fun
else:
    import simpleplot
    import userXX_XXXXXXX as student
    

# URLs for data files
PAM50_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_PAM50.txt"
HUMAN_EYELESS_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_HumanEyelessProtein.txt"
FRUITFLY_EYELESS_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_FruitflyEyelessProtein.txt"
CONSENSUS_PAX_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_ConsensusPAXDomain.txt"
WORD_LIST_URL = "http://storage.googleapis.com/codeskulptor-assets/assets_scrabble_words3.txt"



###############################################
# provided code

def read_scoring_matrix(filename):
    """
    Read a scoring matrix from the file named filename.  

    Argument:
    filename -- name of file containing a scoring matrix

    Returns:
    A dictionary of dictionaries mapping X and Y characters to scores
    """
    scoring_dict = {}
    scoring_file = urllib2.urlopen(filename)
    ykeys = scoring_file.readline()
    ykeychars = ykeys.split()
    for line in scoring_file.readlines():
        vals = line.split()
        xkey = vals.pop(0)
        scoring_dict[xkey] = {}
        for ykey, val in zip(ykeychars, vals):
            scoring_dict[xkey][ykey] = int(val)
    return scoring_dict




def read_protein(filename):
    """
    Read a protein sequence from the file named filename.

    Arguments:
    filename -- name of file containing a protein sequence

    Returns:
    A string representing the protein
    """
    protein_file = urllib2.urlopen(filename)
    protein_seq = protein_file.read()
    protein_seq = protein_seq.rstrip()
    return protein_seq


def read_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """
    # load assets
    word_file = urllib2.urlopen(filename)
    
    # read in files as string
    words = word_file.read()
    
    # template lines and solution lines list of line string
    word_list = words.split('\n')
    print "Loaded a dictionary with", len(word_list), "words"
    return word_list

# =============================================================================
# Q1~3
# =============================================================================

PAM50 = read_scoring_matrix(PAM50_URL)
HumanEyelessProtein = read_protein(HUMAN_EYELESS_URL)
FruitflyEyelessProtein = read_protein(FRUITFLY_EYELESS_URL)

def q1():
    q1_alignment = fun.compute_alignment_matrix(HumanEyelessProtein, FruitflyEyelessProtein, PAM50, False)
    return fun.compute_local_alignment(HumanEyelessProtein, FruitflyEyelessProtein, PAM50, q1_alignment)

ConsensusPAXDomain = read_protein(CONSENSUS_PAX_URL)

def q2():
    human_local = q1()[1]
    fruitfly_local = q1()[2]
    human_local = human_local.replace('-', '')
    fruitfly_local = fruitfly_local.replace('-', '')
    
    human_align = fun.compute_alignment_matrix(human_local, ConsensusPAXDomain, PAM50, True)
    fruitfly_align = fun.compute_alignment_matrix(fruitfly_local, ConsensusPAXDomain, PAM50, True)
    
    human_global = fun.compute_global_alignment(human_local, ConsensusPAXDomain, PAM50, human_align)[1:]
    fruitfly_global = fun.compute_global_alignment(fruitfly_local, ConsensusPAXDomain, PAM50, fruitfly_align)[1:]
    
    human_len = len(human_global[0])
    human_same = 0.0
    for idx in range(human_len):
        if human_global[0][idx] == human_global[1][idx]:
            human_same += 1
    human_same /= human_len  
    
    fruitfly_len = len(fruitfly_global[0])
    fruitfly_same = 0.0
    for idx in range(fruitfly_len):
        if fruitfly_global[0][idx] == fruitfly_global[1][idx]:
            fruitfly_same += 1
    fruitfly_same /= fruitfly_len
    
    return (human_same,fruitfly_same)
 

# =============================================================================
# Quick calculation of likelihood of agreements of sequence of amino acids
# assuming that characters are randomly distributed
# =============================================================================

import math

ALPHABET_SIZE = 23
SEQ_LENGTH = 130
MIN_MATCHES = 90

def binomial_term(matches, total_length, alphabet_size):
    """
    Compute terms of the binomial expansion with probability equal to 
    one over alphabet size
    """
    
    prob = 1.0 / alphabet_size
    non_matches = total_length - matches
    combinations = (math.factorial(total_length) / 
                   (math.factorial(matches) * math.factorial(non_matches)))
    return  combinations * (prob ** matches) * (1 - prob) ** (non_matches) 

# compute probability of terms MIN_MATCHES or more characters matching out of 
# a sequence of SEQ_LENGTH
#print sum([binomial_term(possible_matches, SEQ_LENGTH, 23) for possible_matches 
#           in range(MIN_MATCHES, SEQ_LENGTH + 1)])
    
# =============================================================================
# Q4
# =============================================================================
def generate_null_distribution(seq_x, seq_y, scoring_matrix, num_trials):
    """
    Generate a random permutation of the sequence seq_y using random.shuffle().
    Compute the maximum value score for the local alignment of seq_x and rand_y using the score matrix scoring_matrix.
    Increment the entry score in the dictionary scoring_distribution by one.
    
    Input:Two sequences: seq_x, seq_y; scoring_matrix; num_trials
      
    Output:n a dictionary represents an un-normalized distribution 
    """
    scoring_distribution = {}
    for _ in range(num_trials):
        rand_y = list(seq_y)
        random.shuffle(rand_y)
        rand_y = "".join(rand_y)
        rand_alignment = fun.compute_alignment_matrix(seq_x, rand_y, scoring_matrix, False)
        score = fun.compute_local_alignment(seq_x, rand_y, scoring_matrix, rand_alignment)[0]
        if score in scoring_distribution.keys():
            scoring_distribution[score] += 1
        else:
            scoring_distribution[score] = 1
    return scoring_distribution

#q4 = generate_null_distribution(HumanEyelessProtein, FruitflyEyelessProtein, PAM50, 1000)

def a4q4_plot(x, y):
    plt.title("Null distribution in human and fruitfly(1000 trials)")
    plt.xlabel("Scores of local alignment")
    plt.ylabel("Scores / Trails")
    plt.bar(x, y)
    plt.show() 

a4q4_plot(sorted(q4.keys()), [q4[k]/1000.0 for k in q4.keys()])

# =============================================================================
# q5
# =============================================================================
import numpy as np

def q5():
    total = []
    for k,v in q4.items():
        for _ in range(v):
            total.append(k)
    mean = np.mean(total)
    std = np.std(total)
    z_value = (q1()[0] - mean) / std
    return mean,std,z_value


# =============================================================================
# q8
# =============================================================================
import string
alphabet = set(string.ascii_lowercase)
word_list = read_words(WORD_LIST_URL)

def check_spelling(checked_word, dist, word_list):
    diag_score = 2
    off_diag_score = 1
    dash_score = 0
    scoring_matrix = fun.build_scoring_matrix(alphabet, diag_score, off_diag_score, dash_score)
    
    word_within = []
    for word in word_list:
        alignment_matrix = fun.compute_alignment_matrix(checked_word, word, scoring_matrix, True)
        score = fun.compute_global_alignment(checked_word, word, scoring_matrix, alignment_matrix)[0]
        if (len(word) + len(checked_word) - score) <= dist:
            word_within.append(word)
    return word_within

def q8():
    checked_word1 = "humble"
    checked_word2 = "firefly"
    dist1 = 1
    dist2 = 2
    q8_1 = check_spelling(checked_word1, dist1, word_list)
    q8_2 = check_spelling(checked_word2, dist2, word_list)
    return (q8_1,q8_2)

