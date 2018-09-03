import BeautifulSoup as beautifulSoup
import requests
import csv

# first step: request the webpage I need for data extraction

page = requests.get("https://data.marinemammals.gov.au/nmmdb/events/?event_class=[Sighting]&spatial_bounds=112.14844,-44.11177,155.03906,-9.69318")

soup = beautifulSoup.BeautifulSoup(page.text)

tableBody = soup.findAll('tbody')[0]

tableContent = tableBody.findAll('tr')

with open('prueba.csv', mode="w") as csvFile:
    csvWriter = csv.writer(csvFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for child in tableContent:
        currentRow = child.findAll('td')
        csvWriter.writerow(("\'"+currentRow[2].string+"\'", currentRow[3].string, currentRow[4].string, "\'"+currentRow[5].string+"\'",
                            "\'"+currentRow[6].string+"\'", currentRow[7].string, currentRow[8].string))



#csvRows = list()

#for child in tableContent:
#    currentRow = child.findAll('td')
#    csvRows.append(("\""+currentRow[2].string+"\"", currentRow[3].string, currentRow[4].string, "\""+currentRow[5].string+"\"",
#                    "\""+currentRow[6].string+"\"", currentRow[7].string, currentRow[8].string))

#for i in csvRows:
#    for j in i:
#        print(j)
#    print("*********")