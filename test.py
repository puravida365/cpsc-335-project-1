def oreo(s):
    for i in range(0,len(s)):
        for x in range(1,len(s)):
            if s[i] == s[x]:
                length = (x-i) + 1
                if length > mainLength: 
                    mainLength = length
                    start = i
                    end = x 
                    
        x=i+1