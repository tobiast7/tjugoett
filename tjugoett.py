from DeckofCard import *

# skapar en klass för hur spelet ska fungera
class Game:
    def __init__(self):
        # Skapa en kortlek och blandar den
        self.deck = Deck()
        self.deck.shuffle_deck()

        # Skapa spelarens och bankirens händer
        self.player_hand = Hand("Spelaren")
        self.bankir_hand = Hand("Bankiren")

        # Ge två kort till spelaren och två kort till bankiren
        self.deal_cards()

    def deal_cards(self) -> None:
        # Ge två kort till både spelaren och bankiren
        for i in range(2):
            self.player_hand.draw(self.deck)
            self.bankir_hand.draw(self.deck)

    def show_hands(self, show_bankir_card=False):
        # Visa spelarens hand
        print(f"\n{self.player_hand.name}'s hand:")
        for card in self.player_hand:
            print(card)
        print(f"Total Value: {self.player_hand.hand_value()}")

        # Visa bankirens hand och döljer ett kort tills spelarens tur är klar
        print(f"\n{self.bankir_hand.name}'s hand:")
        if show_bankir_card:
            for card in self.bankir_hand:
                print(card)
            print(f"Total Value: {self.bankir_hand.hand_value()}")
        else:
            print(self.bankir_hand[0])  # visar endast 1 kort tills värdet på show_dealer_card=true

    def spelarens_turn(self):
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

    # funktion för när det är bankirens tur
    def bankirens_turn(self):
        # Bankiren drar kort tills deras handvärde är minst 17
        while self.bankir_hand.hand_value() < 17:
            print("\nBankiren drar ett kort...")
            self.bankir_hand.draw(self.deck)
            self.show_hands(show_bankir_card=True)

    # funktion för att kontrollera resultatet som sedan retunerar en str
    def check_winner(self) -> str:
        # Kontrollera vem som har vunnit
        player_value = self.player_hand.hand_value()
        bankir_value = self.bankir_hand.hand_value()
        # kontrollerar resultatet genom att se ifall någon fått över 21
        if player_value > 21:
            return "Du blev tjock! Bankiren vinner."
        elif bankir_value > 21:
            return "Bankiren blev tjock! Du vinner!"
        # om ingen blev tjock så kontrollerar den vem som har högst poäng(närmst 21)
        elif player_value > bankir_value:
            return "Du vinner!"
        elif player_value < bankir_value:
            return "Bankiren vinner!"
        else:
            return "Oavgjort!"
    #funktion för att spela spelet
    def play_game(self):
        
        print("Välkommen till Tjugoett!\n")
        # visar korten
        self.show_hands()

        # Spelarens tur
        self.spelarens_turn()

        # Så länge spelaren in bustade så fortsätter bankiren med att dra sina kort
        if self.player_hand.hand_value() <= 21:
            self.bankirens_turn()

        # Ändrar show_bankir_card till true så korten visas
        self.show_hands(show_bankir_card=True)
        print(self.check_winner())

        
# Startar spelet och fortsätter tills användaren vill sluta spela genom att skriva nej
if __name__ == "__main__":
    print("Välkommen till Tjugoett!")

    start_game = input("Vill du starta ditt spel? (ja/nej): ").lower()

    if start_game == "ja":
        while True:
            # Skapa ett spelobjekt och anropa play_game-funktionen som startar spelet
            game = Game()
            game.play_game()

            # Fråga om spelaren vill spela igen
            play_again = input("\nVill du spela igen? (ja/nej): ").lower()
            if play_again != "ja":
                print("Tack för att du spelade!")
                break  # Avsluta loopen och programmet

    elif start_game == "nej":
        print("Programmet avslutas")
    else:
        print("Felaktigt alternativ. Vänligen skriv 'ja' eller 'nej'.")