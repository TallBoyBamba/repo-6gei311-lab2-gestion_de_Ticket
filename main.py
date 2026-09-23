# -*- coding: utf-8 -*-
from User import User
from Admin import Admin
from Ticket import Ticket
from Attachment import TextAttachment, ImageAttachment, VideoAttachment


def main():
    dev1 = User(1, "Almamy", "Almamy.Sylla@uqac.ca", role="Développeur")
    admin1 = Admin(1, "Bamba", "Bamba.admin@uqac.ca")
    ticket1 = Ticket(101, "Bug d'affichage")

    while True:
        print("\n=== Menu principal ===")
        print("1. connecter vous comme user")
        print("2. connecter vous comme Admin")
        print("3. Quitter")
        choix = input("Choix : ")

        if choix == "1":
            while True:
                print("\n--- Menu User ---")
                print("1. Créer un ticket")
                print("2. Voir le ticket")
                print("3. Mettre à jour le ticket")
                print("4. Ajouter une pièce jointe")
                print("5. Retour au menu principal")
                sous_choix = input("Choix : ")

                if sous_choix == "1":
                    admin1.createTicket(dev1, ticket1)
                elif sous_choix == "2":
                    admin1.viewTicket(dev1, ticket1)
                elif sous_choix == "3":
                    nouvelle_priorite = input("Nouvelle priorité : ")
                    admin1.updateTicket(dev1, ticket1, priority=nouvelle_priorite)
                elif sous_choix == "4":
                    print("Type : 1=Texte, 2=Image, 3=Vidéo")
                    type_choix = input("Choix : ")
                    chemin = input("Chemin du fichier : ")

                    if type_choix == "1":
                        nouvelle_piece = TextAttachment(chemin)
                    elif type_choix == "2":
                        nouvelle_piece = ImageAttachment(chemin)
                    elif type_choix == "3":
                        nouvelle_piece = VideoAttachment(chemin)
                    else:
                        nouvelle_piece = None
                        print("Type invalide.")

                    if nouvelle_piece is not None:
                        ticket1.addAttachment(nouvelle_piece)
                        print("Pièce jointe ajoutée.")
                elif sous_choix == "5":
                    break
                else:
                    print("Choix invalide, réessaie.")

        elif choix == "2":
            while True:
                print("\n--- Menu Admin ---")
                print("1. Assigner le ticket à dev1")
                print("2. Fermer le ticket")
                print("3. Voir tous les tickets")
                print("4. Retour au menu principal")
                sous_choix = input("Choix : ")

                if sous_choix == "1":
                    admin1.assignTicket(ticket1, dev1)
                elif sous_choix == "2":
                    admin1.closeTicket(ticket1)
                elif sous_choix == "3":
                    for t in admin1.viewAllTickets():
                        print(t)
                elif sous_choix == "4":
                    break
                else:
                    print("Choix invalide, réessaie.")

        elif choix == "3":
            print("Au revoir")
            break
        else:
            print("Choix invalide, réessaie.")


if __name__ == "__main__":
    main() 