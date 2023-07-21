
def SumTuples(tuple1,tuple2):
  sum=[]
  for i in range(len(tuple1)): #because same size is doesn't matter which len we use
    sum.append(tuple1[i]+tuple2[i])
  return tuple(sum)

def JSONtoDic():
  object_list=[]
  path="objects.json"
  with open(path,"r") as file:
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
  


def dicToJSON(dic,empty):

  if(empty):
    strr="[\n\t{\n\t\t"
  else:
    strr="\t\n\t{\n\t\t"

  length=0
  for i in dic:
    if(length!=len(dic)-1):
      if(type(dic[i])==list):
        strr+='"'+i+'"'+" : "+str(dic[i])+","+"\n\t\t"  
      else:
        strr+='"'+i+'"'+" : "+'"'+str(dic[i])+'"'+","+"\n\t\t"
    else:
      if(type(dic[i])==list):
        strr+='"'+i+'"'+" : "+'"'+str(dic[i])+'"'+""  
      else:
        strr+='"'+i+'"'+" : "+'"'+str(dic[i])+'"'+""
    length+=1
  
  strr+="\n\t}"+"\n]"  
  


  return strr

def is_empty(path):
  with open(path, 'r') as file:
      content = file.read()
      if content.strip() and content.strip()[-1] == ']':
          delete_last(path, content)
  return not content.strip()

def delete_last(path, content):
    with open(path, 'w') as file:
        file.write(content[:-1])




def main():
  choice=0
  while(choice!=4):
    print("enter the function you want\n","1.Sum Tuples\n","2.Export JSON\n","3.Import JSON\n","4.EXIT")
    choice=int(input())
    if(choice==1):
      size=int(input("enter the size of the tuples"))
      lst=[]
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
    if (choice==3):
      elements=JSONtoDic()
      for i in elements:
        print(i)



    if(choice==2):
      elements=int(input("enter the number of elements of the object"))
      dic={}
      path="writeJson.json"
      print("fill the dictinary (key/value)")
      for i in range(elements):
        key=input("key:")
        value=input("value:")
        dic[key]=value

      flag=is_empty(path)
      var =dicToJSON(dic,flag)
      
      with open (path,'a') as file:
        if(not flag):
          file.write(','+var)
        else:
          file.write(var)

      
      print(dicToJSON(dic,flag))
      

        
    
                    
main()

# complexity:
#1)1/6N+8000N^3+24 = N^3
#2)1/6N^3 = N^3
#3)1/6N! +200N^4 = N!
#4)NlogN +1000 = NlogN
#5)logN +N = N
#6)1⁄2N(N-1) = N^2 (because 1\2 N^2 - 1/2 N)
#7)N^2+220NlogN^2+3N+9000 = N^2
#8)N!+3^N+2^N+N^3+N^2 = n!

#how I did them
#from fastest to slowest

#Log N	
# Log^2 
# N
# NlogN
# N^2			
# N^3			
# 2^N			
# N!
