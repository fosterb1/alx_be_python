# daily_reminder.py

# Prompt user for input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process based on priority using match-case
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"
    case _:
        reminder = f"'{task}' has an unknown priority level"

# Check if task is time-sensitive
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder = f"Note: {reminder}. Consider completing it when you have free time."

# Corrected print statement
print(f"Reminder: {reminder}")
