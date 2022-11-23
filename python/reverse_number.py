# reverse_number.py

# Take in the user input while giving directions
user_input=int(input("Enter the number to reverse: "))
_rev=0
while(user_input>0):
  # store it as a variale
  dig=user_input%10
  # reverse it!
  _rev=_rev*10+dig
  user_input=user_input//10
  # Here we write the reversed number back
print("The reversed number is :",_rev)
