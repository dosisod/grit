import os
import hashlib
import requests
from simplecsv import simplecsv

class grit:
	def __init__(self, dir):
		self.dir=dir #folder storing IPs and index
		if not os.path.exists(dir):
			os.makedirs(dir)

		self.ipsc=simplecsv(self.dir+"ips", "r+", delim=".") #IP simplecsv obj
		self.ips=[]
		for i in self.ipsc.table: #array from csv file
			temp=[] #temp array for storing values
			for j in i:
				temp.append(int(j)) #IPs must be converted into ints
			self.ips.append(temp) #appends IP to array

	def prep(self): #preps file?
		pass

	def download(self):
		pass

	def upload(self): #will upload file
		pass

	def zip(self, input, output): #zips up a file
		pass

	def select(): #file(s) to upload
		pass

	def merge(self, ips): #appends unique IPs to IP file
		with open(self.dir+"ips", "a") as f:
			newips=[] #var for storing new IPs
			for i in ips:
				if i not in self.ips:
					newips.append(i) #append to new list if not in current list
			self.ipsc.writerows(newips)

	def exit(self): #closes everything down
		self.ipsc.close()
