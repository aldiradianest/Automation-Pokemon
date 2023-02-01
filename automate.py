import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains


class TestAutomate(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.browser.maximize_window()

    
    def test_case_automate(self): 
        self.browser.get("https://www.pokemon.com/us/")
        time.sleep(2)
        self.browser.find_element(By.XPATH,"/html/body/div[18]/div[2]/div/div/div[2]/div/div/button[2]").click()
        time.sleep(2)
        # self.browser.find_element(By.XPATH,"/html/body/div[18]/div[2]/div/div/div[2]/div/div/button[2]").click()
        # time.sleep(2)

        actions = ActionChains(self.browser)

        pokedexLink = self.browser.find_element(By.XPATH, "/html/body/nav/div[2]/ul/li[2]/a")
        actions.move_to_element(pokedexLink)
        actions.click(pokedexLink)
        actions.perform()
        time.sleep(2)

        self.browser.find_element(By.ID,"searchInput").send_keys("Pikachu")
        time.sleep(2)
        self.browser.find_element(By.XPATH,"/html/body/div[4]/section[2]/div[1]/div/div[1]/div/div/input").click()
        time.sleep(2)

        pikachuLink = self.browser.find_element(By.XPATH, "/html/body/div[4]/section[5]/ul/li/figure/a/img")
        actions.move_to_element(pikachuLink)
        actions.click(pikachuLink)
        actions.perform()
        time.sleep(3)

        exploreMorePokemon = self.browser.find_element(By.XPATH, "/html/body/div[4]/section[5]/div/div[2]/a")
        actions.scroll_to_element(exploreMorePokemon)
        actions.click(exploreMorePokemon)
        actions.perform()
        time.sleep(3)

        LoadMorePokemon = self.browser.find_element(By.XPATH, "/html/body/div[4]/section[5]/div[2]/a/span")
        actions.scroll_to_element(LoadMorePokemon)
        actions.click(LoadMorePokemon)
        actions.perform()
        time.sleep(3)

        SCROLL_PAUSE_TIME = 2 
        maximum_height = 10000

        # Get scroll height
        last_height = self.browser.execute_script("return document.body.scrollHeight")

        while True:
            # Scroll down to bottom
            self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)

            # Calculate new scroll height and compare with last scroll height
            new_height = self.browser.execute_script("return document.body.scrollHeight")
            if new_height > maximum_height:
                break
            last_height = new_height

        time.sleep(5)



        


    

    
    def tearDown(self): 
        self.browser.close() 


if __name__ == "__main__": 
    unittest.main()
    


    