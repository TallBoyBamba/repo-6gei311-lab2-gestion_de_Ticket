class Admin:
    def __init__(self, admin_id, name, email):
        self.adminID = admin_id
        self.name = name
        self.email = email
        self._tickets = []

    def registerTicket(self, ticket):
        self._tickets.append(ticket)

    def createTicket(self, user, ticket):
        user.createTicket(ticket)
        self.registerTicket(ticket)

    def viewTicket(self, user, ticket):
        user.viewTicket(ticket)

    def updateTicket(self, user, ticket, **kwargs):
        user.updateTicket(ticket, **kwargs)

    def assignTicket(self, ticket, user):
        ticket.assignTo(user)
        print(f"{self.name} a assigné le ticket #{ticket.ticketID} à {user.name}")

    def closeTicket(self, ticket):
        ticket.updateStatus("TERMINÉ")
        print(f"{self.name} a fermé le ticket #{ticket.ticketID}")

    def viewAllTickets(self):
        return list(self._tickets) 
