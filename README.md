# Exercise Reminder Script

This Python script generates notifications to remind the user to perform exercises at specified intervals. It allows the user to set exercise preferences, including the type of exercise, the quantity, and whether to receive notifications for each exercise.

## Features

- Set exercise preferences: Choose exercises (e.g., squats, push-ups, crunches), specify the quantity, and opt-in/out of receiving notifications for each exercise.
- Receive timely reminders: Based on preferences, the script generates notifications at set intervals for the chosen exercises.

## How to Run

1. **Clone the repository:**

    ```bash
    git clone https://github.com/mehdichekori/exercise-reminder.git
    cd exercise-reminder
    ```

2. **Install dependencies:**

    Ensure you have Python (version 3.11.2 or higher) installed. Install the required dependencies using pip and the provided `requirements.txt` file:

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the script:**

    Execute the script `exercise_reminder.py`:

    ```bash
    python exercise_reminder.py
    ```

## Usage

- On running the script, follow the prompts to specify exercise preferences.
- Notifications will be generated based on the specified exercise preferences at set intervals.

## File Structure

- `exercise_reminder.py`: Main script file
- `exercise_preferences.csv`: CSV file to store exercise preferences
- `requirements.txt`: text file that contains the project dependencies

## Contributing

Contributions are welcome! If you have suggestions or improvements, feel free to submit a pull request.


## Future Features

- [ ] Completition tracker - Add a way to mark exercise as completed or skipped.
- [ ] Daily stats - How many X reps of X exercise were completed on each day.
- [ ] Available Hours - When does the script notify you?
- [ ] Calories calculator - Calculate calories burnt based on Age, Height, Weight, etc.
- [ ] Progressive overload - Gradually increase rep count over time.
- [ ] Phone notifications - Get a popup notification on your phone.

## License

This project is licensed under the [MIT License](LICENSE).
