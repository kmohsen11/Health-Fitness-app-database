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


