
## Tables and Fields

### Users
| Field       | Type          | Constraints               |
|-------------|---------------|---------------------------|
| UserID      | INTEGER       | NOT NULL, PRIMARY KEY     |
| UserName    | VARCHAR(50)   | NOT NULL                  |
| Age         | INTEGER       | CHECK (Age >= 0)          |
| Gender      | VARCHAR(10)   |                           |
| Weight      | NUMERIC(5, 2) |                           |
| Height      | NUMERIC(5, 2) |                           |
| ContactInfo | VARCHAR(100)  |                           |

### ExerciseLogs
| Field            | Type          | Constraints                         |
|------------------|---------------|-------------------------------------|
| LogID            | INTEGER       | NOT NULL, PRIMARY KEY               |
| UserID           | INTEGER       | FOREIGN KEY REFERENCES Users(UserID)|
| ExerciseType     | VARCHAR(50)   |                                     |
| DurationMinutes  | INTEGER       |                                     |
| Intensity        | VARCHAR(20)   |                                     |
| DateTime         | DATETIME      |                                     |
| CaloriesBurned   | NUMERIC(7, 2) |                                     |
| DistanceCovered  | NUMERIC(7, 2) |                                     |
| HeartRate        | INTEGER       |                                     |
| WeightLiftedLbs  | NUMERIC(7, 2) |                                     |

### GoalsAndProgress
| Field         | Type          | Constraints                          |
|---------------|---------------|--------------------------------------|
| GoalID        | INTEGER       | NOT NULL, PRIMARY KEY                |
| UserID        | INTEGER       | FOREIGN KEY REFERENCES Users(UserID) |
| GoalType      | VARCHAR(50)   |                                      |
| GoalValue     | NUMERIC(7, 2) |                                      |
| ProgressValue | NUMERIC(7, 2) |                                      |

### HealthMetrics
| Field               | Type          | Constraints                          |
|---------------------|---------------|--------------------------------------|
| MetricID            | INTEGER       | NOT NULL, PRIMARY KEY                |
| UserID              | INTEGER       | FOREIGN KEY REFERENCES Users(UserID) |
| Weight              | NUMERIC(5, 2) |                                      |
| WaistCircumference  | NUMERIC(5, 2) |                                      |
| HipCircumference    | NUMERIC(5, 2) |                                      |
| BodyFatPercentage   | NUMERIC(5, 2) |                                      |
| MuscleMass          | NUMERIC(5, 2) |                                      |
| BloodPressure       | VARCHAR(15)   |                                      |
| StepCount           | INTEGER       |                                      |

### NutritionLogs
| Field     | Type   | Constraints                          |
|-----------|--------|--------------------------------------|
| LogID     | INTEGER| NOT NULL, PRIMARY KEY                |
| UserID    | INTEGER| FOREIGN KEY REFERENCES Users(UserID) |
| MealName  | VARCHAR(100) |                                |
| FoodItems | TEXT   |                                      |
| MealTime  | DATETIME|                                      |

### SleepData
| Field                | Type     | Constraints                          |
|----------------------|----------|--------------------------------------|
| SleepID              | INTEGER  | NOT NULL, PRIMARY KEY                |
| UserID               | INTEGER  | FOREIGN KEY REFERENCES Users(UserID) |
| SleepDurationMinutes | INTEGER  |                                      |
| SleepQualityRating   | INTEGER  |                                      |
| SleepStartTime       | DATETIME |                                      |
| SleepEndTime         | DATETIME |                                      |

### UserPreferences
| Field               | Type          | Constraints                                 |
|---------------------|---------------|---------------------------------------------|
| UserID              | INTEGER       | NOT NULL, PRIMARY KEY                       |
| FitnessGoal         | VARCHAR(50)   |                                             |
| DietaryRestrictions | VARCHAR(100)  |                                             |
| PreferredExercises  | VARCHAR(200)  |                                             |
| UserForeignKey      | INTEGER       | FOREIGN KEY(UserForeignKey) REFERENCES Users(UserID) |

## Indexes

### Users Table Indexes
- `CREATE INDEX idx_Users_UserName ON Users (UserName);`
- `CREATE INDEX idx_Users_Gender ON Users (Gender);`

### ExerciseLogs Table Indexes
- `CREATE INDEX idx_ExerciseLogs_UserID ON ExerciseLogs (UserID);`
- `CREATE INDEX idx_ExerciseLogs_ExerciseType ON ExerciseLogs (ExerciseType);`
- `CREATE INDEX idx_ExerciseLogs_DateTime ON ExerciseLogs (DateTime);`

### GoalsAndProgress Table Indexes
- `CREATE INDEX idx_GoalsAndProgress_UserID ON GoalsAndProgress (UserID);`
- `CREATE INDEX idx_GoalsAndProgress_GoalType ON GoalsAndProgress (GoalType);`

### HealthMetrics Table Indexes
- `CREATE INDEX idx_HealthMetrics_UserID ON HealthMetrics (UserID);`
- `CREATE INDEX idx_HealthMetrics_Weight ON HealthMetrics (Weight);`
- `CREATE INDEX idx_HealthMetrics_WaistCircumference ON HealthMetrics (WaistCircumference);`
- `CREATE INDEX idx_HealthMetrics_HipCircumference ON HealthMetrics (HipCircumference);`
- `CREATE INDEX idx_HealthMetrics_BodyFatPercentage ON HealthMetrics (BodyFatPercentage);`

### NutritionLogs Table Indexes
- `CREATE INDEX idx_NutritionLogs_UserID ON NutritionLogs (UserID);`
- `CREATE INDEX idx_NutritionLogs_MealName ON NutritionLogs (MealName);`
- `CREATE INDEX idx_NutritionLogs_MealTime ON NutritionLogs (MealTime);`

### SleepData Table Indexes
- `CREATE INDEX idx_SleepData_UserID ON SleepData (UserID);`
- `CREATE INDEX idx_SleepData_SleepStartTime ON SleepData (SleepStartTime);`
- `CREATE INDEX idx_SleepData_SleepEndTime ON SleepData (SleepEndTime);`

### UserPreferences Table Indexes
- `CREATE INDEX idx_UserPreferences_UserID ON UserPreferences (UserID);`
- `CREATE INDEX idx_UserPreferences_FitnessGoal ON UserPreferences (FitnessGoal);`
