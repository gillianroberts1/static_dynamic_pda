### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:

#when checking for equality, the comparison operator '==' should be used instead of the assignment operator '='
#There is a syntax error ':' is missing from the end of the else statement
  def check_for_ace(self, card):
    if card.value = 1:
      return True
    else
      return False
   
# there is a typo error with 'dif' this should read'def'
# there is a comma missing after the parameter card1
# the return statment is incorrect on line 33 as 'card' has not been passed in. It should read 'card1'
# the indentaion is incorrect starting from line 32
  dif highest_card(self, card1 card2):
  if card1.value > card2.value:
    return card
  else:
    return card2
  

#total is undefined. it shoudl be initialised as = 0
# the return statement is indented incorrectly, it should be outside the for loop
# the method is not indented correctly
#the string you have a total of need a space at the end and +total requires to be +str(total)
def cards_total(self, cards):
  total
  for card in cards:
    total += card.value
    return "You have a total of" + total
  
```
