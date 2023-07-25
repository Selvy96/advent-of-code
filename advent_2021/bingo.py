from main import read_input

def create_bingo_cards(bingo_cards):
    cards = []
    while len(bingo_cards) > 0:
        card = []
        if len(bingo_cards) >= 6:
            for num in range(6):
                bingo_cards[0] = bingo_cards[0].strip()
                card.append(bingo_cards[0])
                bingo_cards.pop(0)
        else:
            for num in range(len(bingo_cards)):
                bingo_cards[0] = bingo_cards[0].strip()
                card.append(bingo_cards[0])
                bingo_cards.pop(0)
        cards.append(card)
    return cards


def create_card_numbers(cards):
    new_cards = []
    for card in cards:
        new_card = []
        if len(card) == 6:
            card.remove(card[5])
        for row in card:
            row = row.split(" ")
            row = [x for x in row if x]
            new_card.append(row)
        new_cards.append(new_card)
    return new_cards


def create_bingo_call_list(bingo_calls):
    new_bingo_calls = bingo_calls[0].split(",")
    return new_bingo_calls


def play_bingo(bingo_calls, cards):
    for call in bingo_calls:
        for card in cards:
            for i in range(len(card)):
                if call in card[i]:
                    card[i].remove(call)
                if len(card[i]) == 0:
                    result = [call, card]
                    return result


def bingo_score(result):
    call = result[0]
    card = result[1]
    card_total = 0
    for row in card:
        for i in range(len(row)):
            card_total += int(row[i])
    total = card_total * int(call)
    print(total)

def find_losing_card(bingo_calls, cards):
    count = 0
    for call in bingo_calls:
        print(call)
        for card in cards:
            print(card)
            if card != ["x"]:
                for i in range(len(card)):
                    if call in card[i]:
                        card[i].remove(call)
                    if len(card[i]) == 0:
                        count += 1
                        if count != 2:
                            card = ["x"]
                        else:
                            result = [call, card]
                            return result
                    print(card)
            print(card)


if __name__ == "__main__":
    bingo_calls = read_input("bingo_calls.txt")
    #bingo_cards = read_input("bingo_cards.txt")
    #cards = create_bingo_cards(bingo_cards)
    #cards = create_card_numbers(cards)
    bingo_calls = create_bingo_call_list(bingo_calls)
    #result = play_bingo(bingo_calls, cards)
    #bingo_score(result)
    #print(find_losing_card(bingo_calls, cards))
    #print(bingo_score(losing_result))

    bingo_cards = read_input("bingo_cards2.txt")
    cards = create_bingo_cards(bingo_cards)
    cards = create_card_numbers(cards)
    losing_card = find_losing_card(bingo_calls, cards)
    # score = bingo_score(losing_card)
    print(losing_card)



