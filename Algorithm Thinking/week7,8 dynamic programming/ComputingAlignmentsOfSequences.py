# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 00:57:54 2018

@author: Saki
"""
def build_scoring_matrix(alphabet, diag_score, off_diag_score, dash_score):
    """
    Input: alphabet(a set of characters); diag_score(score for remaining 
    diagonal entries); off_diag_score(score for remaining off-diagonal entries);
    dash_score(score for any entry indexed by dash(es)).
    
    Output:a dictionary of dictionaries,its entries are indexed by pairs of 
    characters in alphabet + '-'.
    """
    scoring_matrix = {}
    alphabet_copy = set(list(alphabet))
    alphabet_copy.add('-')
    for char1 in alphabet_copy:
        scoring_matrix[char1] = {}
        for char2 in alphabet_copy:
            if char1 == '-' or char2 == '-':
                scoring_matrix[char1][char2] = dash_score
            elif char1 == char2:
                scoring_matrix[char1][char2] = diag_score
            else:
                scoring_matrix[char1][char2] = off_diag_score
    return scoring_matrix

def compute_alignment_matrix(seq_x, seq_y, scoring_matrix, global_flag):
    """
    这里用来做真正alignment的
    Computes alignment matrix using the method ComputeGlobalAlignmentScores
    
    Input:Two sequences: seq_x, seq_y; scoring_matrix; global_flag
    (global or local alignment)
    
    Output:An alignment matrix
    """
    alignment_matrix = [[0 for _ in range(len(seq_y)+1)] for _ in range(len(seq_x)+1)]
    
    for idx in range(1, len(seq_x) + 1):
        # alignment_matrix start with "-".so alignment_matrix[idx] = seq_x[idx-1]
        alignment_matrix[idx][0] = alignment_matrix[idx-1][0] + scoring_matrix[seq_x[idx-1]]["-"]
        if not global_flag and alignment_matrix[idx][0] < 0:
            alignment_matrix[idx][0] = 0
    
    for idx in range(1, len(seq_y) + 1):
        alignment_matrix[0][idx] = alignment_matrix[0][idx-1] + scoring_matrix["-"][seq_y[idx-1]]
        if not global_flag and alignment_matrix[0][idx] < 0:
            alignment_matrix[0][idx] = 0        
        
    for idx1 in range(1, len(seq_x) + 1):   
        for idx2 in range(1, len(seq_y) + 1):
            alignment_matrix[idx1][idx2] = max(alignment_matrix[idx1-1][idx2-1] + scoring_matrix[seq_x[idx1-1]][seq_y[idx2-1]],
                                              alignment_matrix[idx1-1][idx2] + scoring_matrix[seq_x[idx1-1]]["-"], 
                                              alignment_matrix[idx1][idx2-1] + scoring_matrix["-"][seq_y[idx2-1]])
            if not global_flag and alignment_matrix[idx1][idx2] < 0:
                alignment_matrix[idx1][idx2] = 0 
    
    return alignment_matrix

def compute_global_alignment(seq_x, seq_y, scoring_matrix, alignment_matrix):
    """
    只是trace back的过程
    Fuction use method ComputeAlignment
    
    Input:Two sequences: seq_x, seq_y; scoring_matrix; alignment_matrix
    
    Output:tuple(score,align_x,align_y),a global alignment of seq_x and seq_y and its score
    """
    len_x, len_y = len(seq_x), len(seq_y)
    align_x, align_y = "", ""
    while len_x != 0 and len_y != 0:
        if alignment_matrix[len_x][len_y] == alignment_matrix[len_x-1][len_y-1] + scoring_matrix[seq_x[len_x-1]][seq_y[len_y-1]]:
            align_x = seq_x[len_x-1] + align_x
            align_y = seq_y[len_y-1] + align_y
            len_x -= 1
            len_y -= 1
        else:
            if alignment_matrix[len_x][len_y] == alignment_matrix[len_x-1][len_y] + scoring_matrix[seq_x[len_x-1]]["-"]:
                align_x = seq_x[len_x-1] + align_x
                align_y = "-" + align_y
                len_x -= 1
            else:
                align_x = "-" + align_x
                align_y = seq_y[len_y-1] + align_y
                len_y -= 1
    while len_x != 0:
        align_x = seq_x[len_x-1] + align_x
        align_y = "-" + align_y
        len_x -= 1
    while len_y != 0:
        align_x = "-" + align_x
        align_y = seq_y[len_y-1] + align_y
        len_y -= 1        

    return tuple([alignment_matrix[-1][-1], align_x, align_y])

def compute_local_alignment(seq_x, seq_y, scoring_matrix, alignment_matrix):
    """
    只是trace back的过程
    compute an optimal local alignment
    
    Input:Two sequences: seq_x, seq_y; scoring_matrix; alignment_matrix
    
    Output:tuple(score,align_x,align_y),a global alignment of seq_x and seq_y and its score
    """
    max_score = -1
    row = -1
    col = -1
    for idx1 in range(len(seq_x)+1):
        for idx2 in range(len(seq_y)+1):
            if max_score < alignment_matrix[idx1][idx2]:
                max_score = alignment_matrix[idx1][idx2]
                row = idx1
                col = idx2
    
    len_x, len_y = row, col
    align_x, align_y = "", ""
    while len_x != 0 and len_y != 0 and alignment_matrix[len_x][len_y] != 0:
        if alignment_matrix[len_x][len_y] == alignment_matrix[len_x-1][len_y-1] + scoring_matrix[seq_x[len_x-1]][seq_y[len_y-1]]:
            align_x = seq_x[len_x-1] + align_x
            align_y = seq_y[len_y-1] + align_y
            len_x -= 1
            len_y -= 1
        else:
            if alignment_matrix[len_x][len_y] == alignment_matrix[len_x-1][len_y] + scoring_matrix[seq_x[len_x-1]]["-"]:
                align_x = seq_x[len_x-1] + align_x
                align_y = "-" + align_y
                len_x -= 1
            else:
                align_x = "-" + align_x
                align_y = seq_y[len_y-1] + align_y
                len_y -= 1
    while len_x != 0 and alignment_matrix[len_x][len_y] != 0:
        align_x = seq_x[len_x-1] + align_x
        align_y = "-" + align_y
        len_x -= 1
    while len_y != 0 and alignment_matrix[len_x][len_y] != 0:
        align_x = "-" + align_x
        align_y = seq_y[len_y-1] + align_y
        len_y -= 1        

    return tuple([max_score, align_x, align_y])