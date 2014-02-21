# ===============================================================
# CPSC 335 - Spring 2014
# PROJECT 1 - QUESTION 3

# ===============================================================
# Given:
# 
# Input: a string s of length n > 0
# output: the longest nonempty substring u of s such that u 
#         appears more than once in s
# size: n
#
# ===============================================================


# ================ Design Algorithm =============================



# ============= Describe algorithm using pseudocode =============


# ================ mathematical analysis ========================


# ================ python implementation ========================

# define variable

import sys
import time

def max_char(s):
    max = s[0]
    for i in s:
        if i > max:
            max = i
    return max

def longest_oreo(s):
    mainLength = 0
    startL = 0
    endL = 0
    for i in range(0,len(s)):
        for x in range(i+1,len(s)):
            if s[i] == s[x] and s[x] != ' ':
                length = (x-i) + 1
                if length > mainLength: 
                    mainLength = length
                    startL = i
                    endL = x 
                    
    oreoString = s[startL:endL+1]
    return(oreoString)

def duplicate_list(g):
    CurrentSize = 0
    LargestSize = 0
    DuplicateValue = " "
  

    for i in range(0,len(g)):
        for x in range(i+1,len(g)):        
            if g[i] == g[x] and g[x] != ' ':
                CurrentSize = len(g[i])
                if CurrentSize > LargestSize:
                    DuplicateValue = g[i]
                    LargestSize = CurrentSize

    return DuplicateValue         


def main():
    if len(sys.argv) != 3:
        print('error: you must supply exactly two arguments\n\n' +
              'usage: python <Python source code file> <text file> <n>')
        sys.exit(1)

    filename = sys.argv[1]
    n = int(sys.argv[2])
    m = n
    entire_file = open(filename).read()
    print('Loaded "' + filename + '" of length ' + str(len(entire_file))) 
    print ('n =', n)

    # take only the first n characters of entire_file
    s = entire_file[:n]
    g = entire_file[:m].split(" ")

    assert(len(s) == n)

    start1 = time.perf_counter()
    x = max_char(s)
    end1 = time.perf_counter()
    start2 = time.perf_counter()
    y = longest_oreo(s)
    end2 = time.perf_counter()
    start3 = time.perf_counter()
    z = duplicate_list(g)
    end3 = time.perf_counter()
    
    print ('largest char = ', ord(x))  
    print ('elapsed time = ' + str(end1 - start1))
    print ('longest oreo = [', y, ']')
    print ('elapsed time = ' + str(end2 - start2))
    print ('longest repeated substring = [', z, ']')
    print ('elapsed time = ' + str(end3 - start3))

if __name__ == '__main__':
    main()

'''
SAMPLE OUTPUT:

Loaded "book.txt" of length 675056
n = 100
largest char =  121
elapsed time = 2.1660001948475838e-05
longest oreo = [ e Project Gutenberg EBook of A short history of Rhode Island, by 
George Washington Greene

This e ]
elapsed time = 0.0013798469444736838
longest repeated substring = [ of ]
elapsed time = 4.416698357090354e-05

================================================================


Loaded "book.txt" of length 675056
n = 100
largest char =  121
elapsed time = 2.1660001948475838e-05
longest oreo = [ e Project Gutenberg EBook of A short history of Rhode Island, by 
George Washington Greene

This e ]
elapsed time = 0.0013798469444736838
longest repeated substring = [ of ]
elapsed time = 4.416698357090354e-05
$ python3 3.py book.txt 2000
Loaded "book.txt" of length 675056
n = 2000
largest char =  125
elapsed time = 0.00018807995365932584
longest oreo = [ Gutenberg EBook of A short history of Rhode Island, by 
George Washington Greene

This eBook is for the use of anyone anywhere at no cost and with
almost no restrictions whatsoever.  You may copy it, give it away or
re-use it under the terms of the Project Gutenberg License included
with this eBook or online at www.gutenberg.org


Title: A short history of Rhode Island

Author: George Washington Greene

Release Date: February 18, 2014 [EBook #44955]

Language: English


*** START OF THIS PROJECT GUTENBERG EBOOK A SHORT HISTORY OF RHODE ISLAND ***




Produced by KD Weeks, Charlene Taylor and the Online
Distributed Proofreading Team at http://www.pgdp.net (This
file was produced from images generously made available
by The Internet Archive/American Libraries.)





Transcriber's Note

This version of the text is unable to reproduce certain typographic
features. Italics are delimited with the '_' character as _italic_.
Superscripts are used in certain period quotations (e.g., y^e), are
represents, as shown, with the carat character. Should more than one
character be superscripted, they are enclosed in brackets (e.g.,
Y^{or}). The 'oe' ligature appears only in the words 'manoeuvring',
and is rendered as separate characters. Words printed using small
capitals are shifted to all upper-case.

Footnotes have been relocated to the end of paragraph breaks or tables,
and are assigned sequential letters.

Please consult the notes at the end of this text for a more detailed
discussion of any other issues that were encountered during its
preparation.


[Illustration: STATUE OF ROGER WILLIAMS.]




                                   A
                             SHORT HISTORY
                                   OF
                             RHODE ISLAND,

                                   BY

                    GEORGE WASHINGTON GREENE, LL.D.,

       LATE NON-RESIDENT PROFESSOR OF AMERICAN HISTORY IN CORNELL
            UNIVERSITY; AUTHOR OF "THE LIFE OF MAJOR-G ]
elapsed time = 0.41419019701424986
longest repeated substring = [ Washington ]
elapsed time = 0.02109081100206822


================================================================




'''

# ================= performance measurement ======================




# === compare results w/ the efficiency class of the algorithm ===


