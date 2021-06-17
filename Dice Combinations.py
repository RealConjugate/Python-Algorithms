# Finds the number of, and generates, the possible combinations when an s-sided die is rolled n times.

def Generate(n,s): # n rolls, s-sided die
    sequences = [([1] * n)]
    class1 = [0]*(s-1)
    class1.insert(0,n)
    classes = [class1]
    
    for i in range(1,s**n):
        base = [1] * (MaxP((s**n)-1,s)-MaxP(i,s))
        num = i
        for j in range(0,MaxP(i,s)): # starts at 1, not 0
            p = MaxP(i,s)-j-1
            base.append(int(num//(s**p))+1)
            num = num%(s**p)
        if not GetClass(base,n,s) in classes:    
            sequences.append(base)
            classes.append(GetClass(base,n,s))
            
    print("There are " + str(len(sequences)) + " combinations.")
    for item in sequences:
        print(item)

def MaxP(k,base): # k>=1
    p = 0
    while not (base**(p+1) > k and base**p <= k):
        p+=1
    return p+1
        
def GetClass(seq,n,s):
    classList = []
    for i in range(1,s+1):
        k = 0
        for j in range(0,n):
            if seq[j] == i:
                k+=1
        classList.append(k)
    return classList
