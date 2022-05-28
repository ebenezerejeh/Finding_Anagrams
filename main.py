# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True



def find_anagram(word, anagram): 
        #using the sorted function
    sorted_word = sorted(word)
    sorted_anagram = sorted(anagram)

        #comparing the sorted words
    if sorted_word == sorted_anagram:
        return True
    else:
        return False

    #An example
print(find_anagram("heart","earth"))
print(find_anagram("bad","dad"))






    

