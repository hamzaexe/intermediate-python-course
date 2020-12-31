import random

 

def main():

  dice_sum=0
  team_score=[]
  #Setting number of players
  player_numbers=int(input('how many player you want? '))
  team_names=[]

  #Setting team name of player
  for i in range(0,player_numbers):
  
    team_name=str(input(f'enter {i+1} player team name'))
    team_names.append(team_name)

  #getting number of dice and sides of dice  
  dice_rolls=int(input('how many dice you want to roll? '))
  dice_size=int(input('how many sides you want for dice '))

  #setting team for rolling a dice
  for tnum in range(0,len(team_names)):
    print(f'TEAM {team_names[tnum]} rolling a dice')
    dice_sum=0

  #dice rolling and sum of dices
    for i in range(0,dice_rolls):

      roll=random.randint(1,dice_size)
      
      dice_sum+=roll
      if roll==1:
        print(f'you rolled a {roll} critical fail')
      elif roll==dice_size:
        print(f'you rolled a {roll} critical success')
      else:
        print(f'You rolled a {roll}')
    
    print(f'total sum of dice of team {team_names[tnum]} is {dice_sum}')

if __name__== "__main__":
  main()