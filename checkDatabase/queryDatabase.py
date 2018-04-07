from firebase import firebase
import argparse

class QueryDatabase:

	def __init__(self, argc, argv):
	
		self.argc = argc
		self.argv = argv
		
		self.parser = None
		self.args = None
		
		self.ingredients = None
		
		self.recipes = {}
		self.data = []
		
		self.firebase = firebase.FirebaseApplication('https://madhacks2018.firebaseio.com/', None)
		
		self.parseArgs()
		self.readFromDatabase()
		
		
		
	def parseArgs(self):
	
		self.parser = argparse.ArgumentParser(description='Process some integers.')
		self.parser.add_argument('args', metavar='N', type=str, nargs='+', help='an integer for the accumulator')
		self.args = self.parser.parse_args()
		self.ingredients = vars(self.args)['args']
		
	def readFromDatabase(self):
		
		result = self.firebase.get('/recipes', None)
		
		numEntries = 0
		
		for index, ingredient in enumerate(result):
			
			try:
				for ingredient in self.ingredients:
				
					for otherIngredient in result[index]['ingredients']:
					
						if ingredient in otherIngredient.lower():
							
							print(result[index])
								
			except:
				continue

				
			
			
if __name__ == "__main__":

	QueryDatabase(1, 2)