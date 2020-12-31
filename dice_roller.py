import random
dice_rolls=2

  

def main():
  dice_sum=0
  for i in range(0,dice_rolls):

    roll=random.randint(1,6)
    dice_sum+=roll
    print('You rolled a',roll)
    
  print('total sum of dice',dice_sum)
if __name__== "__main__":
  main()