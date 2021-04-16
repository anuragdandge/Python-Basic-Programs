def pat(a):
  for i in range(0,a):
    for j in range(0,i+1):
        print(" * ",end= " ")
    print("\r")

a = 5
pat(a)

