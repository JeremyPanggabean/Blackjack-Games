# import random modul for randomize cards
import random

# import logo from art file
from art import logo

CHIP_VALUES = {"1K": 1000, "3K": 3000, "5K": 5000, "10K": 10000}  # Chip denominations

def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw 🤝"
    elif c_score == 0:
        return "Lose, Computer has a Blackjack 😮"
    elif u_score == 0:
        return "You win with a Blackjack 😎"
    elif u_score > 21:
        return "You busted! You lose 😭"
    elif c_score > 21:
        return "Computer busted! You win 🤩"
    elif u_score > c_score:
        return "You win 🤫"
    else:
        return "You lose 😌"

def format_chips(chips):
    return f"{chips:,}".replace(",", ".")

def play_game(chips):
    print(logo)
    if chips <= 0:
        print("You have no more chips left! Game over.")
        return chips
    
    print(f"You have {format_chips(chips)} chips.")
    print(f"Available chip bets: {list(CHIP_VALUES.keys())}")
    bet = 0
    while bet == 0:
        bet_input = input("Choose your bet (1K, 3K, 5K, 10K): ").upper()
        if bet_input in CHIP_VALUES and CHIP_VALUES[bet_input] <= chips:
            bet = CHIP_VALUES[bet_input]
        else:
            print("Invalid input or insufficient chips. Please enter a valid chip amount.")
    
    user_cards = [deal_card(), deal_card()]
    computer_cards = [deal_card(), deal_card()]
    is_game_over = False
    
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")
        
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True
    
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    result = compare(user_score, computer_score)
    print(result)
    
    # Comparison case sensitive
    if "win" in result.lower():
        chips += bet
    elif "lose" in result.lower():
        chips -= bet
    
    print(f"You now have {format_chips(chips)} chips.")
    return chips


chips = 10000  # Player starts with 10K chips
while True:
    play_again = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if play_again != 'y':
        break
    print("\n" * 30)
    chips = play_game(chips)
    if chips < 1000:
        print("Your chips are below 1K. Resetting to 10K chips.")
        chips = 10000

print("Thank you for playing Blackjack! 🎉")