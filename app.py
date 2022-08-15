from database import Database
from menu import Menu

Database.initialize()

menu = Menu()

menu.run_menu()











#The code below was practice for using MongoDB
# import collections
# import pymongo

# uri = "mongodb://127.0.0.1:27071"

# client = pymongo.MongoClient(uri)
# database = client['fullstack']
# collection = database['students']

# students =  [student for student in collection.find({})]

# print(students)

