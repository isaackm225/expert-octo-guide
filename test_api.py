import requests
import os 
import json
from bs4 import BeautifulSoup as bs
import csv

class Email_Bot():
	def __init__(self):
		self.RAPID_API_KEY = os.getenv('RAPID_API_KEY')

	def get(self)->tuple:
		url = "https://temp-gmail.p.rapidapi.com/get"
		querystring = {"domain":"gmail.com","username":"random","server":"server-1","type":"real"}
		headers = {
			"X-RapidAPI-Key": self.RAPID_API_KEY,
			"X-RapidAPI-Host": "temp-gmail.p.rapidapi.com"
	}
		response = requests.request("GET", url, headers=headers, params=querystring)
		data = (json.loads(response.text))

		if data['code'] == 200:
			cred = data['items'] #credentials
			email = cred['email']
			timestamp = cred['timestamp']
			return email,timestamp	
		else:
			raise Exception(f"Request failed generating email. Code: {data['code']}")


	def check(self,email:str,timestamp:str)->str:
		url = "https://temp-gmail.p.rapidapi.com/check"
		querystring = {"email":email,"timestamp":timestamp}
		headers = {
			"X-RapidAPI-Key": self.RAPID_API_KEY,
			"X-RapidAPI-Host": "temp-gmail.p.rapidapi.com"
		}
		response = requests.request("GET", url, headers=headers, params=querystring)
		data = (json.loads(response.text))
		if data['code'] == 200:
			try:
				item = data['items'][0]
				return item['mid'] #returns message ID
			except:
				print("No emails")
		else:
			raise Exception(f"Request failed while checking email. Email: {email}; Timestamp: {timestamp} Code: {data['code']}")
		

	def read(self,email:str,mid:str)->str:
		url = "https://temp-gmail.p.rapidapi.com/read"
		querystring = {"email":email,"message_id":mid}
		headers = {
			"X-RapidAPI-Key": self.RAPID_API_KEY,
			"X-RapidAPI-Host": "temp-gmail.p.rapidapi.com"
		}
		response = requests.request("GET", url, headers=headers, params=querystring)
		data = (json.loads(response.text))
		if data['code'] == 200:
			item = data['items']
			body = item['body']
			soup = bs(body, 'html.parser')
			
			if soup.p.text:
				a_tags = soup.find_all('a')
				u = a_tags[1]['href']
			return u
		else:
			raise Exception(f"Request failed while reading msg. Email: {email}; MID: {mid} Code: {data['code']}")

if __name__=="__main__":
	b = Email_Bot()
	email,t = b.get()

	mid = b.check(email,t)
	if mid:
		txt = b.read(email,mid)
		print(txt)