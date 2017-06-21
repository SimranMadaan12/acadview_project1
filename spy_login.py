# importing classes Spy,ChatMessage & list friend[] & object spy of class Spy
from spy_detail import Spy, ChatMessage, friend, spy
# importing library steganography for message encoding
from steganography.steganography import Steganography
# default status
STATUS_MESSAGES = ['My name is Bond, James Bond', 'Shaken, not stirred.', 'Keeping the British end up, Sir']

print "Hello! Let\'s get started"

# to continue with the default user or create their own
question = "Want to continue as " + " " +spy.salutation+ " " +spy.name + "Y/N?"
exist = raw_input(question)


# function definition for status update, for adding a new status , appending the new status to old list , selecting from old ones
def add_status():
    updated_status_message = None
    if spy.current_status_message != None:
        print "Your current status message is %s \n"%(spy.current_status_message)
    else:
        print "You don't have any current status. \n"
    default =raw_input("Do you want to select from old [y/n]?")
    if default.upper() == "N": # adding a new status and upper() function will convert lower letter into upper case
         new_status_message = raw_input("What status do you want to set?")
         if len(new_status_message) > 0:
               STATUS_MESSAGES.append(new_status_message)   # To append the new status to old list
               updated_status_message=new_status_message
    elif default.upper() == "Y": # selecting from old status
        item_position = 1
        for message in STATUS_MESSAGES: # to Print the status list we apply the loop
            print str(item_position)+ " " + message
            item_position = item_position+1
        message_selection=int(raw_input("\n Choose from above messages"))
        if len(STATUS_MESSAGES) >= message_selection:
            updated_status_message = STATUS_MESSAGES[message_selection-1] # zero base indexing
        else:
            print  "Please enter valid choice!!"
    else:
         print "The option you chose is not valid! Press either y or n"  # other than yes or no
    if updated_status_message:
        print 'Your updated status message is: %s' % (updated_status_message)
    else:
         print 'You current don\'t have a status update'
    return updated_status_message



# to decode a send message
def read_message():
  sender = select_friend()

  output_path = raw_input("What is the name of the file?")
  secret_text = Steganography.decode(output_path)
  new_chat = ChatMessage(secret_text,False)
  friend[sender].chats.append(new_chat)
  print "Your secret message is!"+ secret_text

# to send a encoded message to your friend from friend list
def send_message():
  friend_choice = select_friend()
  print  friend_choice

  original_image = raw_input("What is the name of the image?")
  output_path = 'output.jpg'
  text = raw_input("What do you want to say?")
  Steganography.encode(original_image, output_path, text)
  new_chat = ChatMessage(text,True)
  friend[friend_choice].chats.append(new_chat)
  print"Your Secret message is ready!!!"



# to add  a new friend we create a object new_friend of class Spy
def add_friend():
    new_friend = Spy('','',0,0.0)



    new_friend.name = raw_input("Please add your friend's name:")
    if len(new_friend.name) >0 and new_friend.name.isspace() == False:  # isspace() function is set to false so that user doesnot enter blank spaces

        new_friend.salutation = raw_input("Are they Mr. or Ms.")
        if new_friend.salutation == "Mr." or new_friend.salutation =="Ms.":

            new_friend.name = new_friend.salutation + " " + new_friend.name
            new_friend.age = int(raw_input("age?"))
            new_friend.rating = float(raw_input("Enter rating"))


            if  new_friend.age>18 and new_friend.rating>=spy.rating:
              friend.append(new_friend) # adding new friends to old list using append function
              print "ADD friend!!"
            else:
                print  "Sorry!! not eligible"
        else:
            print "enter valid salutation!!"

    else:
        print "sorry! invalid entry....."
    return len(friend) # to count number of friends in friend[] list

# used to choose friends from friend[] list
def select_friend():
    item_number = 0
    for frien in friend:
        print " %d.  %s"%(item_number +1,frien.name)
        item_number = item_number+1
    friend_choice=raw_input("Choose from your friends")
    friend_choice_position=int(friend_choice)-1
    return friend_choice_position
# to read old history sent by you or by your friend
def read_chat_history():
    read_for=select_friend()

    for chat in friend[read_for].chats:
        if chat.sent_by_me:
            print '[%s] %s: %s'%(chat.time.strftime("%d %B %Y"),'You said:',chat.message)
        else:
            print '[%s} %s said: %s'% (chat.time.strftime("%d %B %Y"),friend[read_for].name,chat.message)



# spy has multiple choices to choose from application
def spy_chat(spy):
    spy.name = spy.salutation + " " + spy.name
    if spy.age > 12 and spy.age < 50:
        print "Authentication complete. Welcome " + spy.name + " Proud to have you onboard"
        show_menu = True
        while show_menu:
            menu_choice = "what do you want to do?\n 1. Status Update \n 2. Add a Friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read chats from users \n 6. Exit application  "
            menu_choic = raw_input(menu_choice)
            if len(menu_choic) > 0:
                menu_choic = int(menu_choic)
                if menu_choic == 1:
                    spy.current_status_message = add_status() # calling of function
                elif menu_choic == 2:
                    number_of_friends = add_friend()  #  calling of function
                    print "You have %d friends" % (number_of_friends)
                elif menu_choic == 3:
                    send_message()      # calling of function
                elif menu_choic == 4:
                    read_message()      # calling of function
                elif menu_choic == 5:
                    read_chat_history()  # calling of function
                elif menu_choic == 6:
                    show_menu = False
    else:
         print 'Sorry you are not of the correct age to be a spy'




if (exist=="Y" or exist=="y"): # if existing user
    print "Welcome " + spy.salutation + " " +spy.name + " your age is " + str(spy.age) + " and rating is " + str(spy.rating)
    spy_chat(spy)  # calling of function


elif(exist=="N" or exist=="n"):  # if not a existing user
    spy = Spy('', '', 0, 0.0)
    spy.name = raw_input("Welcome to spy chat, you must tell me your spy name first:")
    if len(spy.name) > 0 and spy.name.isspace()== False:
     spy.salutation=raw_input("What should i call you Mr. or Ms.")
     if spy.salutation == "Mr." or spy.salutation == "Ms.":
        spy.age=int(raw_input("Enter your age"))
        spy.rating=float(raw_input("what is your spy rating"))
        spy.is_online = True
        spy_chat(spy)
     else:
         print "enter valid salutation!!"

    else:
        print 'Please add a valid spy name'

else:
    print "invalid choice!!!"


