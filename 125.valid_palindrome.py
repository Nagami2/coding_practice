'''A phrase is a palindrome if, after converting all 
uppercase letters into lowercase letters and 
removing all non-alphanumeric characters, it reads the same forward and backward'''
# wrong initiation? first, last = s[0], s[-1]

r,l = 0, len(s)-1

while l<r:
    while l<r and not s[l].isalnum():
        l +=1
    while l<r and not s[r].isalnum():
        r -=1
    if l<r and s[l].lower() != s[r].lower():
        return False
    else:
        l +=1
        r -=1
        continue
    
return True


