import requests,pprint,json
from bs4 import BeautifulSoup


insta_url = "https://www.instagram.com/"+input("ENTER USERNAME     ")
responce = requests.get(insta_url)
soup = BeautifulSoup(responce.text,'html.parser')
# posts folloers and following
try:
	information = soup.find('meta',attrs={'property': 'og:description'})
	print(information['content'].split('-')[0])

	#### NAME 
	name = soup.find('script',attrs={'type':'application/ld+json'})
	Name = str(name).split('{')
	Name = Name[1].split(':')
	userName = Name[4].split(',')[0]
	username = Name[5].split(',')[0]
	bio = Name[6].split(',')[0]
	print(username,userName,"\n BIO  \n",bio)
except IndexError:
	print("ACCOUNT IS PRIVATE   ??!!!! ")

##########  Images

try:
	script= soup.find_all('script',attrs={ 'type':"text/javascript"})[3].contents
	link_list=[]
	for i in script:
		I=i.split("thumbnail_src")
		for ele in I:
			ELE = ele.split('"')
			link_list.append(ELE[2])
	link_list.pop(0)
	new_link_list=[]

	for j in link_list:
		new_link_list.append(j.replace('\\u0026','&'))

	pprint.pprint(new_link_list)
except IndexError:
	print("Images NOT FOUND !!!! \n ACCOUNT IS PRIVATE  ??!!!")

##########  Images

try:
	script= soup.find_all('script',attrs={ 'type':"text/javascript"})[3].contents
	link_list=[]
	for i in script:
		I=i.split("thumbnail_src")
		for ele in I:
			ELE = ele.split('"')
			link_list.append(ELE[2])
	link_list.pop(0)
	new_link_list=[]

	for j in link_list:
		new_link_list.append(j.replace('\\u0026','&'))

	pprint.pprint(new_link_list)
except IndexError:
	print("Images NOT FOUND !!!! \n ACCOUNT IS PRIVATE  ??!!!")


