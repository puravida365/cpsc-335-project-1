# ===============================================================
# CPSC 335 - Spring 2014
# PROJECT 1 - QUESTION 2

# ===============================================================
# The longest oreo problem is:
# input: a string s of length n > 0
# output: the longest non-empty substring u of s such that the
#         first and last characters of u are identical
# size: n
# ===============================================================


# ================ Design Algorithm =============================



# ============= Describe algorithm using pseudocode =============
'''
read data from file
set temp value to first letter of string

'''

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
			
def main():
    if len(sys.argv) != 3:
        print('error: you must supply exactly two arguments\n\n' +
              'usage: python <Python source code file> <text file> <n>')
        sys.exit(1)

    filename = sys.argv[1]
    n = int(sys.argv[2])

    entire_file = open(filename).read()
    print('Loaded "' + filename + '" of length ' + str(len(entire_file))) 
    print ('n =', n)

    # take only the first n characters of entire_file
    s = entire_file[:n]
    assert(len(s) == n)

    start = time.perf_counter()
    x = max_char(s)
    y = longest_oreo(s)
    end = time.perf_counter()
    print ('largest char = ', ord(x))  
    print ('elapsed time = ' + str(end - start))
    print ('longest oreo = [', y, ']')

if __name__ == '__main__':
    main()

'''
SAMPLE OUTPUT:

$ python3 2.py book.txt 100
Loaded "book.txt" of length 675056
n = 100
largest char =  121
elapsed time = 0.0010750539950095117
longest oreo = [ e Project Gutenberg EBook of A short history of Rhode Island, by 
George Washington Greene

This e ]
$ 

===========================================================

$ python3 2.py book.txt 10
Loaded "book.txt" of length 675056
n = 10
largest char =  114
elapsed time = 3.6934041418135166e-05
longest oreo = [ e Proje ]
$ 

===========================================================

$ python3 2.py book.txt 500
Loaded "book.txt" of length 675056
n = 500
largest char =  121
elapsed time = 0.02722752100089565
longest oreo = [ The Project Gutenberg EBook of A short history of Rhode Island, by 
George Washington Greene

This eBook is for the use of anyone anywhere at no cost and with
almost no restrictions whatsoever.  You may copy it, give it away or
re-use it under the terms of the Project Gutenberg License included
with this eBook or online at www.gutenberg.org


Title: A short history of Rhode Island

Author: George Washington Greene

Release Date: February 18, 2014 [EBook #44955]

Language: English


*** START ]
$ 



'''

# ================= performance measurement ======================




# === compare results w/ the efficiency class of the algorithm ===


