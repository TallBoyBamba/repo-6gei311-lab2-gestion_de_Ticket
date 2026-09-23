from datetime import datetime
from Attachment import Attachment


class Ticket:
    def __init__(self, ticket_id, title, priority="Normal"):
        self.ticketID = ticket_id
        self.title = title
        self.status = "OUVERT"
        self.priority = priority
        self.creationDate = datetime.now()
        self.updateDate = datetime.now()

        self.comments = []
        self.assignedTo = None
        self.attachments = []

    def assignTo(self, user):
        self.assignedTo = user
        self.status = "ASSIGNÉ"
        self.updateDate = datetime.now()

    def updateStatus(self, status):
        self.status = status
        self.updateDate = datetime.now()

    def addComment(self, comment):
        self.comments.append(comment)

    def addAttachment(self, attachment: Attachment):
        self.attachments.append(attachment)
        self.updateDate = datetime.now()

    def __str__(self):
        return f"Ticket #{self.ticketID} - {self.title} [{self.status}] (priorité: {self.priority})"  


