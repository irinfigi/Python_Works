string1=input("Enter the string:")
non_repeating_chars=[]
for chars in string1:
    if string1.count(chars)==1:
        non_repeating_chars.append(chars)
print("Non repeating characters",non_repeating_chars)
