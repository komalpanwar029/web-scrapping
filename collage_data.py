from bs4 import BeautifulSoup
from pydash import py_
import requests
import csv

url = "https://hte.rajasthan.gov.in/dept/dce/college.php"
r =  requests.get(url)
print(r)
soup = BeautifulSoup(r.text ,"html5lib")
print(soup)

info =[]
headers = soup.select("div#collegelist table tr th")
for row in soup.select('div#collegelist table tr'):
  data = dict(
                {k.string:v.string for k, v in zip(headers, row.select("td"))},
                Link=py_.get(row.select_one('td a'), "attrs.href",''),
            )
  info.append(data)
print(info) 
 

csv_file_path = 'collage_data.csv'
# Writing the CSV file with header included only once
with open(csv_file_path, 'w', newline='') as csv_file:
    fieldnames = info[1].keys()  # Assuming all dictionaries have the same keys
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    # Write the header
    csv_writer.writeheader()

    # Write the data
    csv_writer.writerows(info)