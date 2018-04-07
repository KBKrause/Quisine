from bs4 import BeautifulSoup, SoupStrainer
import requests

class RecipeScraper:

	def __init__(self, websites):
		
		# Get the list of website to look through
		self.websites = websites
		
		# Storage space for HTML code
		self.RawHTML = []
		
		# Get raw HTML from requested website
		self.__requestHTML()
		
	def __requestHTML(self):
	
		session = requests.Session()
		session.max_redirects = 60
	
		# Get the content and response of main web page
		response = session.get("https://www.allrecipes.com/?page=5")
		
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
					self.parseContent(response1.content)
					
				except Exception as e:
					continue
		
	def parseContent(self, content):
	
		# Get the content of the current page
		currentPageInfo = BeautifulSoup(content, "html.parser")
		
		# Find the ingredients of the recipe
		#for span in currentPageInfo.find_all('span',itemprop="ingredients"):
		#	print(span.string)
		
		# Find the prep time for the recipe 
		#for time in currentPageInfo.find_all('span', {'class' : 'prepTime__item--time'}):
		#	print(time.string)
			
		#for calories in currentPageInfo.find_all('span', itemprop="calories"):
		#	print(calories.string.strip(";"))
			
		for image in currentPageInfo.find_all("meta", property="og:image"):
			print(image["content"])
		
		
		

if __name__ == "__main__":

	RecipeScraper(["test", "test1"])