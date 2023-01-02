import os
import csv
import subprocess
import time
import sys
try:
    import pandas as pd
except:
    subprocess.run(["pip","install","pandas"])
    import pandas as pd


df = pd.read_csv("Students.csv", index_col="Student ID")
# Adding row at a given index (Student ID)
df.loc['ECE2102'] = ['sankar kumar das',1,'ECE21']
# Drop "Student ID" index
df = df.reset_index()
# Write the updated DataFrame into employees.csv.
df.to_csv('Students.csv', index=False)
#df = pd.read_csv('Students.csv', index_col='Student ID')
print(df)

df = pd.read_csv("Students.csv", index_col="Student ID")
# Replacing Name
df.at['ECE2102', 'Name'] =  'Avijit kumar'
# Reset inde to 0,1,2,...
df = df.reset_index()
# writing the changes into the file.
df.to_csv('Students.csv', index=False)
print(df)


df = pd.read_csv("Students.csv")
# Updating Name
df = df.replace({"Sankar Das":"Sankar Kumar Das", "Avik Haldar": "Avik Kumar Haldar"})
df.to_csv("Students.csv", index=False)
print(df)

df = pd.read_csv("Students.csv")
# Deleting Row
df = df.iloc[:-1]
df.to_csv("Students.csv", index=False)
print(df)
