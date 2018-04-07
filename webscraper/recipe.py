class Recipe:

	def __init__(self, url, ingredients, description, calories, image, prep):
		
		self.url = url
		self.ingredients = ingredients
		self.description = descritption
		self.calories = calories
		self.image = image
		self.prep = prep
		
	def returnJSON(self):
	
		recipe = {"url": self.url,
				  "ingredients": self.ingredients,
				  "description": self.description,
				  "calories": self.calories,
				  "image": self.image,
				  "prep": self.prep}