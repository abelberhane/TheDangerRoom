# Background
# In this project, students use Python to create a program that creates a vote count of Thanksgiving pies. They will use functions, loops, and if-else statements.

# Complete the following tasks:
# 1. Ask for the number of people coming to Thanksgiving dinner
# 2. Ask for the number of votes for each pie type
# 3. Continually ask the user for the number of votes for each pie type until a viable value is found
# 4. A check_votes function will be used to check that the number of votes given is acceptable based on the number of people attending dinner
# 5. Update the number of votes for each pie type as well as the number of total votes from guests
# 5. Print the votes for each pie type, the total vote count, and the number of people who did not vote


# Ask for the number of people coming to Thanksgiving dinner
guest_count=int(input("How many people are coming to Thanksgiving dinner: "))

# Ask for the number of votes for each pie type
# Continually ask the user for the number of votes for each pie type until a viable value is found
apple_pie_count=int(input("How many people are voting for Apple Pie: "))
  # This is where I verify if all guests have voted
  # If the number of people who voted for apple pie is the same as the total number of guests, set the final pie count equal to apple pie votes
  if apple_pie_count==guest_count:
    final_pie_count=apple_pie_count
  else:
    apple_pie_count=current_pie_count
pumpkin_pie_count=int(input("How many people are voting for Pumpkin Pie: "))
  # If the number of people who voted for pumpkin and apple pie is the same as the total number of guests, set the final pie count equal to sum of both pie votes
  if apple_pie_count + pumpkin_pie_count==guest_count:
    final_pie_count=(apple_pie_count + pumpkin_pie_count)
  else:
    (apple_pie_count + pumpkin_pie_count)=current_pie_count
pecan_pie_count=int(input("How many people are voting for Pecan Pie: "))
  # Same logic as above
  if pecan_pie_count + apple+pie_count + pumpkin_pie_count==guest_count:
      final_pie_count=(apple_pie_count + pumpkin_pie_count + pecan_pie_count)
  else:
    (apple_pie_count + pumpkin_pie_count + pecan_pie_count)=current_pie_count
key_lime_pie_count=int(input("How many people are voting for Key Lime Pie: "))
  # Same logic as above
  if key_lime_pie + pecan_pie_count + apple+pie_count + pumpkin_pie_count==guest_count:
      final_pie_count=(key_lime_pie + pecan_pie_count + apple+pie_count + pumpkin_pie_count)
  else:
    (key_lime_pie + pecan_pie_count + apple+pie_count + pumpkin_pie_count)=current_pie_count
chocolate_pie_count=int(input("How many people are voting for Chocolate Pie: "))
  # Same logic as above
  if chocolate_pie_count + key_lime_pie_count + pecan_pie_count + apple+pie_count + pumpkin_pie_count==guest_count:
      final_pie_count=(chocolate_pie_count + key_lime_pie + pecan_pie_count + apple+pie_count + pumpkin_pie_count)
  else:
    (chocolate_pie_count + key_lime_pie + pecan_pie_count + apple+pie_count + pumpkin_pie_count)=current_pie_count

# A check_votes function will be used to check that the number of votes given is acceptable based on the number of people attending dinner
# There should be some logic here to skip the next pie questions based on if we have met the total guest count of votes
# def check_votes():
  
# Here I can work on the non_voters variable 
non_voters=int(guest_count - final_pie_count)

# Update the number of votes for each pie type as well as the number of total votes from guests
# Print the votes for each pie type, the total vote count, and the number of people who did not vote
print("The number of people who voted for Apple Pie is:",apple_pie_count)
print("The number of people who voted for Pumpkin Pie is:",pumpkin_pie_count)
print("The number of people who voted for Pecan Pie is:",pecan_pie_count)
print("The number of people who voted for Key Lime Pie is:",key_lime_pie_count)
print("The number of people who voted for Chocolate Pie is:",chocolate_pie_count)

# This is where I print the total number of votes
print("The total vote count is:",final_pie_count)

# This is where we display the people who did not vote. Can use non_voters later.
print("The number of people who did not vote is:",(non_voters)
