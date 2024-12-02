"""
write a problem that prompts the user to enter an integer for today's day of the week (Sunday is 0, Monday is 1,..., and Saturday is 6). Also, prompt the user to enter the number of days after today for a future day and display the future day of the week.
Here is a sample run:
Enter today's day: 1
Enter the number of days elapsed since today: 3
Today is Monday and the future day is Thursday

pseudocode
1. Match the day number to the corresponding day name
2. Get user input for today's day and days elapsed
3. Get today's day name
4. Calculate the future day
5. Get the future day name
"""

def get_day_name(week_days):
   
    match week_days:
        case 0:
            return "Sunday"
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4:
            return "Thursday"
        case 5:
            return "Friday"
        case 6:
            return "Saturday"

week_days = int(input("Enter today's day: "))
future_day = int(input("Enter the number of days elapsed since today: "))

today_day_name = get_day_name(week_days)
print(f"Today is: {today_day_name}")

future = (week_days + future_day) % 7

future_day_name = get_day_name(future)
print(f"The day after {future_day} days will be: {future_day_name}")
