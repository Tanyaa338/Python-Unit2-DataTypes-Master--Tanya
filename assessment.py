""" def spaces(N, y, t):
    y = ("C", "C", ".", ".", "C")
    t = (".", "C", "C", ".", ".")
    for i in range(N):
        y[i] and t[i]
    if y[i] == "c" and t[i] == "c":
        print("+1")
    else: 
        print("+0") """

#def spaces(n, y, t):
#    occupied = 0
#    for i in range(n):
#        if y[i] == "C" and t[i]:
#            occupied+=1
#        return occupied
#
#print(spaces(6, "CC..CC", ".CC..C"))



""" 
occupied = occupied + 1










for i in range(len(y)) """

def wizard(owner, N, duels):
    #print(duels[0][0])
    for i in range(N):
      if duels[i][1] == owner:
            owner = duels[i][0]
    print(owner) 

wizard("A",3,["BA","CB","DA"])