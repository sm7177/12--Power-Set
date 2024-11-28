# def pps(set,setsize):
#     pss=2**setsize
#     outer=0
#     inner=0
#     for outer in range(0,pss):
#         for inner in range(0,setsize):
#             if ((outer &(1<<inner))>0):
#                 print(set[inner],end="")
#         print("")
        
# size=int(input("Enter arrray size:"))

# set=[]

# for i in range(0,size):
#     n=int(input("Enter element:"))
#     set.append(n)
    
# pps(set,len(set))









# def single(nums):
#     result=0
#     for num in nums:
#         result^=num
#     return result

# print(single([1,2,3,2,1]))









# def flip (num1,num2):
#     flip=0
#     while(num1>0 or num2>0):
#         t1=num1 & 1
#         t2=num2 & 1
#         if t1!=t2:
#             flip+=1
#         num1>>=1
#         num2>>=1
#     return flip

# num1=int(input("Enter num1:"))
# num2=int(input("Enter num2:"))

# print("Number of flips required:",flip(num1,num2))






def add(a,b):
    while b!=0:
        carry=a & b
        a=a ^ b
        b=carry << 1
    return a

print(add(10, 5))