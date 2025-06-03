from django.core.management.base import BaseCommand
from crawling.models import Match
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import tempfile

class Command(BaseCommand):
  help = 'Crawl LCK Match'

  def handle(self, *args, **options):
      self.crawling_match()
  
  def crawling_match(self):
    
    options = Options()
    options.binary_location = '/usr/bin/chromium'
    options.add_argument('--headless')
    options.add_argument('--window-size=1920x1080')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--headless=new')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-extensions')
    options.add_argument('--remote-debugging-port=9222')  # Specify a port
    options.add_argument('--disable-setuid-sandbox')
    options.add_argument("--incognito")
    options.add_argument("--disable-application-cache")
    options.add_argument("--enable-do-not-track")
    options.add_argument("--disable-popup-blocking")
    profile_dir = tempfile.mkdtemp()
    options.add_argument(f'--user-data-dir={profile_dir}')


    service = Service('/usr/bin/chromedriver') 
    driver = webdriver.Chrome(service=service, options=options)

    
    search_url = "https://game.naver.com/esports/League_of_Legends/schedule/lck"
    driver.get(search_url)
    driver.implicitly_wait(10)
    
    cards = driver.find_elements(By.CLASS_NAME, "card_item__3Covz")
    
    for card in cards:
      
      match_date = card.find_element(By.CLASS_NAME, "card_date__1kdC3").text
      eachDay = card.find_elements(By.CLASS_NAME, "row_item__dbJjy")
      
      for each in eachDay: 
        match_time = each.find_element(By.CLASS_NAME, "row_time__28bwr").text
        
        team_a = each.find_element(By.CLASS_NAME,"row_home__zbX5s")
        a_name = team_a.find_element(By.CLASS_NAME,"row_name__IDFHz").text
        if a_name != "TBD":
          a_url = team_a.find_element(By.CLASS_NAME,"row_logo__c8gh0").get_attribute('src')
        else:
          a_url =""
        
        team_b = each.find_element(By.CLASS_NAME, "row_away__3zJEV")
        b_name = team_b.find_element(By.CLASS_NAME,"row_name__IDFHz").text
        if b_name != "TBD":
          b_url = team_b.find_element(By.CLASS_NAME,"row_logo__c8gh0").get_attribute('src')
        else:
          b_url=""

        Match.objects.update_or_create(
            team_a=a_name,
            team_b=b_name,
            match_date=match_date,
            match_time=match_time,
            defaults={
                'a_logo': a_url,
                'b_logo': b_url,
            }
        )

    self.stdout.write(self.style.SUCCESS(f"Successfully processed match: {a_name} vs {b_name}"))

    driver.close()
