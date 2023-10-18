haystack = input("give me the haystack ")  #example haystack = "hellohe"
needle = input("give me the needle ")      #example needle = "he"  

list(haystack)
list(needle)

index_value = []
i = 0
while i < len(haystack):
    dummy = 0
    if haystack[i] == needle[0]:
        for k in range(i,len(needle)+i):
            if haystack[k] == needle[k-i]:
                dummy +=1
        if dummy == len(needle):
            index_value.append(i)
    i += 1

print(index_value)
x = len(index_value)
print(f"The word '{needle}' is inside the word '{haystack}' {x} times at the indexes {index_value}")