import GenerateDatabaseTables
import InsertCoursesIntoDatabase
import InsertGenEdsToDatabase
import ScrapeMajorRequirementsJSON
import AddMajorRequirementsToDatabase

import sqlite3
import os


database = "\\".join(os.getcwd().split("\\")[:os.getcwd().split("\\").index("399capstone-p-np") + 1]) + "\\library\\adapters\\399courses.db"
sqliteConnection = sqlite3.connect(database)
cursor = sqliteConnection.cursor()

#THIS ASSUMES EVERYTHING IS A SCIENCE MAJOR
cursor.execute("""insert into scheduleMajorLink (scheduleID, majorID)
select scheduleID, majorRequirements.majorID from  schedule 
inner join majorRequirements 
on scheduleID == "Open Schedule"
or scheduleID == "Engineering, Medical and Health Sciences, Science (EMHSS) Schedule";""")

sqliteConnection.commit()
cursor.close()

