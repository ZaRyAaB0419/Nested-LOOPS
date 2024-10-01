# Input a number
num = int(input("Enter the number: "))
t = num
numLen = 0

while t > 0:
    numLen += 1
    t = t // 10  

if numLen >= 4:
    numLen //= 2
    chk = 0
    midOne = midTwo = 0  

    while num > 0:
        rem = num % 10  
        num //= 10  

        if chk == numLen:
            midOne = rem
        elif chk == (numLen - 1):
            midTwo = rem
        
        chk += 1

    prod = midOne * midTwo
 
    print(f"\nProduct of Mid digits ({midOne} * {midTwo}) = {prod}")
else:
    print("The number must have at least 4 digits.")