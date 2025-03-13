str= input ("Enter a String: ")
dict = {}
for n in str :
    if n in dict:
        dict[n] += 1
    else:
        dict[n] = 1
print(dict)
"tran nguyen viet duc"