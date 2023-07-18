import os
import requests
import urllib.request
from urllib.parse import urljoin
base_url="https://dude.docking.org/targets/"
from bs4 import BeautifulSoup
response=requests.get(base_url)
html_content=response.text
def get_subfolder_list(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    subfolder_list = []
    name_cells = soup.find_all("td", class_="name")
    for cell in name_cells:
        link = cell.find("a")
        if link:
            href = link["href"]
            subfolder_list.append(href)
    return subfolder_list

subfolder=get_subfolder_list(html_content)
print(subfolder)

for folder in subfolder:
    folder_name=folder.split('/')[-1]
    os.mkdir(folder_name)
    if "https://dude.docking.org/targets/" in folder:
        active_url=folder+"/marginal_actives_combined.ism"
        inactive_url = folder+"/marginal_inactives_combined.ism"
        urllib.request.urlretrieve(active_url, folder_name+"/marginal_actives_combined.ism")
        urllib.request.urlretrieve(inactive_url, folder_name+"/marginal_inactives_combined.ism")
