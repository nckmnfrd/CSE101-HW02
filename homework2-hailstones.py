#Nicholas Manfredi
#110207186
#CSE 101
#Lab Section 8
#Homework 2


#Part 1 A
def hail(n):
    print(n)
    while n != 1:
        if n %2 == 0:
            n = n//2
        else:
            n = (n*3)+1
        print(n)

#Part 1 B
def hail_length(n):
    length = 1   
    while n != 1:
        if n %2 == 0:
            n = n//2
        else:
            n = (n*3)+1
        length = length + 1

    return length

#Part 1 C
def siblings(length,max_val):
    
    for i in range(1,max_val+1):
        if hail_length(i) == length:
            print(i)

#Part 1 D
print("hail(6)")
hail(6)
print("hail_length(7)")
print (hail_length(7))

print("siblings(10,100)")
siblings(10,100)

            
            
            
