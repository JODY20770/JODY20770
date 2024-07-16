import time
import random

def introduction():
    """Introduce the game to the player."""
    print('Welcome to the Haunted Mansion Adventure Game!')
    print('You find yourself in a creepy old mansion, and your goal is to find the hidden treasure.')
    time.sleep(2)

def choose_path():
    """Ask the player to choose a path."""
    print('\nYou come to a fork in the hallway. Do you want to go left, right, or straight ahead?')
    print('1: Left')
    print('2: Right')
    print('3: Straight ahead')
    choice = input('Enter 1, 2, or 3: ')
    return choice

def encounter():
    """Randomly determine what the player encounters."""
    events = [
        'a ghost', 
        'a friendly spirit', 
        'a hidden trapdoor', 
        'a creepy doll', 
        'an old mirror'
    ]
    encounter_event = random.choice(events)
    print(f'\nYou encounter {encounter_event}!')
    time.sleep(2)
    return encounter_event

def handle_encounter(encounter_event, score):
    """Handle the outcome of an encounter and update the score."""
    if encounter_event == 'a ghost':
        print('The ghost scares you and you lose some sanity.')
        score -= 10
    elif encounter_event == 'a friendly spirit':
        print('The spirit gives you some helpful advice.')
        score += 10
    elif encounter_event == 'a hidden trapdoor':
        print('You fall through a trapdoor and lose some health.')
        score -= 20
    elif encounter_event == 'a creepy doll':
        print('The doll gives you a fright, but you manage to keep your cool.')
        score -= 5
    elif encounter_event == 'an old mirror':
        print('The mirror shows you a vision of the treasure, boosting your morale.')
        score += 15
    return score

def additional_choice():
    """Ask the player to make an additional choice."""
    print('\nYou find a mysterious door. Do you want to open it?')
    print('1: Yes')
    print('2: No')
    choice = input('Enter 1 or 2: ')
    return choice

def handle_additional_choice(choice, score):
    """Handle the outcome of an additional choice."""
    if choice == '1':
        print('You open the door and find a hidden stash of gold!')
        score += 20
    elif choice == '2':
        print('You decide not to open the door and move on.')
        score += 0
    return score

def check_win_lose(score):
    """Check if the player has won or lost."""
    if score <= 0:
        print('\nYour sanity is too low. You lose!')
        return True
    elif score >= 70:
        print('\nCongratulations! You found the hidden treasure and win the game!')
        return True
    return False

def play_again():
    """Ask the player if they want to play again."""
    choice = input('\nDo you want to play again? (yes or no): ')
    return choice.lower() == 'yes'

def main():
    """Main function to run the game."""
    introduction()
    
    while True:
        score = 20  # Initial score
        game_over = False
        
        while not game_over:
            choice = choose_path()
            if choice not in ['1', '2', '3']:
                print('Invalid input. Please enter 1, 2, or 3.')
                continue

            encounter_event = encounter()
            score = handle_encounter(encounter_event, score)
            print(f'Current score: {score}')
            
            if not game_over:
                extra_choice = additional_choice()
                if extra_choice not in ['1', '2']:
                    print('Invalid input. Please enter 1 or 2.')
                    continue
                score = handle_additional_choice(extra_choice, score)
                print(f'Current score: {score}')
            
            game_over = check_win_lose(score)
        
        if not play_again():
            break

    print('Thanks for playing!')

# Start the game
if __name__ == '__main__':
    main()
