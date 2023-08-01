from datetime import date



#for the date: https://www.programiz.com/python-programming/datetime 
#for the id to add zeros to the left side: https://www.python-engineer.com/posts/pad-zeros-string/#:~:text=Use%20str.,-zfill(width)&text=zfill%20is%20the%20best%20method,a%20string%20of%20length%20width.


######################
## reading the file ##
######################
def readFile():
    ticket_list=[] #list of tickets
    with open('tickets.txt','r') as file:
        lines = file.readlines()
        for line in lines:
            line=line.split(', ')
            ticket={
                'ticket_id':int(line[0].strip().strip('tick')),
                'event_id':int(line[1].strip().strip('ev')),
                'owner':line[2],
                'event_date':int(line[3]),
                'priority':int(line[4])
            }
            ticket_list.append(ticket)

    return ticket_list


#######################
## sorting the array ##
#######################
def merge(ticket_list,left,mid,right,key):
    low=left #starting index 
    high=mid+1 
    k=0 #for the new list
    temp=[] #new array
    while(low<=mid and high<=right):
        if(ticket_list[low][key]<ticket_list[high][key]):
            temp.append(ticket_list[low])
            k+=1
            low+=1
        else:
            temp.append(ticket_list[high])
            k+=1
            high+=1
    while(low<=mid):
        temp.append(ticket_list[low])
        k+=1
        low+=1
    while(high<=right):
        temp.append(ticket_list[high])
        k+=1
        high+=1
    for i in range(k):
        ticket_list[left+i]=temp[i]
#######################
## sorting the array ##
#######################
def merge_sort(ticket_list,left,right,key):
    if(left<right):
        
        mid=(left+right)//2
        merge_sort(ticket_list,left,mid,key)
        merge_sort(ticket_list,mid+1,right,key)

        merge(ticket_list,left,mid,right,key)
    return ticket_list



#################################################
## search for first occurance with today's date##
#################################################
def search(ticket_list,date):
    index=0
    while(index<len(ticket_list) and ticket_list[index]['event_date']<date ): #searching for the date or the nearest date
        index+=1
    
    return index
        
            
            




###################
## range of date ##
###################
def range_of_same_date(new_list):
    indices=[]
    i=0
    while i < len(new_list): #for each date in the list we check if there is consecutive dates equal to it
        starting_index=0
        ending_index=0 #these are for the parts that are equal dates
        j=i+1

        while(j<len(new_list) and new_list[i]['event_date'] == new_list[j]['event_date']): #while the event date are the same (because sorted they will be next to each other) we keep looping
        
            starting_index=i
            ending_index=j #when the loop stops we will have the correct ending date
            

            j+=1
        i=j # because j is the ending_index of the tickets with same date (we don't want to check them again)

        indices.append({'starting_index':starting_index,'ending_index':ending_index}) #dictionaries that have the starting and ending index of dates that are the same
    return(indices)
        
        
    

##############
## choice 1 ##
##############
def display_statistics(ticket_list):
    element_occurance={} #dictionary that has key=the id of the event, and data=number of occurance of that id
    for ticket in ticket_list: #ticket list is a list of dicitionaries each dic has the ticket data
        event_id=ticket['event_id']

        if(event_id in element_occurance):
            element_occurance[event_id]+=1
        else: #add a new event in the dictionary and initilize to 1
            element_occurance[event_id]=1

    Max_occurance=0
    event_id_index=[]
    for index in element_occurance:
        if(element_occurance[index]>Max_occurance):
            Max_occurance=element_occurance[index] #find max occurance

    for index in element_occurance:
        if(Max_occurance == element_occurance[index]):
            event_id_index.append(index) #find all the tickets that are ewaule to max occurance

    return event_id_index


##############
## choice 2 ##
##############
def add_ticket(event_id,userName,priority,event_date,ticket_list,save=None):
    index=0
    new_ticket={  #new tickets dicitonry
        'ticket_id':len(ticket_list)+1,
        'event_id':int(str(event_id).zfill(3)),
        'owner':userName,
        'event_date':int(event_date),
        'priority':priority
    }

    while(index<len(ticket_list) and ticket_list[index]['priority']<priority): # insert it in its right position 
        index+=1
    ticket_list.insert(index,new_ticket)
    
    if(save): #when a user adds a ticket
        with open('tickets.txt','a') as file:
            
            event_id=str(new_ticket["event_id"]).zfill(3)
            ticket = f'tick{new_ticket["ticket_id"]}, ev{event_id}, {new_ticket["owner"]}, {new_ticket["event_date"]}, {new_ticket["priority"]}\n'
            file.write(ticket)
        

##############
## choice 3 ##
##############
def displayTickets(ticket_list):
    today_date=int(date.today().strftime("%Y%m%d"))

    merge_sort(ticket_list,left=0,right=len(ticket_list)-1,key='event_date') #sort by date

    starting_index=search(ticket_list,today_date) #function that returns the starting index for the list with the correct dates and sorted 
    
    new_list=ticket_list[starting_index:len(ticket_list)] #new list that has the correct dates (without old dates)

    indices=range_of_same_date(new_list) #function that return a list of dictionaries with the range of the consecutive items 

    for i in range(len(indices)): #I use the ranges dictionary of indices to sort the items that have the save date 
        merge_sort(new_list,left=indices[i]['starting_index'],right=indices[i]['ending_index'],key='event_id') #sort by event_id

    for i in (new_list): #print the sorted list
        print(i)




##############
## choice 4 ##
##############
def edit_priority(ticket_list,ticket_id,new_priority):
    index=0
    while(index<len(ticket_list) and ticket_list[index]['ticket_id']!=ticket_id): #when the loop stops we will have the index of the ticket_id we want to edit
        index+=1

    if(index>=len(ticket_list)): #if we traverse the whole list => we didn't find the ticket_id
        print('element not found')
        return False
    else:
        ticket_list[index]['priority']=new_priority #we change the priority
        return True


##############
## choice 5 ##
##############
def delete_ticket(ticket_id,ticket_list):
    index=0
    while(index<len(ticket_list) and ticket_list[index]['ticket_id']!=ticket_id): #finding the index of ticket_id 
        index+=1

    if(index>=len(ticket_list)): #if we traverse the whole list without finding the ticket_id
        print('ticket not found')
        return False
    else:
        del ticket_list[index]
    return True

##############
## choice 6 ##
##############
def run_events(ticket_list):
    today=int(date.today().strftime('%Y%m%d'))
    today_event=[] #list that contains today's events

    for i in ticket_list:
        if (i['event_date']==today):
            today_event.append(i)

    for i in today_event: #delete the ticket's that have the date of today
        ticket_list.remove(i)

    if(len(today_event)==0): #no ticket's for today
        print('no events today')

    return today_event


################
# Admin menu ##
################
def admin_menu(ticket_list):

    menu="options:\n \t1. Display Statistics\n \t2. Book a Ticket\n \t3. Display all Tickets\n \t4. Change Ticket's Priority\n\t5. Disable Ticket\n\t6. Run Events\n\t7. Exit"
    choice=0
    while(choice!='7'):
        print(menu)
        choice=input('enter the number of your choice:')
        while(not choice.isdigit() or int(choice)<1 or int(choice)>7): #choice validation
            choice=input('entre a valid number')

        if(choice=='1'):
            print('the event(s) with most number of tickets is/are:',end="")
            indexs=display_statistics(ticket_list) #list that conatains a list of the correct tickets 
            for i in indexs:
                print('ev'+str(i).zfill(3),end=' ')
            print('\n')


        if(choice=='2'): #do if two events are the same
            event_id=input('enter the event id')

            while(not event_id.isdigit()): #event id validation
                event_id=input('enter a valid event id')
            event_id=int(event_id)

            userName=input('enter the name of the ticket owner:')

            priority=input('etner the priority:')
            while(not priority.isdigit()):
                priority=input('etner the priority should be a number:')
            priority=int(priority)

            year=int(input('enter the year:'))
            while(year<int(date.today().strftime('%Y'))):#year validation
                year=int(input('enter a valid year:'))

            month=int(input('enter the month number:'))
            while(int(date(year,month,1).strftime('%Y%m'))< int(date.today().strftime('%Y%m'))): #month validation
                month=int(input('enter a valid month number:'))

            day=int(input('enter the day number:'))
            while(int(date(year,month,day).strftime('%Y%m%d'))< int(date.today().strftime('%Y%m%d'))): #day validation
                day=int(input('enter a valid day number:'))

            event_date = date(year,month,day).strftime("%Y%m%d")

            add_ticket(event_id,userName,priority,event_date,ticket_list)


        if(choice=='3'):
            displayTickets(ticket_list)


        if(choice=='4'):
            ticket_id=input('enter the ticket ID')
            while(not ticket_id.isdigit()): #ticket id validation
                ticket_id=input('enter a valid event id')
            ticket_id=int(ticket_id)

            new_priority=input('enter new priority')
            while(not new_priority.isdigit()):#ticket priority validation
                new_priority=input('etner the priority should be a number:')
            new_priority=int(new_priority)

            found=edit_priority(ticket_list,ticket_id,new_priority) #function that edits the priority if the ticket is found it will return true

            if(found): #if we changed the priority we sort the elements again
                merge_sort(ticket_list,left=0,right=len(ticket_list)-1,key='priority')


        if(choice=='5'):
            ticket_id=input('enter the id of the ticket you want to delete: ')
            while(not ticket_id.isdigit()):
                ticket_id=input('enter a valid id for a ticket you want to delete: ')

            delete_ticket(int(ticket_id),ticket_list)
        
        if (choice=='6'):
            my_list=run_events(ticket_list)#function will return a list of tickets that have today's date

            for i in my_list:
                print(i)
        



###############
## user menu ##
###############
def user_menu(userName,ticket_list):
    print('welcome',userName)
    menu="options:\n \t1. Book a Ticket\n \t2. Exit"
    choice=0
    while(choice!='2'):
        print(menu)
        choice=input("enter the number of your choice: ")
        while(not choice.isdigit() or int(choice)<1 or int(choice)>2):
            choice=input("enter a valid choice")

        if(choice=='1'):
            event_id=input('enter the event id')
            while(not event_id.isdigit()):
                event_id=input('enter a valid event id')
            event_id=int(event_id)

            priority=0 #initilize priority to 0
            
            year=int(input('enter the year:'))
            while(year<int(date.today().strftime('%Y'))):#year validation
                year=int(input('enter a valid year:'))
            
            month=int(input('enter the months number:'))
            while(int(date(year,month,1).strftime('%Y%m'))< int(date.today().strftime('%Y%m'))): #month validation
                month=int(input('enter a valid month number:'))

            day=int(input('enter the day number:'))
            while(int(date(year,month,day).strftime('%Y%m%d'))< int(date.today().strftime('%Y%m%d'))): #day validation
                day=int(input('enter a valid day number:'))

            event_date= date(year,month,day).strftime("%Y%m%d")

            add_ticket(event_id,userName,priority,event_date,ticket_list,save=True)
            #userName from the argument and the save=true is a optional parameter to save the data to the file 




#####################
## user validation ##
#####################
def validate_user(userName,password,ticket_list):
    


    attempts=0
    flag_attempts=True
    flag_valid=False

    string='' #string do be printed (for wrong user name and password)

    
    while(attempts<4 and flag_valid ==False): 
        flag_user=True
        flag_password=True
        
        if(password!=''): # for admin

            string='wrong ' #string of error to be displayed
            
            if(userName!='admin'):  #check user name
                string+=' admin username ' #add to the string
                flag_user=False     #flag = False if user name is false

            if(password!='admin123123'):
                if(flag_user==False): #if user name also wrong add 'and'
                    string+=" and "

                string+=' password ' #string to be displayed
                flag_password=False

            flag_valid=flag_password and flag_user #check if everything is true

            if(flag_valid): #if correct
                admin_menu(ticket_list) #display admin menu send the list of ticket also

        else:  # for normal user
            if(userName=='admin'):   #if a normal user (without password) enter his username as admin 
                string+='wrong admin password'
                flag_password=False
            else:
                user_menu(userName,ticket_list) #display user menu if correct send the userName and list of ticket also

        flag_valid=flag_password and flag_user

        if(flag_valid):
            string='bye'
        print(string)              
        
        if(not flag_valid): #if password is false
            attempts+=1
            print('attempts left :',5-attempts)
            userName=input('re-enter your username:')
            password=input('re-enter your password:')
            


##########
## main ##
##########
def main():
    my_list=readFile() #import the file and store them in a list of dicitionaries  each dictionary has the information of one ticket
    
    merge_sort(my_list,left=0,right=len(my_list)-1,key="priority") #special list sorted by priority

    userName=input('enter your username:')
    password=input('enter your password:')

    validate_user(userName.strip(' '),password.strip(' '),my_list) #validate the username and password and then go the user menue or admin menu


main()
