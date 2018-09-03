import BeautifulSoup as beautifulSoup
import requests
import csv
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

page = requests.get("http://data.marinemammals.gov.au/nmmdb/events/?event_class=[Sighting]&spatial_bounds=112.14844,-44.11177,155.03906,-9.69318")

driver = webdriver.Safari()
driver.get("http://data.marinemammals.gov.au/nmmdb/events/?event_class=[Sighting]&spatial_bounds=112.14844,-44.11177,155.03906,-9.69318")


with open('prueba.csv', mode="w") as csvFile:
    csvWriter = csv.writer(csvFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    soup = beautifulSoup.BeautifulSoup(page.text)
    while True:
        tableBody = soup.findAll('tbody')[0]
        tableContent = tableBody.findAll('tr')
        for child in tableContent:
            currentRow = child.findAll('td')
            csvWriter.writerow(("\'"+currentRow[2].string+"\'", currentRow[3].string, currentRow[4].string,
                                "\'"+currentRow[5].string+"\'", "\'"+currentRow[6].string+"\'", currentRow[7].string,
                                currentRow[8].string))
        try:
            driver.find_element_by_xpath('//*[@id="gridTab"]/div/div/div[2]/nav/ul/li/a[@aria-label="Next"]').click()
        except NoSuchElementException:
            break