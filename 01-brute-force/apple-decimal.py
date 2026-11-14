
print("\nheyy\n")

weights = []
groupA = []
groupB = []
groupC = []
bestGroupA = []
bestGroupB = []
bestGroupC = []

n = int(input()) # 1 <=  n <=  20

for i in range(n):
    
    y = int(input()) # 1 <=  pi <=  10^9 ,, y <= 1000000000
    weights.append(y)

k = int(input())
  
minDiff = sum(weights)

for i in range(k ** n):  
    
    groupBsum = 0 
    groupAsum = 0
    groupCsum = 0

    groupA = []
    groupB = []
    groupC = []
    
    for j in range(len(weights)):
        
        # print("-  "+str(i)+" - "+str(j))
        
        if (((i // (k ** j)) % k) == 0 ):
        
        # k ** j  Calculates the power
        # //  Removes digits on the right
        # % k  Gets the digit we need
         
            groupAsum += weights[j]
            groupA.append(weights[j])
        
        elif (((i // (k ** j)) % k) == 1 ):
            
            
            groupBsum += weights[j]
            groupB.append(weights[j])
        
        else:
            
            groupCsum += weights[j]
            groupC.append(weights[j])
        
        
            
         
    diff = max(groupAsum, groupBsum, groupCsum) - min(groupAsum, groupBsum, groupCsum)
    
    if diff <= minDiff:
        minDiff = diff
        bestGroupA = []
        bestGroupB = []
        bestGroupC = []
        bestGroupA = groupA.copy()
        bestGroupB = groupB.copy()
        bestGroupC = groupC.copy()
   
          
print(bestGroupA)  
print(bestGroupB)      
print(bestGroupC) 
print(minDiff)         
            