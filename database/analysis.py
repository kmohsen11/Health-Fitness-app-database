import sqlite3
import time
import matplotlib.pyplot as plt

# Connect to the SQLite database
conn = sqlite3.connect("health_fitness_app.db")
cursor = conn.cursor()

# Helper function to execute a query and measure its execution time
def execute_query(query):
    start_time = time.time()
    cursor.execute(query)
    execution_time = time.time() - start_time
    return execution_time

# Original Query 1 (uses a subquery)
query1_original = """
SELECT ExerciseType, DurationMinutes, CaloriesBurned
FROM ExerciseLogs
WHERE UserID IN (SELECT UserID FROM Users WHERE UserName = 'JohnDoe');
"""
execution_time_original_query1 = execute_query(query1_original)

# Optimized Query 1 (Same as Original, but without subquery)
query1_optimized = """
SELECT ExerciseType, DurationMinutes, CaloriesBurned
FROM ExerciseLogs
WHERE UserID = 1;
"""
execution_time_optimized_query1 = execute_query(query1_optimized)

# Original Query 2 (performing a self-join)
query2_original = """
SELECT G1.GoalType, G1.GoalValue, P1.ProgressValue
FROM GoalsAndProgress G1
JOIN GoalsAndProgress P1 ON G1.UserID = P1.UserID
WHERE G1.UserID = 1;
"""
execution_time_original_query2 = execute_query(query2_original)

# Optimized Query 2 (Same as Original, but without self-join)
query2_optimized = """
SELECT GoalType, GoalValue, ProgressValue
FROM GoalsAndProgress
WHERE UserID = 1;
"""
execution_time_optimized_query2 = execute_query(query2_optimized)

# Original Query 3 (adding unnecessary filtering)
query3_original = """
SELECT COUNT(*) AS NumberOfGoals
FROM GoalsAndProgress
WHERE UserID = 1 AND GoalValue > 0;
"""
execution_time_original_query3 = execute_query(query3_original)

# Optimized Query 3 (Same as Original, but without unnecessary filtering)
query3_optimized = """
SELECT COUNT(*) AS NumberOfGoals
FROM GoalsAndProgress
WHERE UserID = 1;
"""
execution_time_optimized_query3 = execute_query(query3_optimized)

# Original Query 4 (adding additional joins)
query4_original = """
SELECT H.Weight, H.WaistCircumference, H.HipCircumference, H.BodyFatPercentage
FROM HealthMetrics H
JOIN ExerciseLogs E ON H.UserID = E.UserID
WHERE H.UserID = 1;
"""
execution_time_original_query4 = execute_query(query4_original)

# Optimized Query 4 (Same as Original, but without additional joins)
query4_optimized = """
SELECT Weight, WaistCircumference, HipCircumference, BodyFatPercentage
FROM HealthMetrics
WHERE UserID = 1;
"""
execution_time_optimized_query4 = execute_query(query4_optimized)

# Original Query 5 (using a subquery)
query5_original = """
SELECT MealName, FoodItems, MealTime
FROM NutritionLogs
WHERE UserID = (SELECT UserID FROM Users WHERE UserName = 'JohnDoe')
  AND DATE(MealTime) = '2023-10-01';
"""
execution_time_original_query5 = execute_query(query5_original)

# Optimized Query 5 (Same as Original, but without subquery)
query5_optimized = """
SELECT MealName, FoodItems, MealTime
FROM NutritionLogs
WHERE UserID = 1
  AND DATE(MealTime) = '2023-10-01';
"""
execution_time_optimized_query5 = execute_query(query5_optimized)

# Original Query 6 (performing a self-join)
query6_original = """
SELECT S1.SleepDurationMinutes, S1.SleepQualityRating, S2.SleepStartTime, S2.SleepEndTime
FROM SleepData S1
JOIN SleepData S2 ON S1.UserID = S2.UserID
WHERE S1.UserID = 1;
"""
execution_time_original_query6 = execute_query(query6_original)

# Optimized Query 6 (Same as Original, but without self-joinin)
query6_optimized = """
SELECT SleepDurationMinutes, SleepQualityRating, SleepStartTime, SleepEndTime
FROM SleepData
WHERE UserID = 1;
"""
execution_time_optimized_query6 = execute_query(query6_optimized)

# Original Query 7 (adding unnecessary filtering)
query7_original = """
SELECT FitnessGoal, DietaryRestrictions, PreferredExercises
FROM UserPreferences
WHERE UserID = 1 AND FitnessGoal = 'Lose Weight';
"""
execution_time_original_query7 = execute_query(query7_original)

# Optimized Query 7 (Same as Original, but with different filtering)
query7_optimized = """
SELECT FitnessGoal, DietaryRestrictions, PreferredExercises
FROM UserPreferences
WHERE UserID = 1;
"""
execution_time_optimized_query7 = execute_query(query7_optimized)

# Original Query 8 (using a subquery)
query8_original = """
SELECT SUM(DurationMinutes) AS TotalExerciseDuration
FROM ExerciseLogs
WHERE UserID = (SELECT UserID FROM Users WHERE UserName = 'JohnDoe');
"""
execution_time_original_query8 = execute_query(query8_original)

# Optimized Query 8 (Same as Original, but without subquery)
query8_optimized = """
SELECT SUM(DurationMinutes) AS TotalExerciseDuration
FROM ExerciseLogs
WHERE UserID = 1;
"""
execution_time_optimized_query8 = execute_query(query8_optimized)

# Original Query 9 (performing a self-join)
query9_original = """
SELECT AVG(E1.Intensity) AS AverageExerciseIntensity
FROM ExerciseLogs E1
JOIN ExerciseLogs E2 ON E1.UserID = E2.UserID
WHERE E1.UserID = 1;
"""
execution_time_original_query9 = execute_query(query9_original)

# Optimized Query 9 (Same as Original, but without self-join)
query9_optimized = """
SELECT AVG(Intensity) AS AverageExerciseIntensity
FROM ExerciseLogs
WHERE UserID = 1;
"""
execution_time_optimized_query9 = execute_query(query9_optimized)

# Original Query 10 (using a subquery)
query10_original = """
SELECT ExerciseType AS MostFrequentExerciseType
FROM ExerciseLogs
WHERE UserID = (SELECT UserID FROM Users WHERE UserName = 'JohnDoe')
GROUP BY ExerciseType
ORDER BY COUNT(*) DESC
LIMIT 1;
"""
execution_time_original_query10 = execute_query(query10_original)

# Optimized Query 10 (Same as Original, but without subquery)
query10_optimized = """
SELECT ExerciseType AS MostFrequentExerciseType
FROM ExerciseLogs
WHERE UserID = 1
GROUP BY ExerciseType
ORDER BY COUNT(*) DESC
LIMIT 1;
"""
execution_time_optimized_query10 = execute_query(query10_optimized)

# Original Query 11 (performing a self-join)
query11_original = """
SELECT (U1.Weight / (U2.Height * U2.Height)) AS BMI
FROM Users U1
JOIN Users U2 ON U1.UserID = U2.UserID
WHERE U1.UserID = 1;
"""
execution_time_original_query11 = execute_query(query11_original)

# Optimized Query 11 (Same as Original, but without self-join)
query11_optimized = """
SELECT (Weight / (Height * Height)) AS BMI
FROM Users
WHERE UserID = 1;
"""
execution_time_optimized_query11 = execute_query(query11_optimized)

# Original Query 13 (using a subquery)
query13_original = """
SELECT AVG(SleepDurationMinutes / 60.0) AS AverageDailySleepDurationHours
FROM SleepData
WHERE UserID = (SELECT UserID FROM Users WHERE UserName = 'JohnDoe');
"""
execution_time_original_query13 = execute_query(query13_original)

# Optimized Query 13 (Same as Original, but without subquery)
query13_optimized = """
SELECT AVG(SleepDurationMinutes / 60.0) AS AverageDailySleepDurationHours
FROM SleepData
WHERE UserID = 1;
"""
execution_time_optimized_query13 = execute_query(query13_optimized)


# Original Query 14 (adding additional joins)
query14_original = """
SELECT AVG(S.SleepQualityRating) AS AverageDailySleepQualityRating
FROM SleepData S
JOIN Users U ON S.UserID = U.UserID
WHERE S.UserID = 1;
"""
execution_time_original_query14 = execute_query(query14_original)

# Optimized Query 14 (Same as Original, but without additional joins)
query14_optimized = """
SELECT AVG(SleepQualityRating) AS AverageDailySleepQualityRating
FROM SleepData
WHERE UserID = 1;
"""
execution_time_optimized_query14 = execute_query(query14_optimized)

# Original Query 15 (using a subquery)
query15_original = """
SELECT E.ExerciseType, E.DurationMinutes, E.DateTime AS LastExerciseDate
FROM ExerciseLogs E
WHERE E.UserID = (SELECT UserID FROM Users WHERE UserName = 'JohnDoe')
ORDER BY E.DateTime DESC
LIMIT 1;
"""
execution_time_original_query15 = execute_query(query15_original)

# Optimized Query 15 (Same as Original, but without subquery)
query15_optimized = """
SELECT ExerciseType, DurationMinutes, DateTime AS LastExerciseDate
FROM ExerciseLogs
WHERE UserID = 1
ORDER BY DateTime DESC
LIMIT 1;
"""
execution_time_optimized_query15 = execute_query(query15_optimized)

# Close the database connection
conn.close()

# Print the performance results
print("Query 1 (Original):", execution_time_original_query1)
print("Query 1 (Optimized):", execution_time_optimized_query1)
print("Query 2 (Original):", execution_time_original_query2)
print("Query 2 (Optimized):", execution_time_optimized_query2)
print("Query 3 (Original):", execution_time_original_query3)
print("Query 3 (Optimized):", execution_time_optimized_query3)
print("Query 4 (Original):", execution_time_original_query4)
print("Query 4 (Optimized):", execution_time_optimized_query4)
print("Query 5 (Original):", execution_time_original_query5)
print("Query 5 (Optimized):", execution_time_optimized_query5)
print("Query 6 (Original):", execution_time_original_query6)
print("Query 6 (Optimized):", execution_time_optimized_query6)
print("Query 7 (Original):", execution_time_original_query7)
print("Query 7 (Optimized):", execution_time_optimized_query7)
print("Query 8 (Original):", execution_time_original_query8)
print("Query 8 (Optimized):", execution_time_optimized_query8)
print("Query 9 (Original):", execution_time_original_query9)
print("Query 9 (Optimized):", execution_time_optimized_query9)
print("Query 10 (Original):", execution_time_original_query10)
print("Query 10 (Optimized):", execution_time_optimized_query10)
print("Query 11 (Original):", execution_time_original_query11)
print("Query 11 (Optimized):", execution_time_optimized_query11)
print("Query 13 (Original):", execution_time_original_query13)
print("Query 13 (Optimized):", execution_time_optimized_query13)
print("Query 14 (Original):", execution_time_original_query14)
print("Query 14 (Optimized):", execution_time_optimized_query14)
print("Query 15 (Original):", execution_time_original_query15)
print("Query 15 (Optimized):", execution_time_optimized_query15)

# Original query execution times
original_execution_times = [
    execution_time_original_query1,
    execution_time_original_query2,
    execution_time_original_query3,
    execution_time_original_query4,
    execution_time_original_query5,
    execution_time_original_query6,
    execution_time_original_query7,
    execution_time_original_query8,
    execution_time_original_query9,
    execution_time_original_query10,
    execution_time_original_query11,
    execution_time_original_query13,
    execution_time_original_query14,
    execution_time_original_query15,
]

# Optimized query execution times
optimized_execution_times = [
    execution_time_optimized_query1,
    execution_time_optimized_query2,
    execution_time_optimized_query3,
    execution_time_optimized_query4,
    execution_time_optimized_query5,
    execution_time_optimized_query6,
    execution_time_optimized_query7,
    execution_time_optimized_query8,
    execution_time_optimized_query9,
    execution_time_optimized_query10,
    execution_time_optimized_query11,
    execution_time_optimized_query13,
    execution_time_optimized_query14,
    execution_time_optimized_query15,
]

# Query labels
query_labels = [
    "Query 1", "Query 2", "Query 3", "Query 4", "Query 5", "Query 6", "Query 7", 
    "Query 8", "Query 9", "Query 10", "Query 11", "Query 13", "Query 14", "Query 15",
]

# Create a bar plot
plt.figure(figsize=(12, 6))
plt.barh(query_labels, original_execution_times, color='b', alpha=0.6, label='Original')
plt.barh(query_labels, optimized_execution_times, color='g', alpha=0.6, label='Optimized')
plt.xlabel('Execution Time (seconds)')
plt.title('Query Execution Times (Original vs. Optimized)')
plt.legend()
plt.tight_layout()
plt.show()
