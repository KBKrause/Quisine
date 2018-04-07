from firebase import firebase
from firebase_admin import db
import json

class UpdateFirebase():

	def __init__(self, json_data):
		
		self.json_data = [data.returnJSON() for data in json_data]
		
		self.database = firebase.FirebaseApplication("https://madhacks2018.firebaseio.com/")
		
		
		self.__pushEntries()
		
	def __pushEntries(self): 
		
		print("Posting the recipe data to the Firebase...")
		self.database.patch("", {"recipes": self.json_data})		
		print("Finished posting data to the Firebase...")
	