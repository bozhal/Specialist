#class Card:
#    pass
    # TODO: сюда копируем реализацию класса карты из предыдущего задания
import card_alex_boz as card

cards = []
# TODO-1: в список cards добавьте ВСЕ карты всех мастей
for suit in card.SUITS:
    for value in card.VALUES:
        cards.append(card.Card(value, suit))

# TODO-2: Выведите карты в формате: cards[кол-во]2♣, ..., A♣, 2♠,...,A♠, 2♦, ... A♦, 2♥, 3♥, 4♥ ... A♥
print(*([n.to_str() for n in cards]),sep=",")
print(len(cards))