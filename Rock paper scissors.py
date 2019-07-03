print ('User A: Rock, Paper, or Scissors?')
usera = input()
print ('User B: Rock, Paper, or Scissors?')
userb = input()

while usera.lower() == 'rock':
    if userb.lower() == 'paper':
        print ('User B wins! Congratulations to you!')
    elif userb.lower() == 'scissors':
        print ('User A wins! Congratulations to you!')
    elif userb.lower() == 'rock':
        print ('Tie! Try again next time')
    else:
        print ('''Please try again! We can't read your decision''')
    break
while usera.lower() == 'paper':
    if userb.lower() == 'rock':
        print ('User A wins! Congratulations to you!')
    elif userb.lower() == 'scissors':
        print ('User B wins! Congratulations to you!')
    elif userb.lower() == 'paper':
        print ('Tie! Try again next time')
    else:
        print ('''Please try again! We can't read your decision''')
    break
while usera.lower() == 'scissors':
     if userb.lower() == 'rock':
        print ('User B wins! Congratulations to you!')
     elif userb.lower() == 'paper':
        print ('User A wins! Congratulations to you!')
     else:
        print ('Tie! Try again next time')
     break
  
