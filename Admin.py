class Admin :
    def __init__(self, admin_id, name, email ):
        self.adminId=admin_id
        self.name=name
        self.email=email
        self._tickets=[] # liste des tickets
    def assignTicket(self,ticket,user):
        ticket.assignTo(user)# DELEGUE A tickets
        print(f"{self.name}  a assigne le ticket # {ticket.ticketID}")
    def closeTicket(self, ticket):
        ticket.updateStatus ("Termine")# reutilise updates status
        print(f"{self.name} a ferme le ticket # {ticket.ticketID}")
    def viewAllTickets(self):
        return list (self._tickets)# retourne un copie