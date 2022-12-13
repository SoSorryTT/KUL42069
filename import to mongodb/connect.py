from pymongo import MongoClient
import csv
from csv import DictReader
from config import CONNECT

def get_database():
 
   # Provide the mongodb atlas url to connect python to mongodb using pymongo
   CONNECTION_STRING = CONNECT
 
   # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
   client = MongoClient(CONNECTION_STRING)
 
   # Create the database for our example (we will use the same database throughout the tutorial
   return client['DAQ']
  
# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":   
  
   # Get the database
   dbname = get_database()




   # open file in read mode
   with open("data.csv", 'r') as f:
      dict_reader = DictReader(f)
      list_of_dict = list(dict_reader)
      dbname['people'].insert_many(list_of_dict)

   # use = []
   # for i in list_of_dict:
   #    use.append(
   #       {i['หน่วยงาน'],
   #       i['ที่อยู่จุดบริการ'],
   #       i['ละติจูด'],
   #       i['ลองติจูด']}
   #       )
   #    print(use)
   #    break

   # dbname['hospital'].insert_one({'name': 'test2'})
   # print(collection_name)

   