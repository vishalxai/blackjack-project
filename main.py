import random
from art import logo

def deal_card():
    """Return a random card from the deck ."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)
def calculate_score(cards):
    """Take a list of cards and return the total score."""
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score,computer_score):
    """Compares scores and return the game result ."""
    if user_score >21 and computer_score >21 :
        return "you both went over you both lose "
    if user_score == computer_score :
        return "Draw"
    elif computer_score==0:
        return "Lose,dealer has blackjack "
    elif user_score==0:
        return "win,you have the blackjack "
    elif user_score>21:
        return "You lose,you went over "
    elif computer_score>21:
        return "You win ,computer went over "
    elif user_score > computer_score:
        return "you win "
    else:
        return "you lose "

def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    game_over = False

    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"   Your cards: {user_cards}, current score: {user_score}")
        print(f"   Dealer's first card: {computer_cards[0]}")

        if user_score==0 or computer_score ==0 or user_score >21:
            game_over = True
        else:
            user_should_deal = input("Type 'y',to get another card , 'n' to pass:")
            if user_should_deal =="y":
                user_cards.append(deal_card())
            else:
                game_over= True
    #dealer turn must hit untill score reaches >=17
    while computer_score != 0 and computer_score <17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"your final hand :{user_cards},final score:{user_score}")
    print(f"Dealers final hand :{computer_cards},final score :{computer_score}")
    print(compare(user_score,computer_score))

while input ("Do you want to play a game of blckjack ? Type 'y' or 'n': ") =="y":
    play_game()