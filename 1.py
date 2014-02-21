# ===============================================================
# CPSC 335 - Spring 2014
# PROJECT 1 - QUESTION 1

# ===============================================================
# Given:
# 
# Input: a string s of length n > 0
# output: the character c in s with the greatest integer value
# size: n
#
# ===============================================================


# ================ Design Algorithm =============================



# ============= Describe algorithm using pseudocode =============
'''
read data from file
set max value to first character of string
loop through string of characters
    compare all characters to max value
    if character is > max
        max = new character 
print results
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
    end = time.perf_counter()
    print ('largest char = ', ord(x))  
    #print('x = ' + str(x))
    print('elapsed time = ' + str(end - start))

if __name__ == '__main__':
    main()

'''
SAMPLE OUTPUT:

=================================================================

Loaded "book.txt" of length 675056
n = 100
largest char =  121
elapsed time = 1.9369006622582674e-05

=================================================================

Loaded "book.txt" of length 675056
n = 2000
largest char =  125
elapsed time = 0.00015600200276821852

=================================================================

Loaded "book.txt" of length 675056
n = 50000
largest char =  246
elapsed time = 0.003546701977029443

=================================================================

Loaded "book.txt" of length 675056
n = 200000
largest char =  246
elapsed time = 0.014268580009229481

=================================================================

Loaded "book.txt" of length 675056
n = 500000
largest char =  246
elapsed time = 0.03547984198667109

'''

# ================= performance measurement ======================




# === compare results w/ the efficiency class of the algorithm ===


