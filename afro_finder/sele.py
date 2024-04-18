import time
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from models import engine, Scholarship
from sqlalchemy.orm import sessionmaker

url = 'https://www.mastersportal.com/search/scholarships/master/computer-sciences'
headers = {"Accept-Language":"en-US,en;q=0.9,nl;q=0.8",

            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
            
            }
driver = uc.Chrome()

for i in range(1,3):
     print(i)
     print()
     driver.get(url + f'?page={i}')
     scholarship = driver.find_elements(By.CLASS_NAME, 'ScholarshipCard') 
     deadline_date = driver.find_elements(By.CLASS_NAME, 'ScholarshipCard')
     for element in scholarship: 
          name = element.find_element(By.CLASS_NAME, 'ScholarshipName').text
          location = element.find_element(By.CLASS_NAME, 'Location').text
          labels = element.find_elements(By.CLASS_NAME, 'QFValue')
          about = "{}".format(element.get_attribute("href"))
          grant, deadline = labels
          print(about)
          print(grant.text, ' ', deadline.text)

          Session = sessionmaker(bind=engine)
          session = Session()

          scholarship = Scholarship(name=name, location=location, about=about, grantt=grant.text, deadline=deadline.text)


          session.add(scholarship)
          session.commit()
          print("####################################################")

time.sleep(10)

driver.quit()


