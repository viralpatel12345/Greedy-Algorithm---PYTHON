#DSA-Exer-24

def make_change(denomination_list, amount):
    '''
    Implement the Greedy approach to make the change for the amount using the currencies in
    the denomination list.
    
    The function should return the total number of notes needed to make the change. 
    If change cannot be obtained for the given amount, then return -1.
    Return 1 if the amount is equal to one of the currencies available in the denomination list.  '''
    
    s=0
    count=0
    l=[]
    if amount in denomination_list :
        return 1
    elif amount<min(denomination_list) :
        return -1
    else :    
      while s != amount and len(denomination_list)!=0 :
        if (s+max(denomination_list))>amount :
           denomination_list.remove(max(denomination_list))
        else :
           l+=[max(denomination_list)] 
           s+=max(denomination_list)
           count+=1
    print("Amount = ",amount)
    print("Earned = ",s)
    print(l)
    print("Loss = ",(amount-s))    
        
    return count
#Pass different values to the function and test your program
amount= 46
denomination_list = [25,15,10,8,5,1]

count=make_change(denomination_list, amount)
print(count)