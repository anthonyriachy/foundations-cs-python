
class Stack():
    def __init__(self):
        self.stack=[]

    def push(self,value):
        self.stack.append(value)
    
    def pop(self):
        return self.stack.pop()
    
    def isEmpty(self):
        return self.stack==[]
     
    def size(self):
        return len(self.stack)




class Graph():
    def __init__(self,size):
        self.adj_matrix={}

        self.vertex_list={}

        self.size=size

        for i in range(size):
            self.vertex_list[f'name_{i}']=i
            self.adj_matrix[f'name_{i}']={f'name_{i}':0 for i in range(size)}
            # self.adj_matrix.append([0 for i in range(size)]) #create a 2d array and fill it with 0
            
        
    def print_adj_matrix(self):
        print('adjencent matrix: ')
        for i in self.adj_matrix:
            print('at',i,'is',self.adj_matrix[i])
        print('vertex list: ')
        for i in self.vertex_list:
            print('name is:',i,'position:',self.vertex_list[i])
        print('inverted vertex list:')

    
    def add_edge(self,name_1,name_2):
        self.adj_matrix[name_1][name_2]=1
        self.adj_matrix[name_2][name_1]=1
        
    def remove_edge(self,name_1,name_2):
        if(self.adj_matrix[name_1][name_2]==0):
            print('there is no relation between them')
            return
        self.adj_matrix[name_1][name_2]=0
        self.adj_matrix[name_2][name_1]=0
    

    def remove_vertex(self,user):
        del self.adj_matrix[user]
        self.size=self.size-1
        for i in self.adj_matrix.values():
            del i[user]
        del self.vertex_list[user]
        


    def check_user(self,user):
        return user in self.vertex_list

    def add_vertex(self,user):
        #use vertex later as the Name of the facebook user
        pos=self.size

        self.size=pos #incrememnt size by 1
        self.vertex_list[user]=pos #add it to the vertex_list
        
        self.adj_matrix[user]=({i:0 for i in (self.vertex_list)}) # add a new row of zeros

        for i in self.adj_matrix:
            self.adj_matrix[i][user]=0


        

    def list_of_friends(self,name):
        friends=[]
        name_pos=self.vertex_list[name]
        for i in self.adj_matrix[name]:
            if(self.adj_matrix[name][i]==1):

                friends.append(i) #insert the numebr of the friend 

        for i in friends: 
            print(i)
            


    def DFS(self,v):
        visited={i:False for i in self.adj_matrix}        
        stack=Stack()
        stack.push(v)

        while False in visited.values():

            if stack.isEmpty():
                for i in visited:
                    if not visited[i]:
                        stack.push(i)

            else:
                v =stack.pop()
                if not visited[v]:
                    visited[v]=True
                    print(v,end=" ")
                    for i in self.adj_matrix[v]:
                        if(self.adj_matrix[v][i]==1 and not visited[i]):
                            stack.push(i)
        print('\n')
def main():
    people=Graph(8)

    # people.add_edge('name_2',"name_3")
    # people.add_edge('name_2',"name_4")
    # people.add_edge('name_2',"name_6")
    # people.add_edge('name_2',"name_9")
    # people.add_edge('name_2',"name_0")
    menu="1.Add a user to the platform.\n2.Remove a user from the platform\n3.Send a friend request to another user.\n4.Remove a friend from your list\n5.View your list of friends.\n6.View the list of users of the platform.\n7.Exit\n- - - - - - - - - - - - - - - -\nEnter a choice:"
    choice=0

    while(choice!=7):
        print(menu)
        choice=input()
        while(not choice.isdigit() or int(choice)<0 or int(choice)>7):
            choice=input("etner a valid choice")
        choice=int(choice)

        if(choice==1):
            user=input("enter the userName you want to add: ")
            user_exists=people.check_user(user)
            if(user_exists):
                print('userName already exists')
            else:
                people.add_vertex(user)

        if(choice==2):
            user=input('enter the user you want to delete: ')
            user_exists=people.check_user(user)
            if(not user_exists or user=='name_0'):
                print('userName does not exist')
            else:
                people.remove_vertex(user)
        if (choice==3):
            user_1=input("enter the name of the first user")

            user_exists=people.check_user(user_1)
            if(not user_exists):
                print('userName does not exist')
            else:
                user_2=input("enter the name of the second user")
                user_exists=people.check_user(user_2)
                if(not user_exists):
                    print('userName does not exist')
                else:
                    people.add_edge(user_1,user_2)

        if(choice==4):
            user_1=input("enter the name of the first user")
            user_exists=people.check_user(user_1)
            if(not user_exists):
                print('userName does not exist')
            else:
                user_2=input("enter the name of the second user") #check if users are here
                user_exists=people.check_user(user_2)
                if(not user_exists):
                    print('userName does not exist')
                else:
                    people.remove_edge(user_1,user_2) 
        if(choice==5):
            user=input('enter the user you want to find his friends')
            user_exists=people.check_user(user)
            if(not user_exists):
                print('userName does not exist')
            else:
                people.list_of_friends(user)
        if(choice==6):
            people.DFS('name_0')




    
    
    people.add_edge('name_2',"name_3")
    people.add_edge('name_2',"name_4")
    people.add_edge('name_2',"name_6")
    people.add_edge('name_2',"name_9")
    people.add_edge('name_2',"name_0")
    people.print_adj_matrix()   
    print('friends are: ')
    people.list_of_friends('name_2')
    people.DFS(0)
main()


