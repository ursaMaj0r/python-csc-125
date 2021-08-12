RULES = {
  ('scissors', 'scissors') : 'Tie',
  ('scissors', 'paper'): 'Scissors cut Paper',
  ('scissors', 'rock'): 'Rock breaks Scissors',
  ('scissors', 'lizard'): 'Scissors decapitate Lizard',
  ('scissors', 'spock'): 'Spock melts Scissors',
  ('paper', 'scissors'): 'Scissors cut Paper',
  ('paper', 'paper'): 'Tie',
  ('paper', 'rock'): 'Paper covers Rock',
  ('paper', 'spock'): 'Paper disproves Spock',
  ('paper', 'lizard'): 'Lizard eats Paper',
  ('rock', 'scissors'): 'Rock breaks Scissors',
  ('rock', 'paper'): 'Paper covers Rock',
  ('rock', 'rock'): 'Tie',
  ('rock', 'lizard'): 'Rock crushes Lizard',
  ('rock', 'spock'): 'Spock vaporizes Rock',
  ('lizard', 'spock'): 'Lizard poisons Spock',
  ('lizard', 'paper'): 'Lizard eats Paper',
  ('lizard', 'rock'): 'Rock crushes Lizard',
  ('lizard', 'scissors'): 'Scissors decapitate Lizard',
  ('lizard', 'lizard'): 'Tie',
  ('spock', 'scissors'): 'Spock melts Scissors',
  ('spock', 'rock'): 'Spock vaporizes Rock',
  ('spock', 'paper'): 'Paper disproves Spock',
  ('spock', 'lizard'): 'Lizard poisons Spock',
  ('spock', 'spock'): 'Tie'
}

hand_1 = input('Hand 1: ')
hand_2 = input('Hand 2: ')

print(RULES[(hand_1,hand_2)])








