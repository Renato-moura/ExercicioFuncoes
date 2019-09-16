1 Espião: Escreva uma função que receba uma lista de inteiros e retorne True se contém um 007 em ordem mesmo que não contínuo.
def espiao(a):
  
  d = {"p1":0,"p2":0,"p3":0}

  for i in range(0,len(a)):
    if a[i] == 0:
      d["p1"] = d["p2"]
      d["p2"]=i  

    if a[i] == 7:
      d["p3"]=i   
  #print("d",d)
   
  if d["p1"] < d["p2"] and d["p2"] < d["p3"]:
    return True
  else:
    return False

def resultado(a):
  if a == True:
    print("sucesso")
  else:
    print("fracasso")

a = espiao([1,2,4,0,0,7,5]) 
b = espiao([1,0,2,4,0,5,7]) 
c = espiao([1,7,2,4,0,5,0])


resultado(a)
resultado(b)
resultado(c)
