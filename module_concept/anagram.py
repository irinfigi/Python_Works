def anagramCheck(str1,str2):
    if(sorted(str1)==sorted(str2)):
        return True
    else:
        return False
str1=input("Enter string1:")
str2=input("Enter string2:")
if anagramCheck(str1,str2):
    print("Anagram")
else:
    print("Not an anagram")