# reverse_number.py
# This small python example is a combination of a couple scripts. You can find part of this example here: 
# https://www.scaler.com/topics/reverse-a-number-in-python/
# And Example 2 here, https://www.fosslinux.com/46256/python-script-examples.htm

# The variable user_input is the int value of the input to the question "Enter the number to reverse"
user_input=int(input("Enter the number to reverse: "))

# Creating the variable we will use for the final reversed number
reversed_num=0

# Creating a while loop to run until we have removed every number in user_input. Every iteration of the loop removes a number. As each number is removed from user_input, it is added to the new reversed variable, _rev
while(user_input>0):
  
  # Taking the modulo with 10 gives us the last number in user_input and we assign it into a new variable called current_number_being_extracted
  current_number_being_extracted=user_input%10
  
  # Takes the current number being extracted and adds it to the reversed number. We make sure it is at the end by multiplying everything by 10 and then adding the current number.
  reversed_num=reversed_num*10+current_number_being_extracted
  
  # Removes the last digit from user_input by dividing it by 10
  user_input=user_input//10
  
  # Show the final reversed number to the user
print("The reversed number is :",reversed_num)
