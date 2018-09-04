import BeautifulSoup as beautifulSoup
import requests
import csv

""" 

HTML Scraper: Small script that obtains raw data from a web page, transforms it to CSV format and outputs it in a .csv file.
Educational purposes only.

@author: paolaos
@date: 04/09/18

"""

# Create and open a new CSV file, which will be used to dump all the raw data from the requested page
with open('whales.csv', mode="w") as csvFile:
    # CSV configuration: item delimiter is with commas, row delimiter is with enter space. Single quotes for strings.
    csvWriter = csv.writer(csvFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    # This makes sure to iterate through all the pages
    for counter in range(0, 525):
        # Requests the page from which the data will be extracted
        page = requests.get("http://data.marinemammals.gov.au/nmmdb/events/?event_class=[Sighting]&spatial_bounds=112.14844,-44.11177,155.03906,-9.69318&page=" + str(counter))
        # Extracts and loads the page's text in order to make way to the table
        soup = beautifulSoup.BeautifulSoup(page.text)
        # Finds the first matching element with the tbody tag
        tableBody = soup.findAll('tbody')[0]
        # Creates a list of all table rows
        tableContent = tableBody.findAll('tr')
        # Iterates through said list
        for child in tableContent:
            # Separates all items in a specific row
            currentRow = child.findAll('td')
            # Dumps the relevant contents to a CSV file by appending it as a tuple DS.
            # All string items are inserted with single quotes
            csvWriter.writerow(("\'"+currentRow[2].string+"\'", currentRow[3].string, currentRow[4].string,
                                "\'"+currentRow[5].string+"\'", "\'"+currentRow[6].string+"\'", currentRow[7].string,
                                currentRow[8].string))
