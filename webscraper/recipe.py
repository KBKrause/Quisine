class Recipe:

	def __init__(self):
		
		self.url = None
		self.ingredients = None
		self.description = None
		self.calories = None
		self.image = None
		self.prep = None
		
	def setURL(self, url):
		self.url = url
		
	def setIngredients(self, ingredients):
		self.ingredients = ingredients
		
	def setDescription(self, description):
		self.description = description
		
	def setCalories(self, calories):
		self.calories = calories
		
	def setImage(self, image):
		self.image = image
		
	def setPrep(self, prep):
		self.prep = prep
		
	def returnJSON(self):
	
		recipe = {"url": self.url,
				  "ingredients": self.ingredients,
				  "description": self.description,
				  "calories": self.calories,
				  "image": self.image,
				  "prep": self.prep}
				  
		return recipe