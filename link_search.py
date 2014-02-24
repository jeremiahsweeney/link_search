from bs4 import BeautifulSoup
import urllib.request
import re 

website = 'http://www.youtube.com'
link_list = []

url = input('Enter the link of the webpage to search: ')
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page)
for link in soup.find_all('a', href=re.compile(website)):
    link_list.append(link['href'])

answer = input('Do you want to save the results to a .txt file? ')
if answer in ['yes','y']:
    new_file = open('results.txt', 'w')
    for x in link_list:
        y = str(x)
        new_file.write(y)
    new_file.close()
else:
    for i in link_list:
        print(i)
