haystack = input("give me the haystack ")  #example haystack = "hellohe"
needle = input("give me the needle ")      #example needle = "he"  

list(haystack)
list(needle)

index_value = []
i = 0
while i < len(haystack):     
    dummy = 0
    if haystack[i] == needle[0]:                #if we find that a value from the haystack is equal to a value from the needle we start a loop search
        for k in range(i,len(needle)+i):        # example, if i = 5, then the loop will search from 5 to 5+2=7 at the haystack and on the needle it will search 5-5=0 to 7-5=2, which is the length of the needle
            if haystack[k] == needle[k-i]:
                dummy +=1
        if dummy == len(needle):
            index_value.append(i)               #here I append the index value "i" where equality started
    i += 1

print(index_value)
x = len(index_value)
print(f"The word '{needle}' is inside the word '{haystack}' {x} times at the indexes {index_value}")