import  requests
from bs4 import BeautifulSoup
url = "https://en.wikipedia.org/wiki/List_of_Marvel_Cinematic_Universe_films"
r = requests.get(url)
#print(r)
soup = BeautifulSoup(r.content ,"html.parser")
#print(soup.prettify)
#Beautifulsoup
print(type(soup))
#tag
print(type(soup.title))
#navigablestring
print(type(soup.title.string))
#title ,string
print(soup.title)
print(soup.title.string)
#find p 
respo_p = soup.find_all("p")
#print(respo_p)
#find a
respo_a = soup.find_all("a")
#print(respo_a)

print(soup.find('p')['class'])
print(soup.find('a')['class'])

#add the scraped data  to the dictionary
data_dict = {}
title = soup.find("h1" , class_ = "firstHeading")
release_date = soup.find("span" , class_ = "release-date")
director = soup.find("div", class_ = "director")
cast = [actor.text for actor in soup.find_all("div" , class_= "cast-member")]
box_office = soup.find("div" ,class_ = "box_office")
critics = soup.find("div" , class_ = "critics")
#data_dict["Title"] = title
#data_dict["Release_date"] = release_date
#data_dict["Director"] = director
#data_dict["Cast"] = cast
#data_dict["Box_office"] = box_office
#data_dict["critics"] = critics
#print the dictionary
#print(data_dict)

tables = soup.find_all("table",class_= 'wikitable')
table = tables[0]
for table in tables :
    rows = table.find_all("tr")
    for row in rows[1 :] :
        cells = row.find_all("td")
        if len(cells)>= 5:
            filim = cells[0].text.strip
            release_date =cells[1].text.strip()
            director =cells[2].text.strip()
            screen_writer= cells[3].text.strip()
            producer = cells[4].text.strip
           
            
            print(f"filim: {filim}" )
            print(f"release date: {release_date}" )
            print(f"director: {director}" )
            print(f"screen writer: {screen_writer}" )
            print(f" producer : { producer}" )
          
            
