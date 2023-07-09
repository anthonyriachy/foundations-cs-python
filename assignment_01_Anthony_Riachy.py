##################################################################################################
# ex 1

def factorial(number):
    if(number==0):
      return 1
      
    return number*factorial(number-1)


#######################################################################################################
#ex 2
def divisors(number):
  number=abs(number)#to handle negative numbers

  my_list=[]
  div=1
  while(div<=number):#starting from one till the number
    if(number%div==0):
      my_list.append(div)
    div+=1
    #if we want same output as in the ex we do this
  #if(len(my_list)==2 and 1 in my_list and number in my_list):
   # return "[]"
  return my_list

#############################################github change test#####################################################
#ex 3
def reverseString(str):
  pos=len(str)-1#from the end of the string to the start
  new_str=''
  while(pos>=0):
    new_str+=str[pos]
    pos-=1
  return new_str

      
##################################################################################################
#ex 4

def evenNumbers(my_list):
  new_list=[]
  for num in my_list:
    if num % 2==0:
      new_list.append(num)
  return new_list

##################################################################################################
def passwordValidator(password):
  flag=False
  upper=False
  lower=False
  digit=False
  special=['#','?','!','$']
  specialChar=False
  
  if(len(password)>=8):
    for i in password:
      if(i.isupper()):
        upper=True
      if(i.islower()):
        lower=True  
      if(i.isdigit()):
        digit=True
      if(i in special):
        specialChar=True
    flag=upper * lower * digit * specialChar #because true =1 false=0, we can use 'and'
    
  else:
    flag =False
  
  if(flag):
    print ("strong password")
  else:
    print("weak password")
##################################################################################################
#bonus question

def IPv4Validator(ip):
  numbers=ip.split('.')

  if(len(numbers)!=4):
    return False
  
  for num in numbers:
    if(num==""):
      return False
    if(int(num)<0 or int(num)>255):
      return False
    if(int(num[0])==0 and len(num)>1):
      return False
  
      
  return True

  











def main():
  
  print("enter the number of the function that you want:\n"+
        "1)for factorial\n"+
        "2)for divisors\n"+
        "3)for reverseString\n"+
        "4)for evenNumbers\n"+
        "5)for password validator\n"+
        "6)for IPv4 validator\n"+
        "7)exit"
       )

  

  
  choice=0
  while(choice!=7):
    choice=input()
    #to check wether the input is a number or not and it has a function
  
    while(not choice.isdigit() or int(choice)>6 or int(choice)<0):
      choice =input("invalide input. Enter the number of the function ")

    choice=int(choice)

    if(choice==1):

      num=input("enter a number")
      while(not num.isdigit()):
        num=input("enter a POSITIVE number")
      num=int(num)
      print("the factorial of",num,"is",factorial(num))
      
    elif(choice==2):

      num=input("enter a number:")

      while(not num.isdigit() and not num.startswith('-') and  not num[1:].isdigit()):#to check if user enter a number and it's not e negative because .isdigit() consider negative numbers false
        num=input("enter a NUMBER")
      num=int(num)
      print("divisors are",divisors(num))
      
    elif(choice ==3):
      str=input("enter a string to reverse:")
      print (str,"reversed is",reverseString(str))
      
    elif(choice==4):
      size=input("enter the number of elements in the list:")

      while(not size.isdigit()):
        size=input("enter the NUMBER of elements in the list:")

      size=int(size)

      my_list=[]
      
      while(size>0):  
        num=int(input("enter a number:"))
        my_list.append(num)
        size-=1
      print("the even numbers are",evenNumbers(my_list))
      
    elif(choice ==5):
      password=input("enter a password:")
      passwordValidator(password)
  
    elif(choice ==6):
      ip=input("enter an ip address:")
      flag=True
      numbers=ip.split('.')

      for num in numbers:
        if(not num.isnumeric()):
          flag=False

      while not flag:
        ip=input("enter a positive number")
        numbers=ip.split('.')
        flag=True
        for num in numbers:
          if(not num.isnumeric() ):
            flag=False
      
        

      if(IPv4Validator(ip)==True):
        print("valid")
      else:
          print("Invalid")

    elif(choice==7) :
      return 0
    print("\nenter another function:\n")

main()