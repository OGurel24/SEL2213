from selenium import webdriver
import unittest
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

class AmazonSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.set_page_load_timeout(20)
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()
        self.driver.get("https://www.amazon.com/")

        #Adding necessary cookies
        cookie1 = {'name':'a-ogbcbff', 'value':'1'}
        self.driver.add_cookie(cookie1)
        
        cookie2 = {'name':'at-main', 'value':'Atza|IwEBIP8G5cPGny4yxq6SWtDCbF60AcBICZz7-3-A16fRF-Gzm5qd2335_eTJpgutAilKq_sDmgJzU5IQsTxomXnn8833Xqu3lFO7v6RglSiYh3GCvNAOBJzW7_C6I4-fDjZO5dlWveqU-eZVC3gQv4qquOZPLzJKxbEfW-shtCPw6cVmJYM3UCJCrYOKtpfeOSz_TFu6VDscHfns389xH_6V4pOP7N2WAII2nfgqbCgMHPE_sXC12CdCAXnggsjyFpWLAxFbgXipyolN5bWu2lhEYKfroVvcOso_6JlFe9JcUprOYaXMxupD-7XZkgjX_hY-rMigw_xCTZ4xwJ5CmFisi2jQR9bac5UyCNSVF1UiTOq7F18t9QYh6n8KH9P6Xhs5KCYLFO6HOE0a8-oQySgtJ-RU'}
        self.driver.add_cookie(cookie2)

        cookie3 = {'name':'sess-at-main', 'value':'"+pSbPQpb5PY4hb75sK9dUTFRa3E5utixQo8a8I/gakU="'}
        self.driver.add_cookie(cookie3)

        cookie4 = {'name':'session-id', 'value':'131-3130701-5319519'}
        self.driver.add_cookie(cookie4)   

        cookie5 = {'name':'session-token', 'value':'"KnCViIQQ2Tw6m1DiVifJl7XGaOprelHGmXhwKGno1pFDhyDZqh/JWBADzEMrk9obmAqhiFgk3/XZAEenkCQ0kiW35EqaAg9dpejiQk0+3u6pI9f9pBsWrXJEx/e/LuipZcnyNm9ae0nejpFv/yNLMKxVrUnZS9kpLij8dONyWduh2h6smJ8xyrVfFvfO7YSZjDts5s9yTHs+eFR15njS+goWujI136vlzxWPpDzG3rcHKXDfoBZpSNI2Lt/wOQoVrsliklwnN2NW8WXo1ZDenw=="'}
        self.driver.add_cookie(cookie5)

        cookie6 = {'name':'sp-cdn', 'value':'"L5Z9:TR"'}
        self.driver.add_cookie(cookie6)

        cookie7 = {'name':'sst-main', 'value':'Sst1|PQHOeanSyKltHj4MEJU43PpcC0Zb3gTTUyTitAa832lqt-T7rLWDutFUS4Cn023Kkdz6krBfe3UxkRiBETFXJJLomdgFycBFTc9GbjCRn8oEp0tSCD88GEnjaiWf5tgHl9GMUY-Ra0eex0dfHWiSU4SNnKi7kz6xk6r7oYiDTyTgQMk_7BhT5yniI42Ygihrif6N1aZwXPYX3tyn4gvXPLwbtrNZuqPDXW4HMLmRnQ9woj0LkCMkYolGjYygaYSDEVfXwSFZIwyJ71VTWiqtbEFiiLEVrqe_N1xX4CBbTbFa4fDYjp2AXqvl1628a3FnHQR2YPLv9JM9fECWlDQeScBE8g'}
        self.driver.add_cookie(cookie7)

        cookie8 = {'name':'ubid-main', 'value':'135-4793041-7411221'}
        self.driver.add_cookie(cookie8)

        cookie9 = {'name':'x-main', 'value':'"KfHeyIJ@2lQv34sNXlH7m04H?5qK2wAyUxLt1mOaB74Oxrgyw@YjpoDp3T2YwI?T"'}
        self.driver.add_cookie(cookie9)

        cookie10 = {'name':'x-wl-uid', 'value':'1YwZm/LPj030FfWcs+3cEhY2x6kaj5WfiULOOKHxxVsRXzK7j+AXASirvqCarjfzBZr8N/ZywNTMZFBhYrGnp86GmLH3hPebLU9na3k++ywQq9mmK9Bs9fCsXS/P5ETj+ACty58j/PnM='}
        self.driver.add_cookie(cookie10)

        
    def test_Onur(self):
        self.assertEqual(self.driver.current_url,'https://www.amazon.com/') #checking whether the current page is www.amazon.com or not

        login_button=self.driver.find_element_by_xpath('//*[@id="nav-link-accountList"]/span[2]') #locating login button
        login_button.click()
        self.driver.find_element_by_xpath('//*[@id="ap-account-switcher-container"]/div[1]/div/div/div[2]/div[1]').click()
        password_form=self.driver.find_element_by_name("password") #locating password entry button
        password_form.send_keys("987654")
        password_form.submit() #submit corresponding e-mail and password
    
        search_bar = self.driver.find_element_by_name('field-keywords') #locating product search bar
        search_bar.send_keys('samsung') 
        search_bar.submit() # submitting for to search for samsung 

        searched_keyword=self.driver.find_element_by_xpath('//*[@id="search"]/span/h1/div/div[1]/div/div/span[3]').text # locating the element of searched keyword
        self.assertEqual ( searched_keyword, '"samsung"' ) # compare the searching word with samsung, searching keyword must be samsung

        self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div[2]/div/span[7]/div/div/div/ul/li[3]/a').click() # second page of the searched products

        product=self.driver.find_element_by_xpath('//*[@id="search"]/div[1]/div[2]/div/span[3]/div[1]/div[1]/div/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/div[1]/h2/a')#dsired product
        product_text=product.text  #text of the product
        product.click()
            
        self.driver.find_element_by_xpath('//*[@id="add-to-wishlist-button"]').click() #adding product to wish list
        add_to_wish_list_button=self.driver.find_element_by_xpath('//*[@id="atwl-list-privacy-HKXHXOZNB7GD"]')
        add_to_wish_list_button.click()

        self.driver.refresh()

        ActionChains (self.driver).move_to_element( self.driver.find_element_by_xpath('//html/body/div[2]/header/div/div[2]/div[2]/div/a[2]/span[2]') ).perform()
        self.driver.find_element_by_link_text('Wish List').click() #entering to wish list
        
        self.driver.find_element_by_name('submit.deleteItem').click() #delete matching item

                
    def tearDown(self):
        self.driver.close()
              
        
unittest.main()        
