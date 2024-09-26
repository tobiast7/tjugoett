from DeckofCard import *

class Game:
    def __init__(self):
        # Skapa en kortlek och blandar den
        self.deck = Deck()
        self.deck.shuffle_deck()

        # Skapa spelarens och dealerns händer
        self.player_hand = Hand("Player")
        self.dealer_hand = Hand("Dealer")

        # Ge två kort till spelaren och två kort till dealern
        self.deal_initial_cards()

    def deal_initial_cards(self):
        # Ge två kort till både spelaren och dealern
        for _ in range(2):
            self.player_hand.draw(self.deck)
            self.dealer_hand.draw(self.deck)

    def display_hands(self, show_dealer_card=False):
        # Visa spelarens hand
        print(f"\n{self.player_hand.name}'s hand:")
        for card in self.player_hand:
            print(card)
        print(f"Total Value: {self.player_hand.hand_value()}")

        # Visa dealerns hand och döljer ett kort tills spelarens tur är klar
        print(f"\n{self.dealer_hand.name}'s hand:")
        if show_dealer_card:
            for card in self.dealer_hand:
                print(card)
            print(f"Total Value: {self.dealer_hand.hand_value()}")
        else:
            print(self.dealer_hand[0])  # visar endast 1 kort tills värdet på show_dealer_card=true

    def player_turn(self):
        # Spelaren får val att få fler kort eller stanna
        while self.player_hand.hand_value() < 21:
            choice = input("\nVill du dra ett till kort? (ja/nej): ").lower()
            if choice == "ja":
                self.player_hand.draw(self.deck)
                print("\nDin hand:")
                for card in self.player_hand:
                    print(card)
                print(f"Total Value: {self.player_hand.hand_value()}")
            elif choice == "nej":
                break
            # så att programmet enbart hoppar vidare ifall spelaren skriver nej 
            # och inte enbart fortsätter ifall spelaren skriver ja.
            else:
                print("fel inmatning, vad god skriv ja eller nej")

    def dealer_turn(self):
        # Dealern drar kort tills deras handvärde är minst 17
        while self.dealer_hand.hand_value() < 17:
            print("\nDealern drar ett kort...")
            self.dealer_hand.draw(self.deck)
            self.display_hands(show_dealer_card=True)

    def check_winner(self):
        # Kontrollera vem som har vunnit
        player_value = self.player_hand.hand_value()
        dealer_value = self.dealer_hand.hand_value()

        if player_value > 21:
            return "Du bustade! Dealern vinner."
        elif dealer_value > 21:
            return "Dealern bustade! Du vinner!"
        elif player_value > dealer_value:
            return "Du vinner!"
        elif player_value < dealer_value:
            return "Dealern vinner!"
        else:
            return "Oavgjort!"
    #funktion för att spela spelet
    def play_game(self):
        
        print("Välkommen till Tjugoett!\n")
        # visar korten
        self.display_hands()

        # Spelarens tur
        self.player_turn()

        # Så länge spelaren in bustade så fortsätter dealern med att dra sina kort
        if self.player_hand.hand_value() <= 21:
            self.dealer_turn()

        # Ändrar show_dealer_card till true så korten visas
        self.display_hands(show_dealer_card=True)
        print(self.check_winner())

        
# Startar spelet och fortsätter tills användaren vill sluta spela genom att skriva nej
if __name__ == "__main__":
    while True:
        game = Game()
        game.play_game()
        
        while True:
            #tar input ifrån användaren och gör om till .lowercase
            play_again = input("\nVill du spela igen? (ja/nej): ").lower()
            if play_again == "ja":
                break  # Gå tillbaka till början av loopen och starta en ny omgång
            elif play_again == "nej":
                print("Tack för att du spelade!")
                exit()  # Avsluta programmet
            else:
                print("Felaktigt alternativ valt. Vänligen skriv 'ja' eller 'nej'.")