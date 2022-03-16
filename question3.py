user_input = input().split(" ")
mode = int(user_input[0])
number = user_input[1]



# do not change above
# you have both mode and number

if mode == 0:
    binary= ""
    number = int(number)
    n = 99
    while n !=0:
        n -=  1
        if number>=(2**n):
            number = number - (2**n)
            binary= binary +"1"
        else:
            binary = binary + "0"


    starting_index=binary.find("1") 
    print(binary[starting_index:])

    
    
    

    
elif mode == 1:
    number = str(number)
    number=number[::-1]
    decimal = 0
    for i in range(len(number)):
        decimal =decimal + (int(number[i])*(2**i))
    print(decimal)
# do not forget to print the result
# do your work below


####decimal to binary####

####binary to decimal####




    
    
    
    
    

