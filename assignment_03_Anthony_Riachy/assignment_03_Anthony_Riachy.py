
def SumTuples(tuple1,tuple2):
  sum=[]
  for i in range(len(tuple1)): #because same size is doesn't matter which len we use
    sum.append(tuple1[i]+tuple2[i])
  return tuple(sum)

def JSONtoDic():
  object_list=[]
  with open("objects.json","r") as file:
    json=file.read()

  json =json.strip().strip("[ ]")
  json=json.split('{')

  for obj in json:
    if obj:
      obj=obj.strip().strip(',}')
      obj_dic={}
      obj=obj.split(',')
      for line in obj:
        if(":" in line):
          line=line.split(':')
          obj_dic[line[0].strip().strip('"')]=line[1].strip().strip('"')
        #end of line
      if(obj_dic):
        object_list.append(obj_dic)

        

      #end of object
      

  return object_list
  

    
  

  
  


def main():
  lst=[]
  print("enter the function you want\n","1.Sum Tuples\n","2.Export JSON\n","3.Import JSON","4.EXIT")
  choice=int(input())
  if(choice==1):
    size=int(input("enter the size of the tuples"))
    
    #filling the first tuple
    for i in range(size): 
      lst.append(int(input("fill the first tuples")))
    tuple1=tuple(lst)
    lst.clear()
    
    print("---------------")
    
    #filling the second tuple
    for i in range(size): 
      lst.append(int(input("fill the second tuples")))
    tuple2=tuple(lst)
    
    del lst
    print(SumTuples(tuple1,tuple2))
  if (choice==2):
    print(JSONtoDic())
  
    
      
  
                   
main()