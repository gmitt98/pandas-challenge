import pandas as pd
import os

# First I get the path to the project directory
projectDir = os.path.dirname(os.path.abspath(__file__))
# Then I create the file path relative to the project directory
schoolFilePath = os.path.join(projectDir, "Resources", "schools_complete.csv")
studentFilePath = os.path.join(projectDir, "Resources", "students_complete.csv")
# Now I read the csv file into a dataframe
schdf = pd.read_csv(schoolFilePath)
studf = pd.read_csv(studentFilePath)
# Look at the dataframes to make sure this worked
print(schdf.head())
print(studf.head())