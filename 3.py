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



'''

# ================= performance measurement ======================




# === compare results w/ the efficiency class of the algorithm ===


