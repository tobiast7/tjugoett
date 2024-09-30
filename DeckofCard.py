import random
# Klass för kort
class Card():
    def __init__(self, suit, rank, value):
        self.suit = suit # sparar färgen som ett attribut på objektet.
        self.rank = rank # sparar ranken som ett attribut
        self.value = value # sparar värdet som ett attribut
    # skriver ut kort objekten som 'rank of suit' för att skriva ut king of hearts eller liknande
    def __str__(self):
        return f"{self.suit} {self.rank} "

class Deck(list):
    def __init__(self):
        # objekt från denna klas ärver får list datatypen 
        # och att create_deck metoden anropas när deck() objektet ska skapas.
        super().__init__(self.create_deck())
        self.name = "deck"
    
    def create_deck(self):
        suits = ["Hjärter", "Klöver", "Spader", "Ruter"]
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        #skapar ett nytt card objekt med suit, rank och värde
        #parar ihop rank och value så 2 blir = 2 och Q(drottning) blir 12 osv
        #skapar en lista men ett kort för varje (rank och value) i varje suit(färg)
        return [Card(suit, rank, value) for suit in suits for rank, value in zip(ranks, values)]
    
    def shuffle_deck(self):
        random.shuffle(self)

class Hand(list):
    def __init__(self, name):
        # Ärver alla metoder och egenskaper ifrån datatypen "list"
        super().__init__()
        # används för att kunna identifiera ifall det är spelaren eller bankirens hand
        self.name = name

    def draw(self, deck: list):
        # drar översta kortet från "deck" och ger till instans som anropar metoden
        self.append(deck.pop(0))
        
    def hand_value(self):
        #räknar ut värdet på instansen som anropar metoden
        total_value = 0
        num_aces = 0  # För att hantera ess som kan vara 14 eller 1

        for card in self:
            total_value += card.value
            if card.rank == "A":
                num_aces += 1

        # Justera essens värde om det är nödvändigt
        while num_aces > 0 and total_value > 21:
            # Minskar total_value med 13 för att göra så att ett av Essen räknas som 1 istället för 14
            total_value -= 13
            # tar bort antal ess som justerats för att kontrollera ifall det finns fler ess att kontrollera
            num_aces -= 1

        return total_value