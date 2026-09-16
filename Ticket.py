from datetime import datetime

class Ticket:
    def __init__(self, ticket_id, title, description, priority="Normal"):
        self.ticketID = ticket_id
        self.title = title
        self.description = description
        self.status = "OUVERT"
        self.priority = priority
        self.creationDate = datetime.now()
        self.updateDate = datetime.now()

        self.comments = []       # liste vide qui contiendra les commentaires ajoutés au fil du temps
        self.assignedTo = None   # aucun développeur assigné au départ

    def assignTo(self, user):
        self.assignedTo = user            # on enregistre qui est maintenant responsable du ticket
        self.status = "ASSIGNÉ"           # le ticket change automatiquement de statut
        self.updateDate = datetime.now()  # on trace le moment de l'assignation

    def updateStatus(self, status):
        self.status = status
        self.updateDate = datetime.now() 

    def addComment(self, comment):
        self.comments.append(comment)

    def __str__(self):
        return f"Ticket #{self.ticketID} - {self.title} [{self.status}] (priorité: {self.priority})" 


