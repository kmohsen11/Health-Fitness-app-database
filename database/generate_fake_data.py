import sqlite3
from faker import Faker
import random
from datetime import datetime, timedelta

# Initialize Faker
fake = Faker()

# Connect to the SQLite database
conn = sqlite3.connect("health_fitness_app.db")
cursor = conn.cursor()

# Generate and insert fake data into Users table
for _ in range(100):
    username = fake.user_name()
    age = random.randint(18, 70)
    gender = random.choice(["Male", "Female"])
    weight = round(random.uniform(100, 300), 2)
    height = round(random.uniform(4.5, 7.0), 2)
    contact_info = fake.email()

    cursor.execute(
        "INSERT INTO Users (UserName, Age, Gender, Weight, Height, ContactInfo) VALUES (?, ?, ?, ?, ?, ?)",
        (username, age, gender, weight, height, contact_info),
    )

# Generate and insert fake data into ExerciseLogs table
for user_id in range(1, 101):
    for _ in range(10):
        exercise_type = fake.random_element(elements=("Running", "Swimming", "Strength Training", "Cycling"))
        duration_minutes = random.randint(10, 120)
        intensity = fake.random_element(elements=("Low", "Moderate", "High"))
        date_time = fake.date_time_between(
            start_date="-1y", end_date="now", tzinfo=None
        ).strftime("%Y-%m-%d %H:%M:%S")
        calories_burned = round(random.uniform(100, 600), 2)
        distance_covered = round(random.uniform(0.5, 10.0), 2)
        heart_rate = random.randint(80, 200)
        weight_lifted_lbs = round(random.uniform(0, 300), 2)

        cursor.execute(
            "INSERT INTO ExerciseLogs (UserID, ExerciseType, DurationMinutes, Intensity, DateTime, CaloriesBurned, DistanceCovered, HeartRate, WeightLiftedLbs) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (user_id, exercise_type, duration_minutes, intensity, date_time, calories_burned, distance_covered, heart_rate, weight_lifted_lbs),
        )

# Generate and insert fake data into GoalsAndProgress table
for user_id in range(1, 101):
    for _ in range(5):
        goal_type = fake.random_element(elements=("Weight Loss", "Muscle Gain", "General Fitness"))
        goal_value = round(random.uniform(5, 50), 2)
        progress_value = round(random.uniform(0, goal_value), 2)

        cursor.execute(
            "INSERT INTO GoalsAndProgress (UserID, GoalType, GoalValue, ProgressValue) VALUES (?, ?, ?, ?)",
            (user_id, goal_type, goal_value, progress_value),
        )

# Generate and insert fake data into HealthMetrics table
for user_id in range(1, 101):
    for _ in range(5):
        weight = round(random.uniform(100, 300), 2)
        waist_circumference = round(random.uniform(20, 50), 2)
        hip_circumference = round(random.uniform(20, 60), 2)
        body_fat_percentage = round(random.uniform(5, 30), 2)
        muscle_mass = round(random.uniform(20, 80), 2)
        blood_pressure = f"{random.randint(90, 140)}/{random.randint(60, 90)}"
        step_count = random.randint(1000, 20000)

        cursor.execute(
            "INSERT INTO HealthMetrics (UserID, Weight, WaistCircumference, HipCircumference, BodyFatPercentage, MuscleMass, BloodPressure, StepCount) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            (user_id, weight, waist_circumference, hip_circumference, body_fat_percentage, muscle_mass, blood_pressure, step_count),
        )

# Generate and insert fake data into NutritionLogs table
for user_id in range(1, 101):
    for _ in range(5):
        meal_name = fake.random_element(elements=("Breakfast", "Lunch", "Dinner", "Snack"))
        food_items = fake.sentence(nb_words=6)
        meal_time = fake.date_time_between(
            start_date="-1y", end_date="now", tzinfo=None
        ).strftime("%Y-%m-%d %H:%M:%S")

        cursor.execute(
            "INSERT INTO NutritionLogs (UserID, MealName, FoodItems, MealTime) VALUES (?, ?, ?, ?)",
            (user_id, meal_name, food_items, meal_time),
        )

# Generate and insert fake data into SleepData table
for user_id in range(1, 101):
    for _ in range(5):
        sleep_duration_minutes = random.randint(240, 540)
        sleep_quality_rating = random.randint(1, 5)
        sleep_start_time = fake.date_time_between(
            start_date="-1y", end_date="now", tzinfo=None
        ).strftime("%H:%M:%S")
        sleep_end_time = (datetime.strptime(sleep_start_time, "%H:%M:%S") + timedelta(minutes=sleep_duration_minutes)).strftime("%H:%M:%S")

        cursor.execute(
            "INSERT INTO SleepData (UserID, SleepDurationMinutes, SleepQualityRating, SleepStartTime, SleepEndTime) VALUES (?, ?, ?, ?, ?)",
            (user_id, sleep_duration_minutes, sleep_quality_rating, sleep_start_time, sleep_end_time),
        )

# Generate and insert fake data into UserPreferences table
for user_id in range(1, 101):
    fitness_goal = fake.random_element(elements=("Lose Weight", "Build Muscle", "General Fitness"))
    dietary_restrictions = fake.sentence(nb_words=6)
    preferred_exercises = fake.sentence(nb_words=12)

    cursor.execute(
        "INSERT INTO UserPreferences (UserID, FitnessGoal, DietaryRestrictions, PreferredExercises) VALUES (?, ?, ?, ?)",
        (user_id, fitness_goal, dietary_restrictions, preferred_exercises),
    )

# Commit and close the database connection
conn.commit()
conn.close()
