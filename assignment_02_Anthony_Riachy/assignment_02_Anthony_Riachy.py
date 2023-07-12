htmlCode="""
<html>
  <head>
  <title>My Website</title>
  </head>
  <body>
    <h1>Welcome to my website!</h1>
    <p>Here you'll find information about me and my hobbies.</p>
    <h2>Hobbies</h2>
    <ul>
      <li>Playing guitar</li>
      <li>Reading books</li>
      <li>Traveling</li>
      <li>Writing cool h1 tags</li>
    </ul>
  </body>
</html>
"""


########################
#         ex 1         #
########################

def numOfDigits(num):
  
  num=int(num)#cast
  
  if(num==0):
    return 0
    
  return 1 + numOfDigits(num//10) 
########################
#         ex 2         #
########################

def findMax(lst,prevMax):
  
  if(len(lst)==0):
    return prevMax 
    
  if(lst[0]>prevMax):
    prevMax=lst[0]
    
  
  return findMax(lst[1:],prevMax)
  
########################
#         ex 3         #
########################

def htmltag(lst,tag):
  if(len(lst)==0):
    return 0
  if(lst[0][0:len(tag)]==tag):
    return 1+htmltag(lst[1:],tag)
  
  return htmltag(lst[1:],tag)
  
  


def main():
  choice=0
  
  while(choice!=4):
    print("\n\n1.Count Digits\n"+"2.Find Max\n"+"3.Count Tags\n"+"4.Exit")
    print("- - - - - - - - - - - - - -")
    
    choice=input("Enter a choice:")
  
    while(not choice.isdigit() or (int(choice)<0) or(int(choice)>4)):
      choice=input("Enter a valid number:")
      
    if(choice=="1"):
      number=input("enter an integer:")
      
      while(not number.isdigit()):      #user input validation
          number=input("enter a interger")
        
      print(numOfDigits(number))
      
    if(choice=="2"):
      num=0
      lst=[]
      size=input("enter the size of the array:")
      while(not size.isdigit()):    
          size=input("enter a interger")
      size=int(size)
      
      print("fill the list:")
      
      for i in range(size):
        num=input()
        while(not num):
          num=input("enter an integer: ")
          
        while(not num.isdigit() and num[0]!='-'):
          num=input("WRONG, enter an integer: ")
        num=int(num)
        lst.append(num)
      
      print("the largest number is :" ,findMax(lst[1:],lst[0]))
    if(choice=="3"):

      
      f=int(input("what HTML file do you want:\n 1)local variable (small)\n 2)large file"))
      tag=input("enter the tag you want to count:")
      if(f==2):
        with open('index.html' , 'r') as file:
          html=file.read()
        print(tag, "is repeated", htmltag(html.split("<"),tag),"times")
      if(f==1):
        print(tag, "is repeated", htmltag(htmlCode.split("<"),tag),"times")
      

      
      

    if(choice=="4"):
      return 0
    
  
    
main()
  