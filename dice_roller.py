import random
dice_rolls=int(input('how many dice you want to roll? '))
dice_size=int(input('how many sides you want for dice '))
  

def main():
  dice_sum=0
  for i in range(0,dice_rolls):

    roll=random.randint(1,dice_size)
    dice_sum+=roll
    if roll==1:
      print(f'you rolled a {roll} critical fail')
    elif roll==dice_size:
      print(f'you rolled a {roll} critical success')
    else:
      print(f'You rolled a {roll}')
    
  print('total sum of dice',dice_sum)
if __name__== "__main__":
  main()