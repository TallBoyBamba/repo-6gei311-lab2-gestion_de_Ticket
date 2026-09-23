from datetime import datetime


class User:
    def __init__(self, user_id, name, email, role):
        self.userID = user_id
        self.name = name
        self.email = email
        self.role = role

    def createTicket(self, ticket):
        ticket.creator = self
        print(f"{self.name} a créé le ticket #{ticket.ticketID} : {ticket.title}")

    def viewTicket(self, ticket):
        print(f"--- Ticket #{ticket.ticketID} ---")
        print(f"Titre : {ticket.title}")
        print(f"Statut : {ticket.status}")
        print(f"Priorité : {ticket.priority}")
        print("Pièces jointes :")
        if not ticket.attachments:
            print("  (aucune)")
        else:
            for attachment in ticket.attachments:
                print(f"  - {type(attachment).__name__} : {attachment.load()}")

    def updateTicket(self, ticket, title=None, priority=None):
        if title is not None:
            ticket.title = title
        if priority is not None: 
            ticket.priority = priority
        ticket.updateDate = datetime.now()    
        print(f"{self.name} a mis à jour le ticket #{ticket.ticketID}")
         



