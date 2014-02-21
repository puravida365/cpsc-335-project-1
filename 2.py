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
            if s[i] == s[x]:
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


'''

# ================= performance measurement ======================




# === compare results w/ the efficiency class of the algorithm ===


