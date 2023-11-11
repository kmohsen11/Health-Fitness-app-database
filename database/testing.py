import unittest
import sqlite3
import os

class TestDatabaseOperations(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Connect to the database (use an in-memory database for testing)
        cls.conn = sqlite3.connect(":memory:")
        cls.cursor = cls.conn.cursor()

        # Create tables and indexes (use the same SQL queries as in your project)
        create_tables_sql = """
       -- Create tables
CREATE TABLE Users (
    UserID INTEGER NOT NULL, 
    UserName VARCHAR(50) NOT NULL, 
    Age INTEGER CHECK (Age >= 0), 
    Gender VARCHAR(10), 
    Weight NUMERIC(5, 2), 
    Height NUMERIC(5, 2), 
    ContactInfo VARCHAR(100), 
    PRIMARY KEY (UserID)
);

CREATE TABLE ExerciseLogs (
    LogID INTEGER NOT NULL, 
    UserID INTEGER, 
    ExerciseType VARCHAR(50), 
    DurationMinutes INTEGER, 
    Intensity VARCHAR(20), 
    DateTime DATETIME, 
    CaloriesBurned NUMERIC(7, 2), 
    DistanceCovered NUMERIC(7, 2), 
    HeartRate INTEGER, 
    WeightLiftedLbs NUMERIC(7, 2), 
    PRIMARY KEY (LogID), 
    FOREIGN KEY(UserID) REFERENCES Users (UserID)
);

CREATE TABLE GoalsAndProgress (
    GoalID INTEGER NOT NULL, 
    UserID INTEGER, 
    GoalType VARCHAR(50), 
    GoalValue NUMERIC(7, 2), 
    ProgressValue NUMERIC(7, 2), 
    PRIMARY KEY (GoalID), 
    FOREIGN KEY(UserID) REFERENCES Users (UserID)
);

CREATE TABLE HealthMetrics (
    MetricID INTEGER NOT NULL, 
    UserID INTEGER, 
    Weight NUMERIC(5, 2), 
    WaistCircumference NUMERIC(5, 2), 
    HipCircumference NUMERIC(5, 2), 
    BodyFatPercentage NUMERIC(5, 2), 
    MuscleMass NUMERIC(5, 2), 
    BloodPressure VARCHAR(15), 
    StepCount INTEGER, 
    PRIMARY KEY (MetricID), 
    FOREIGN KEY(UserID) REFERENCES Users (UserID)
);

CREATE TABLE NutritionLogs (
    LogID INTEGER NOT NULL, 
    UserID INTEGER, 
    MealName VARCHAR(100), 
    FoodItems TEXT, 
    MealTime DATETIME, 
    PRIMARY KEY (LogID), 
    FOREIGN KEY(UserID) REFERENCES Users (UserID)
);

CREATE TABLE SleepData (
    SleepID INTEGER NOT NULL, 
    UserID INTEGER, 
    SleepDurationMinutes INTEGER, 
    SleepQualityRating INTEGER, 
    SleepStartTime DATETIME, 
    SleepEndTime DATETIME, 
    PRIMARY KEY (SleepID), 
    FOREIGN KEY(UserID) REFERENCES Users (UserID)
);

CREATE TABLE UserPreferences (
    UserID INTEGER NOT NULL, 
    FitnessGoal VARCHAR(50), 
    DietaryRestrictions VARCHAR(100), 
    PreferredExercises VARCHAR(200), 
    UserForeignKey INTEGER, 
    PRIMARY KEY (UserID), 
    FOREIGN KEY(UserForeignKey) REFERENCES Users (UserID)
);
-- Indexing for Users table
CREATE INDEX idx_Users_UserName ON Users (UserName);
CREATE INDEX idx_Users_Gender ON Users (Gender);

-- Indexing for ExerciseLogs table
CREATE INDEX idx_ExerciseLogs_UserID ON ExerciseLogs (UserID);
CREATE INDEX idx_ExerciseLogs_ExerciseType ON ExerciseLogs (ExerciseType);
CREATE INDEX idx_ExerciseLogs_DateTime ON ExerciseLogs (DateTime);

-- Indexing for GoalsAndProgress table
CREATE INDEX idx_GoalsAndProgress_UserID ON GoalsAndProgress (UserID);
CREATE INDEX idx_GoalsAndProgress_GoalType ON GoalsAndProgress (GoalType);

-- Indexing for HealthMetrics table
CREATE INDEX idx_HealthMetrics_UserID ON HealthMetrics (UserID);
CREATE INDEX idx_HealthMetrics_Weight ON HealthMetrics (Weight);
CREATE INDEX idx_HealthMetrics_WaistCircumference ON HealthMetrics (WaistCircumference);
CREATE INDEX idx_HealthMetrics_HipCircumference ON HealthMetrics (HipCircumference);
CREATE INDEX idx_HealthMetrics_BodyFatPercentage ON HealthMetrics (BodyFatPercentage);

-- Indexing for NutritionLogs table
CREATE INDEX idx_NutritionLogs_UserID ON NutritionLogs (UserID);
CREATE INDEX idx_NutritionLogs_MealName ON NutritionLogs (MealName);
CREATE INDEX idx_NutritionLogs_MealTime ON NutritionLogs (MealTime);

-- Indexing for SleepData table
CREATE INDEX idx_SleepData_UserID ON SleepData (UserID);
CREATE INDEX idx_SleepData_SleepStartTime ON SleepData (SleepStartTime);
CREATE INDEX idx_SleepData_SleepEndTime ON SleepData (SleepEndTime);

-- Indexing for UserPreferences table
CREATE INDEX idx_UserPreferences_UserID ON UserPreferences (UserID);
CREATE INDEX idx_UserPreferences_FitnessGoal ON UserPreferences (FitnessGoal);
        """
        cls.cursor.executescript(create_tables_sql)
        cls.conn.commit()

    @classmethod
    def tearDownClass(cls):
        # Close the database connection
        cls.conn.close()

    def setUp(self):
        # Create a new cursor for each test
        self.cursor = self.conn.cursor()

    def tearDown(self):
        # Rollback any uncommitted changes after each test
        self.conn.rollback()

    def test_insert_user(self):
        # Test inserting a user into the Users table
        insert_user_sql = """
        INSERT INTO Users (UserName, Age, Gender)
        VALUES (?, ?, ?);
        """
        user_data = ("JohnDoe", 30, "Male")
        self.cursor.execute(insert_user_sql, user_data)
        self.conn.commit()

        self.assertEqual(self.cursor.rowcount, 1)

        # Retrieve the inserted user and check if data matches
        self.cursor.execute("SELECT * FROM Users WHERE UserName = 'JohnDoe';")
        user = self.cursor.fetchone()
        self.assertIsNotNone(user)
        self.assertEqual(user[1], "JohnDoe")
        self.assertEqual(user[2], 30)
        self.assertEqual(user[3], "Male")

    def test_update_user(self):
        # Test updating a user's age in the Users table
        insert_user_sql = """
        INSERT INTO Users (UserName, Age, Gender)
        VALUES (?, ?, ?);
        """
        user_data = ("JohnDoe", 30, "Male")
        self.cursor.execute(insert_user_sql, user_data)
        self.conn.commit()

        update_user_sql = """
        UPDATE Users
        SET Age = ?
        WHERE UserName = ?;
        """
        updated_age = 35
        self.cursor.execute(update_user_sql, (updated_age, "JohnDoe"))
        self.conn.commit()

        # Retrieve the updated user and check if age is updated
        self.cursor.execute("SELECT * FROM Users WHERE UserName = 'JohnDoe';")
        user = self.cursor.fetchone()
        self.assertIsNotNone(user)
        self.assertEqual(user[2], updated_age)

    def test_delete_user(self):
        # Test deleting a user from the Users table
        insert_user_sql = """
        INSERT INTO Users (UserName, Age, Gender)
        VALUES (?, ?, ?);
        """
        user_data = ("JohnDoe", 30, "Male")
        self.cursor.execute(insert_user_sql, user_data)
        self.conn.commit()

        delete_user_sql = """
        DELETE FROM Users
        WHERE UserName = ?;
        """
        self.cursor.execute(delete_user_sql, ("JohnDoe",))
        self.conn.commit()

        # Check if the user is deleted
        self.cursor.execute("SELECT * FROM Users WHERE UserName = 'JohnDoe';")
        user = self.cursor.fetchone()
        self.assertIsNone(user)

    def test_insert_exercise_log(self):
        # Test inserting an exercise log into the ExerciseLogs table
        insert_exercise_log_sql = """
        INSERT INTO ExerciseLogs (UserID, ExerciseType, DurationMinutes, Intensity, DateTime)
        VALUES (?, ?, ?, ?, ?);
        """
        exercise_log_data = (1, "Running", 60, "High", "2023-10-15 08:00:00")
        self.cursor.execute(insert_exercise_log_sql, exercise_log_data)
        self.conn.commit()

        self.assertEqual(self.cursor.rowcount, 1)

        # Retrieve the inserted exercise log and check if data matches
        self.cursor.execute("SELECT * FROM ExerciseLogs WHERE LogID = 1;")
        exercise_log = self.cursor.fetchone()
        self.assertIsNotNone(exercise_log)
        self.assertEqual(exercise_log[2], "Running")
        self.assertEqual(exercise_log[3], 60)
        self.assertEqual(exercise_log[4], "High")

    def test_update_exercise_log(self):
        # Test updating an exercise log's intensity in the ExerciseLogs table
        insert_exercise_log_sql = """
        INSERT INTO ExerciseLogs (UserID, ExerciseType, DurationMinutes, Intensity, DateTime)
        VALUES (?, ?, ?, ?, ?);
        """
        exercise_log_data = (1, "Running", 60, "High", "2023-10-15 08:00:00")
        self.cursor.execute(insert_exercise_log_sql, exercise_log_data)
        self.conn.commit()

        update_exercise_log_sql = """
        UPDATE ExerciseLogs
        SET Intensity = ?
        WHERE LogID = ?;
        """
        updated_intensity = "Moderate"
        self.cursor.execute(update_exercise_log_sql, (updated_intensity, 1))
        self.conn.commit()

        # Retrieve the updated exercise log and check if intensity is updated
        self.cursor.execute("SELECT * FROM ExerciseLogs WHERE LogID = 1;")
        exercise_log = self.cursor.fetchone()
        self.assertIsNotNone(exercise_log)
        self.assertEqual(exercise_log[4], updated_intensity)

    def test_delete_exercise_log(self):
        # Test deleting an exercise log from the ExerciseLogs table
        insert_exercise_log_sql = """
        INSERT INTO ExerciseLogs (UserID, ExerciseType, DurationMinutes, Intensity, DateTime)
        VALUES (?, ?, ?, ?, ?);
        """
        exercise_log_data = (1, "Running", 60, "High", "2023-10-15 08:00:00")
        self.cursor.execute(insert_exercise_log_sql, exercise_log_data)
        self.conn.commit()

        delete_exercise_log_sql = """
        DELETE FROM ExerciseLogs
        WHERE LogID = ?;
        """
        self.cursor.execute(delete_exercise_log_sql, (1,))
        self.conn.commit()

        # Check if the exercise log is deleted
        self.cursor.execute("SELECT * FROM ExerciseLogs WHERE LogID = 1;")
        exercise_log = self.cursor.fetchone()
        self.assertIsNone(exercise_log)

    # Add more test cases for other tables and CRUD operations

if __name__ == '__main__':
    unittest.main()
