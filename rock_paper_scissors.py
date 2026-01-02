import random

print("🎮 Rock-Paper-Scissors Game 🎮")
print("0 → Rock")
print("1 → Paper")
print("2 → Scissors")

# User input
try:
    user_choice = int(input("Enter your choice (0/1/2): "))
except ValueError:
    print("Invalid input! Please enter a number (0, 1, or 2).")
    exit()

choices = ["Rock", "Paper", "Scissors"]
computer_choice = random.choice([0, 1, 2])

# Display choices
if user_choice in [0, 1, 2]:
    print(f"You picked: {choices[user_choice]}")
else:
    print("❌ Invalid choice!")
    exit()

print(f"Computer picked: {choices[computer_choice]}")

# Decide winner
if (user_choice == 0 and computer_choice == 2) or \
   (user_choice == 1 and computer_choice == 0) or \
   (user_choice == 2 and computer_choice == 1):
    print("🎉 You won!")
elif user_choice == computer_choice:
    print("😎 It's a draw!")
else:
    print("💻 Computer won!")
