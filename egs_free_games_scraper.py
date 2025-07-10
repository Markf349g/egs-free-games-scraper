import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC




# Class for avoiding namespace problems
class EpicGamesStoreScraper:
	'''
	A class for getting free games every two weeks from Epic Games Store

	Contains:
		get_free_games_json()
	'''

	def __init__(self, web_driver: WebDriver = None, destructor: bool = True):
		'''
		Initializes a new instance of a EpicGamesStoreScraper class
		Parameters:
			web_driver(WebDriver): selenium web driver instance
			destructor(bool): necessity of destruction of web driver
		'''
		self.web_driver = web_driver if web_driver != None else webdriver.Chrome()
		self.destructor = destructor

	def __del__(self):
		self.web_driver.quit() if self.web_driver != None and self.destructor else None
	
	def get_free_games_json(self) -> str:
		'''
		Gives JSON object with information
		Attributes:
			None
		Returns:
			str: a json object
		'''
		# Setup
		self.web_driver.get('https://store.epicgames.com/en-US/free-games')
		element = WebDriverWait(self.web_driver, 5).until(
			EC.presence_of_element_located((By.CLASS_NAME, 'css-2u323'))
		)

		# Main dictionary and 2 constants
		parse_data: dict = {}
		xpath1 = '//*[@id="app-main-content"]/div[3]/div/div/div/div[1]/div[2]/span/div/div/section/div/div['
		xpath2 = '/div/div/div/a/div/div['
		
		# Main loop
		for i in range(4):
			# Find name of the game using XPATH
			name: str = self.web_driver.find_element(
        By.XPATH, 
        f'{xpath1}{i+1}]{xpath2}2]/div/h6'
    	).text
    
			# Find image of the game using XPATH
			image: str = self.web_driver.find_element(
        By.XPATH,
        f'{xpath1}{i+1}]{xpath2}1]/div[1]/div/div/div/img'
    	).get_attribute('src')

			# Find status of the game using XPATH
			status: str = self.web_driver.find_element(
        By.XPATH,
        f'{xpath1}{i+1}]{xpath2}1]/div[2]/div/div/span'
    	).text

			# Find date of the free game using XPATH
			date: str = self.web_driver.find_element(
        By.XPATH,
        f'{xpath1}{i+1}]{xpath2}2]/div/p/span'
    	).text
			date = date.replace('Free ', '', 1)

			# JSON Object
			parse_data[name] = {
        'Name': name,
        'Image': image,
        'Status': status,
        'Free Date': date
    	}

		return json.dumps(parse_data, indent=2)
  
if __name__ == '__main__':
	# A few lines example
	web_driver: WebDriver = webdriver.Chrome()

	egss_class: EpicGamesStoreScraper = EpicGamesStoreScraper(
		web_driver=web_driver,
		destructor=False
	)
	json_value: str = egss_class.get_free_games_json()
	print(json_value)

	web_driver.quit()
	# A one line example
	print(EpicGamesStoreScraper().get_free_games_json())