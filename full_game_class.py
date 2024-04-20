from deck_total import Card, Deck, SUITS_UNI
#Cоздадим имитацию ходов в “Дурака без козырей”:
class Hand:
    def __init__(self, deck):
        self.hand = deck[:10]

    def __str__(self) -> str:
        return f'hand[{len(self.hand)}]: {", ".join([str(card) for card in self.hand])}'

    def show(self) -> None:
        print(self)

    def __getitem__(self, item):
        return self.hand.__getitem__(item)

    def attack_card_func(self):
        if len(self.hand) > 0:
            attack_card = min(self.hand)
            return attack_card
    def beat_card_func(self, attack_card):
        rep = sorted([card for card in self.hand if card.suit == attack_card.suit])
        if len(rep) > 0:
            for beat_card in rep:
                if beat_card > attack_card:
                    return beat_card
    def add_card_func(self, attack_card):
        rep = sorted([card for card in self.hand if card.suit == attack_card.suit])
        if len(rep) > 0:
            for add_card in rep:
                return add_card

    def remove(self, attack_card):
        self.hand.remove(attack_card)

    def extend(self, table):
        self.hand.extend(table)

    def len(self):
        return len(self.hand)

deck = Deck()
deck.shuffle()
Player_1 = Hand(deck)
deck.delete(10)
Player_2 = Hand(deck)
deck.delete(10)

attack = 'begin'
table = []

while min(Player_1.len(), Player_2.len()) > 0:

    for hand in Player_1, Player_2:
        print(f'{"Player_1" if hand == Player_1 else "Player_2"} {hand}')
        #print(f'attack: {attack}')
        #print(f'table: {table}')
        #print(f'len {hand.len()}')

        if attack == 'begin':
            if hand.len() > 0:
                attack_card = hand.attack_card_func()
                print(f'Хожу: {attack_card}')
                hand.remove(attack_card)
                table.append(attack_card)
                attack = 'answer'

        elif attack == 'add':
                if hand.add_card_func(attack_card) is not None:
                    attack_card = hand.add_card_func(attack_card)
                    print(f'Подбрасываю: {attack_card}')
                    hand.remove(attack_card)
                    table.append(attack_card)
                    attack = 'answer'

                else:
                    print(f'Подбрасывать нечего : {SUITS_UNI[attack_card.suit]} нет')
                    table = []
                    attack = 'begin'

        elif attack == 'answer':

            if hand.beat_card_func(attack_card) is not None:
                beat_card = hand.beat_card_func(attack_card)
                print(f'Отбиваю: {beat_card}')
                hand.remove(beat_card)
                table.append(beat_card)
                attack = 'add'

            else:
                print(f'Не могу отбить и забираю себе карты: {table}')
                hand.extend(table)
                attack = 'begin'
                table = []

print(f'Player_1: {Player_1}')
print(f'Player_2: {Player_2}')
if Player_1.len():
    print(f'Победил: Player_2')
else:
    print(f'Победил: Player_1')
