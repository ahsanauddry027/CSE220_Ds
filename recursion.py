a = [10,20,30]
def resursion(a,i,sum):
    if i>=0 and i<len(a):
        sum += a[i]
        return resursion(a,i+1)
    
    return sum
print(resursion(a,0,0))

def reSum(a,i,sum):
    if i>=0 and i<len(a):
        sum+=a[i]
        return reSum(a,i+1,sum)

    return sum
        
print(reSum(a,0,0))
# def reSum(a,i):
#     if i>=0 and i<len(a):
#         print(hex(id(a[i])),i)
#         print(reSum(a,i+1))
#         print(i,"hi")
#         return hex(id(a[i])),i
       
#     return 1

# print(reSum(a,0))
    
