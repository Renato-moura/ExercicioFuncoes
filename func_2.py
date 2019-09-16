#2 Tem 33: Faça uma função que retorne True se, dada uma lista de inteiros, houver em alguma posição da lista um 3 do lado de outro 3.

def tem_33(func):
  a = func[0]
  b = func[1]
  #print(a,b)
  if a == 3 and b == 3:
    #print("verdade_t1")
    val = 1
  else:
    #print(a,b)
    for i in range(2,len(func)):
      a = b
      b = func[i]
      #print(a,b)
      if a == 3 and b == 3:
        #print("verdade_t2")
        val = 1
      else:
        #print("mentira") 
        val = 0
  if val == 1:
    return print("True")
  else:
    return print("False")



tem_33([1,3,3]) #--> True
tem_33([1,3,1,3]) #--> False
tem_33([3,1,3]) #--> False