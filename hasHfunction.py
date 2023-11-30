class Node:
    
    def __init__(self,key,elem,next=None):
        self.key,self.elem,self.next=key,elem,next
    
class HashMap:
    
    def __init__(self,size):
        self.ht = [None]*size
        
    def insertElem(self,s):
        if self.searchElem(s)=="Found":
            print(f"This element already exixts.")
            return
        
        hash_idx = self.hashFunction(s[0])
        pair = Node(s[0],s[1])
        
        if self.ht[hash_idx] == None:
            self.ht[hash_idx] = pair
        else:
            pair.next = self.ht[hash_idx]
            self.ht[hash_idx] = pair
            
    def insertFromArray(self,arr):
        
        for elem in arr:
            self.insertElem(elem)
            
    def printHashMap(self):
        idx=0
        for elem in self.ht:
            head = elem
            print(idx,":",end=" ")
            
            while head !=None:
                print(f"( Key: {head.key} || Value: {head.elem} )",end="-> ")
                head = head.next
            print("None")
            idx+=1
            
    def hashFunction(self, s):
        n = s
        num = 0
        i =1
        if len(s)%2!=0:
            n+="N"
            
        while i<len(n):
            main = n[i-1]+n[i]
            stri =""
            for nums in main:
                stri+= str(ord(nums))
            num+=int(stri)
            i+=2
            
        index = num%5
        return index


  #Do by yourself
    def searchElem(self, s):
        for i in self.ht:
            head = i
            while head!=None:
                if s[0]== head.key:
                    return "Found"
                head = head.next
        return None
arr = [('Colt', 360), ('Cordelius', 730), ('Shelly', 300), ('Doug', 1200), ('Emz', 520), ('Bo', 580)]
ht = HashMap(5)
ht.insertFromArray(arr)
ht.printHashMap()
        
    
    
        
        