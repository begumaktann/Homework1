
# taking input
lst = [float(item) for item in input().split()]
# do not change the above



#### finding the length ####
length =0  # initial length of the list
for num in lst:
    length += 1  # adding 1 for every element in the list


#### find the minimum ####
min = lst[0]


for i in range(1,length):
    if lst[i]< min:
        min = lst[i]
        
index_min= lst.index(min)



#### find the max ####

max = lst[0]


for i in range(1,length):
    if lst[i]>max:
        max = lst[i]

index_max= lst.index(max)


#### find the summation ####

sum = 0

for num in lst:
    sum = sum + num
    


#### find the mean ####

mean = sum/length

#### find the variance ####
variance = 0
for num in lst:
    variance = variance + (((num - mean)**2)/length)
    
###formatting###
max = ("%.5f" %max)
min = ("%.5f" %min)
sum = ("%.5f" %sum)
mean= ("%.5f" %mean)
variance = ("%.5f" %variance)

# print the desired result
print(f"{length} {min} {index_min} {max} {index_max} {sum} {mean} {variance}")

