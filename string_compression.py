def solution(s):
    result = [] # save compressed string's length
    if len(s)==1: # if string's length is 1 (= a single character)
        return 1 # no compress string
    for i in range(1, (len(s)//2)+1): # String's half length
        compressed_string = ''
        cnt = 1 # count the number of compressed strings
        standard = s[:i] # standard for compressed string

        for j in range(i, len(s), i):
            if standard == s[j:i+j]: # compare standard and subsequent string
                cnt+=1
            else: # two strings do not match each other
                if cnt!=1: # (= There are duplicate string)
                    compressed_string = compressed_string + str(cnt) + standard # append compression count and string
                else: # no duplicate string
                    compressed_string = compressed_string + standard # append just standard string
                standard = s[j:j+i] # change standard to subsequent string
                cnt = 1 # reset cnt
        if cnt != 1: 
            compressed_string = compressed_string + str(cnt) + standard # add compression count and compressed string
        else:
            compressed_string = compressed_string + standard # add compressed string
                
        result.append(len(compressed_string)) # append total length
    return min(result) # return minimum length