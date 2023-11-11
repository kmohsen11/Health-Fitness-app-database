-- Query 1: Retrieve the user's exercise logs (type, duration, and calories burned) for UserID 1
SELECT 
    'Exercise Type: ' || ExerciseType || ', Duration: ' || DurationMinutes || ' minutes, Calories Burned: ' || CaloriesBurned
FROM ExerciseLogs
WHERE UserID = 1;

-- Query 2: Retrieve the user's goals and progress (type, goal value, and progress value) for UserID 1
SELECT 
    'Goal Type: ' || GoalType || ', Goal Value: ' || GoalValue || ', Progress Value: ' || ProgressValue
FROM GoalsAndProgress
WHERE UserID = 1;

-- Query 3: Count the number of goals for UserID 1
SELECT 
    'Number of Goals: ' || COUNT(*) AS NumberOfGoals
FROM GoalsAndProgress
WHERE UserID = 1;

-- Query 4: Retrieve the user's health metrics (weight, waist circumference, hip circumference, body fat percentage, muscle mass, blood pressure, and step count) for UserID 1
SELECT 
    'Weight: ' || Weight || ' kg, Waist Circumference: ' || WaistCircumference || ' cm, Hip Circumference: ' || HipCircumference || ' cm, Body Fat Percentage: ' || BodyFatPercentage || '%, Muscle Mass: ' || MuscleMass || ' kg, Blood Pressure: ' || BloodPressure || ', Step Count: ' || StepCount
FROM HealthMetrics
WHERE UserID = 1;

-- Query 5: Retrieve the user's nutrition logs (meal name, food items, and meal time) for UserID 1 on '2023-10-01'
SELECT 
    'Meal Name: ' || MealName || ', Food Items: ' || FoodItems || ', Meal Time: ' || MealTime
FROM NutritionLogs
WHERE UserID = 1
  AND DATE(MealTime) = '2023-10-01';

-- Query 6: Retrieve the user's sleep data (sleep duration, sleep quality rating, start time, and end time) for UserID 1
SELECT 
    'Sleep Duration: ' || SleepDurationMinutes || ' minutes, Sleep Quality Rating: ' || SleepQualityRating || ', Start Time: ' || SleepStartTime || ', End Time: ' || SleepEndTime
FROM SleepData
WHERE UserID = 1;

-- Query 7: Retrieve the user's preferences (fitness goal, dietary restrictions, and preferred exercises) for UserID 1
SELECT 
    'Fitness Goal: ' || FitnessGoal || ', Dietary Restrictions: ' || DietaryRestrictions || ', Preferred Exercises: ' || PreferredExercises
FROM UserPreferences
WHERE UserID = 1;

-- Query 8: Calculate the total duration of exercise (minutes) for UserID 1
SELECT 
    'Total Exercise Duration: ' || SUM(DurationMinutes) AS TotalExerciseDuration
FROM ExerciseLogs
WHERE UserID = 1;

-- Query 9: Calculate the average exercise intensity for UserID 1
SELECT 
    'Average Exercise Intensity: ' || AVG(Intensity) AS AverageExerciseIntensity
FROM ExerciseLogs
WHERE UserID = 1;

-- Query 10: Find the most frequent exercise type for UserID 1
SELECT 
    'Most Frequent Exercise Type: ' || ExerciseType AS MostFrequentExerciseType
FROM ExerciseLogs
WHERE UserID = 1
GROUP BY ExerciseType
ORDER BY COUNT(*) DESC
LIMIT 1;

-- Query 11: Calculate the BMI (Body Mass Index) for UserID 1
SELECT 
    'BMI (Body Mass Index): ' || (Weight / (Height * Height)) AS BMI
FROM Users
WHERE UserID = 1;

-- Query 12: Calculate the average daily sleep duration (hours) for UserID 1
SELECT 
    'Average Daily Sleep Duration: ' || AVG(SleepDurationMinutes / 60.0) AS AverageDailySleepDurationHours
FROM SleepData
WHERE UserID = 1;

-- Query 13: Calculate the average daily sleep quality rating for UserID 1
SELECT 
    'Average Daily Sleep Quality Rating: ' || AVG(SleepQualityRating) AS AverageDailySleepQualityRating
FROM SleepData
WHERE UserID = 1;

-- Query 14: Retrieve the user's most recent exercise log entry (type, duration, and date) for UserID 1
SELECT 
    'Most Recent Exercise: Type: ' || ExerciseType || ', Duration: ' || DurationMinutes || ' minutes, Date: ' || DateTime AS LastExerciseDate
FROM ExerciseLogs
WHERE UserID = 1
ORDER BY DateTime DESC
LIMIT 1;
