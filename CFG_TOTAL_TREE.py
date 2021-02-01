Alphabet = input("Please Input  Alphabet (ε) with seperat by comma --->  ")
Splitted_Alphabet = Alphabet.split(',')


S = input("PLEASE INPUT S CHARACTER AND DON'T KEEP IN MIND THAT PLEASE USE '|',WHILE SEPARATING CHARACTER '|'--->")
S = S.split('|')

X= input("Plase INPUT REFERENCESS OF X TO REPRESENTING TO X WITH SEPERATE BY '|'")
X=X.split('|') 

print("ε = {}= ".format(Splitted_Alphabet))
print( "CFG; S _---> {}".format(S))
print("X ---> {}".format(X)) 

with_X=[]
repeat = []
result = []
detail = {}

for i in range(0, len(S)):
    detail[S[i]] = 0 
    if  S[i].count('X') == 0 :
        result.append(S[i])
    else:
        with_X.append(S[i])
        while len(with_X) != 0:
            new_temp = with_X.pop()
            for j in range(0, len(X)):
                Xtemp = new_temp.replace('X', X[j],1)
                detail[S[i]] +=1
                print(Xtemp)
                if Xtemp.count('X') == 0:
                    if detail[S[i]] <= 2:
                        result.append(Xtemp)
                    else:
                        result.append(Xtemp)
                        repeat.append(Xtemp)
                else:
                    with_X.append(Xtemp)
print("Detail : {}".format(detail))
print("Repeat : {}".format(repeat))
print("Result : {}".format(result))