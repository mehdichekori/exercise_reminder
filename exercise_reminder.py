import csv
import time
import random

from win10toast import ToastNotifier

PREFERENCES_FILE = 'exercise_preferences.csv'

"""
Sends a Windows notification to remind the user to perform an exercise.

Args:
- exercise: The type of exercise to be performed (e.g., squats, push-ups).
- count: The quantity of exercises to be done.

Uses the win10toast library to display a notification for the specified exercise and count.
"""
def send_notification(exercise, count):
    toaster = ToastNotifier()
    message = f"Time to do {count} {exercise}!"
    toaster.show_toast("Take a break!", message, duration=10)


"""
Retrieves exercise preferences stored in a CSV file.

Reads exercise preferences from the PREFERENCES_FILE (CSV) and returns a list of dictionaries
containing exercise, quantity, and notify status.
"""
def get_exercise_preferences():
    exercise_prefs = []
    try:
        with open(PREFERENCES_FILE, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                exercise_prefs.append({'exercise' : row[0],'quantity': row[1],'notify' : row[2]})
    except FileNotFoundError:
        pass
    return exercise_prefs

"""
Saves exercise preferences to a CSV file.

Writes exercise preferences (exercise, quantity, notify status) to the PREFERENCES_FILE (CSV).
"""
def save_exercise_preferences(exercise_prefs):
    with open(PREFERENCES_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        for preference in exercise_prefs:
            writer.writerow([preference['exercise'], preference['quantity'], preference['notify']])

"""
Prints exercise preferences to the console.

Displays exercise details (exercise, quantity, notify status) from the provided list of dictionaries.
"""       
def print_exercise_preferences(exercise_preferences):
    print("Your exercise preferences:")
    for preference in exercise_preferences:
        print(f"{preference['exercise'].capitalize()}: Quantity : {preference['quantity']}, Notify you? - {preference['notify']}")
    print("")


"""
Manages exercise preferences, allows modification, and triggers notifications based on preferences.

- Retrieves exercise preferences.
- Displays current preferences and provides an option to modify.
- Modifies exercise preferences based on user input.
- Triggers exercise notifications based on a probability (1/5 chance per hour).
"""
def test_notification_with_preferences():

    exercise_preferences = get_exercise_preferences()
    print_exercise_preferences(exercise_preferences)

    if exercise_preferences:

        response = input(f"Do you want to modify your settings? ([Y]es/[n]o): ").lower()

        if response == 'yes' or response == 'y' or response =='':      
    
            exercises = ['squats', 'push-ups', 'crunches']

            for exercise in exercises:

                response = input(f"Do you want to be notified for {exercise}? ([Y]es/[n]o): ").lower()

                if response == 'yes' or response == 'y' or response =='':
                    for pref in exercise_preferences:
                        if pref['exercise'] == exercise:
                            pref['notify'] = True
                            count = int(input(f"How many {exercise} would you like to do? Enter a number: "))
                            pref['quantity'] = count
                            break
                else:
                    for pref in exercise_preferences:
                        if pref['exercise'] == exercise:
                            pref['notify'] = False
                            break



            save_exercise_preferences(exercise_preferences)
            print_exercise_preferences(exercise_preferences)

    print("Starting script")        

    while True:
            # Generate a random number between 1 and 5
            random_number = random.randint(1, 5)
            
            if random_number == 1:
                # Get a list of exercises from the preferences
                exercises = list(exercise_preferences.keys())
                # Generate a random exercise from the list
                random_exercise = random.choice(exercises)

                # Trigger a notification for the randomly selected exercise
                send_notification(random_exercise, exercise_preferences[random_exercise])
                
            
            # Wait for an hour before checking the probability again
            time.sleep(3600)  # 3600 seconds = 1 hour

# Run the test notification function with exercise preferences
test_notification_with_preferences()



