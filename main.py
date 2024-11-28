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









def single(nums):
    result=0
    for num in nums:
        result^=num
    return result

print(single([1,2,3,2,1]))