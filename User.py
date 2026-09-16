from datetime import datetime 

class User:
    def __init__(self, user_id, name, email, role):
        self.userID = user_id    # self equivaut à this->userID = user_id en C++ (je fais ce commentaire pour moi Bamba)
        self.name = name
        self.email = email
        self.role = role 

    def createTicket(self, ticket):
        ticket.creator = self    # implémente l'association "creates" : le ticket garde une référence vers son créateur
        print(f"{self.name} a cree le ticket #{ticket.ticketID} : {ticket.title}")


    def viewTicket(self, ticket):
        print(f" Ticket #{ticket.ticketID} ---")
        print(f"Titre : {ticket.title}")
        print(f"Description : {ticket.description}")
        print(f"Statut : {ticket.status}")
        print(f"Priorité : {ticket.priority}") 


    def updateTicket(self, ticket, title=None, description=None, priority=None):
        if title is not None: 
            ticket.title = title 
        if description is not None: 
            ticket.description = description 
        if priority is not None:  
            ticket.priority = priority 
        ticket.updateDate = datetime.now() 
        print(f"{self.name} a mis a jour le ticket #{ticket.ticketID}") 




