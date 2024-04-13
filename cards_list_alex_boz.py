#class Card:
#    pass
    # TODO: сюда копируем реализацию класса карты из предыдущего задания
import card_alex_boz as card

# TODO-1: добавьте в список hearts_cards все червовые карты(от 2-ки до туза)
hearts_cards = [card.Card(x,'Hearts') for x in card.VALUES]

# TODO-2: добавьте в список diamonds_cards все бубновые карты(от туза до 2-ки)
diamonds_cards = [card.Card(x,'Diamonds') for x in card.VALUES]

# TODO-3: выведите все карты из списка hearts_cards в терминал через запятую в одну строку:
# Пример вывода: 2♥, 3♥, 4♥ ... A♥
print(*([n.to_str() for n in hearts_cards]),sep=",")
print(*([n.to_str() for n in diamonds_cards]),sep=",")

