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

def longest_oreo(s):
	max = s[0]
	for i in s:
		if i > max:
			max = i
	return max

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
    x = longest_oreo(s)
    end = time.perf_counter()
    print ('largest char = ', ord(x))  
    #print('x = ' + str(x))
    print('elapsed time = ' + str(end - start))

if __name__ == '__main__':
    main()

'''
SAMPLE OUTPUT:

with python 2 with time.time()

    $ python 1.py book.txt 100
    Loaded "book.txt" of length 675083
    n = 100
    largest value =  121
    elapsed time = 2.50339508057e-05

    $ python 1.py book.txt 675000
    Loaded "book.txt" of length 675083
    n = 675000
    largest char =  195
    elapsed time = 0.0809509754181

with python 3 with time_perf()

    $ python3 1.py book.txt 100
    Loaded "book.txt" of length 675056
    n = 100
    largest char =  121
    elapsed time = 1.876999158412218e-05

    $ python3 1.py book.txt 675000
    Loaded "book.txt" of length 675056
    n = 675000
    largest char =  246
    elapsed time = 0.04807819298002869

'''

# ================= performance measurement ======================




# === compare results w/ the efficiency class of the algorithm ===


