# Начнем с создания карты
# ♥ ♦ ♣ ♠
VALUES = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
SUITS = ('Spades', 'Clubs', 'Diamonds', 'Hearts') #Старшинство мастей определяем следующее: ♠<♣<♦<♥
SUITS_UNI = {
        'Spades': '♠',
        'Clubs': '♣',
        'Diamonds': '♦',
        'Hearts': '♥'
}
class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit    # Масть карты
    def to_str(self):  # возвращает строковое представление карты в виде строки, формата:4♦
        return f"{self.value}{SUITS_UNI[self.suit]}"
    def equal_suit(self, other_card):   # .**equal_suit**(card) - проверяет, одинаковые ли масти у карт \
        return True if self.suit == other_card.suit else False

    def more(self, other_card):  # .more(card) - возвращает True, если карта у которой вызван метод больше, чем карта которую передали в качестве параметра.
        if VALUES.index(self.value) > VALUES.index(other_card.value):  # Если у карты больше(старше) значение, то она больше(старше).
            return True
        elif VALUES.index(self.value) == VALUES.index(other_card.value): # При равенстве значений, сравниваем масти.
            return True if SUITS.index(self.suit) > SUITS.index(other_card.suit) else False #Старшинство мастей определяем следующее: ♠<♣<♦<♥
        else:
            return False

    def less(self, other_card): # .less(card) - проверяет является ли карта младше, чем карта в параметре
        return not self.more(other_card)

# # # Создадим несколько карт
card1 = Card("10", "Hearts")
card2 = Card("A", "Diamonds")
card3 = Card("10", "Hearts")

# Выведем карты на экран в виде: 10♥ и A♦
#print(card1.to_str(), type(card2.to_str()))
#print(card1.equal_suit(card2), type(card1.equal_suit(card2)))
# # Проверим, одинаковые ли масти у карт
#if card1.equal_suit(card2):
#     print(f"У карт: {card1.to_str()} и {card2.to_str()} одинаковые масти")
#else:
#     print(f"У карт: {card1.to_str()} и {card2.to_str()} разные масти")
#Пример:
card1 = Card("J", "Diamonds")
card2 = Card("2", "Diamonds")
#print(card1.more(card2)) # → True, при card1(J♦) card2(10♦). Валет больше(старше) 10-ки
#print(card1.less(card2))

card1 = Card("10", "Diamonds")
card2 = Card("10", "Spades")
card1.more(card2) # → False, при card1(4♦) card2(10♦). 4-ка не старше 10-ки
#print(card1.more(card2))
#print(card1.less(card2))


#print('\u2661', '\u2665')
#print('\u2662', '\u2666')
#print('\u2667', '\u2663')
#print('\u2664', '\u2660')
