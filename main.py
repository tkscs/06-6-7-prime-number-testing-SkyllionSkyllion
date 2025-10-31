testnumber=13
prime = True

for i in range (2, testnumber):
    if testnumber%(i) == 0:
        prime = False
        break

if prime == True:
    print("PRIME")
else:
    print("NOT PRIME")
        