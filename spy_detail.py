from datetime import datetime # importing a library datetime for current datetime

class Spy: # blueprint
    def __init__(self,name,salutation,age,rating): # constructor
     self.name = name
     self.salutation = salutation
     self.age = age
     self.rating = rating
     self.is_online = True
     self.chats = []
     self.current_status_message = None


class ChatMessage:
     def __init__(self,message,sent_by_me):
      self.message = message
      self.time = datetime.now()
      self.sent_by_me = sent_by_me




# objects  of class
spy = Spy('Simran','Ms.',21,4.8)

friend_one = Spy('Aman','Ms.',21,4.0)
friend_two = Spy('Bhavu','Ms.',21,4.5)
friend_three = Spy('Pooja','Ms.',20,4.3)
# adding objects in list
friend = [friend_one,friend_two,friend_three]

















