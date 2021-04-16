


tup = ("anurag","omkar","dishant","jayprasad","vishal")
print("1 : ",tup , "\n" ,"Data Type = ",type(tup)," \n We cannot perform any operation on Tuple \n \n ")


li = ["anurag","omkar","dishant","jayprasad","vishal"]
print("2 : ",li ,"\n","Data Type = ",type(li),"\n We can perform various operation on LIST like Insertion, Sorting , Deletion etc. \n ",)

li.reverse()
print("Reversed List ",li , "\n")

li.sort()
print("Sorted List " ,li, "\n ")

li.insert(5,"Sameer")
print("Insertion Operation ", li, "\n ")

li.pop(5)
print("Deletion(pop) Operation ", li, "\n \n ")


dir = {"anurag":"Motorola","omkar":"Samsung","jay":"Redmi","dishant":"Realme","vishal":"Xiaomi"}
print("\n 3 : ",dir,"\n Data Type = ",type(dir), " \n ")
print(" Here , \n we are printing Anurag's Mobile by Key i.e,'anurag' = " , dir["anurag"],"")








