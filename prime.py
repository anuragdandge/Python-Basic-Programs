a = 11
flag = False
if a > 1:
    for i in range (2,a):
          if (a%i) == 0 :
            flag = True
            break

if flag:
    print(a,"is not Prima")
else:print(a,"is  Prime")
