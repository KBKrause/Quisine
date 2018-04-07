from bs4 import BeautifulSoup, SoupStrainer
import requests
from recipe import Recipe

class RecipeScraper:

	def __init__(self, websites):
		
		# Get the list of website to look through
		self.websites = websites
		
		self.ingredients = []
		self.recipes = []
		
		# Get raw HTML from requested website
		self.__requestHTML()
		
	def __requestHTML(self):
	
		session = requests.Session()
		session.max_redirects = 60
	
		# Get the content and response of main web page
		response = session.get("https://www.allrecipes.com/")
		
		# Get the HTML content of main page
		soup = BeautifulSoup(response.content, "html.parser")
		
		# Index though, retrieving all links 
		for index, link in enumerate(soup.find_all('a', href=True)):
			
			# If from all recipes then try to get recipe
			if (("https://www.allrecipes.com/recipe" in link['href']) and (index > 170)) or (("https://" in link["href"]) and (index > 170)):
				
				# Request information from website
				response1 = session.get(link["href"])

				# Try to parse content, if not continue
				try:
					self.parseContent(response1.content, link["href"])
					
				except Exception as e:
					continue
					
		for r in self.recipes:
			print("prep: ", r.getPrep(), "\n")
			print("desciption: ", r.getDescription(), "\n")
			print("image: ", r.getImage(), "\n")
			print("ingredients: ", r.getIngredients(), "\n")
			print("calories: ", r.getCalories(), "\n")
			print("url: ", r.getURL(), "\n")
			
		
	def parseContent(self, content, link):
	
		# Get the content of the current page
		currentPageInfo = BeautifulSoup(content, "html.parser")
		print("Parsing: ", link)
		new_recipe = Recipe()
		new_recipe.setURL(link)
		
		# Find the ingredients of the recipe
		for span in currentPageInfo.find_all('span',itemprop="ingredients"):
			self.ingredients.append(span.string)
				
		description = currentPageInfo.find("meta",  property="og:description")
		
		new_recipe.setDescription(description["content"])
				
		new_recipe.setIngredients(self.ingredients)
		
		for time in currentPageInfo.find_all('span', {'class' : 'prepTime__item--time'}):
			new_recipe.setPrep(time.string)
			
		for calories in currentPageInfo.find_all('span', itemprop="calories"):
			new_recipe.setCalories(calories.string.strip(";"))
			
		new_recipe.setImage(currentPageInfo.find_all("meta", property="og:image")[0]["content"])
			
		self.recipes.append(new_recipe)
		
		return self.recipes
		
	

if __name__ == "__main__":

	RecipeScraper(["test", "test1"])