#-*- coding: utf-8 -*- 
from User import User
from Admin import Admin
from Ticket import Ticket 


def main():
    # Objets créées pour tester le menu
    dev1 = User(1, "Almamy", "Almamy.Sylla@uqac.ca", role="Développeuse")
    admin1 = Admin(1, "Bamba", "Bamba.admin@uqac.ca")
    ticket1 = Ticket(101, "Bug d'affichage", "Le bouton de connexion ne répond pas sur mobile.")
    admin1._tickets.append(ticket1)  # contournement temporaire — cf. Section I du rapport

    while True:
        print("\n=== Menu principal ===")
        print("1. connecter vous comme user")
        print("2. connecter vous comme Admin")
        print("3. Quitter")
        choix = input("Choix : ")

        if choix == "1":
            # --- Sous-menu User ---
            while True:
                print("\n--- Menu User ---")
                print("1. Créer un ticket")
                print("2. Voir le ticket")
                print("3. Mettre à jour le ticket")
                print("4. Retour au menu principal")
                sous_choix = input("Choix : ")

                if sous_choix == "1":
                    dev1.createTicket(ticket1)
                elif sous_choix == "2":
                    dev1.viewTicket(ticket1)
                elif sous_choix == "3":
                    nouvelle_priorite = input("Nouvelle priorité : ")
                    dev1.updateTicket(ticket1, priority=nouvelle_priorite)
                elif sous_choix == "4":
                    break
                else:
                    print("Choix invalide, fais un bon choix.")

        elif choix == "2":
            # --- Sous-menu Admin ---
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
                    print("Choix invalide, fais un bon choix.")

        elif choix == "3":
            print("A la prochaine")
            break
        else:
            print("Choix invalide, fais un bon choix.")


if __name__ == "__main__":
    main() 