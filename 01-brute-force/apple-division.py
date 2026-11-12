
print("\nheyy\n")

weights = []
groupA = []
groupB = []
bestGroupA = []
bestGroupB = []

n = int(input()) # 1 <=  n <=  20

for i in range(n):
    
    y = int(input()) # 1 <=  pi <=  10^9 ,, y <= 1000000000
    weights.append(y)
    
min = sum(weights)

for i in range(2 ** n):  
    
    groupBsum = 0 
    groupAsum = 0
    groupA = []
    groupB = []
    
    for j in range(len(weights)):
        
        print("-  "+str(i)+" - "+str(j))
        
        if (((i >> j) & 1) == 0 ):
            
            groupAsum += weights[j]
            groupA.append(weights[j])
        else:
            groupBsum += weights[j]
            groupB.append(weights[j])
         
    diff = abs(groupAsum - groupBsum)
    
    if diff <= min:
        min = diff
        bestGroupA = []
        bestGroupB = []
        bestGroupA = groupA.copy()
        bestGroupB = groupB.copy()
        
   
          
print(bestGroupA)  
print(bestGroupB)      
print(min)         
            