# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

def find_anagram(word, anagram):
    
    #Unequal Length strings cannot be anagrams
    if len(word) != len(anagram):
        return False
    
    #sort the first string
    a = sorted(word)
    #sort the second string
    b = sorted(anagram)
    
    #check if both the strings are same
    if a == b:
        return True
    else:
        return False
    
print(find_anagram("below","elbow"))

