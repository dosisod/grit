import os
import hashlib
import tarfile
import requests
import base64 as b64
from simplecsv import simplecsv

class grit:
	def __init__(self, dir):
		self.dir=dir #folder storing IPs and index
		self.home=os.getcwd() #stores where this file is ran from
		if not os.path.exists(dir):
			os.makedirs(dir)

		self.indexsc=simplecsv(self.dir+"index", "w+") #reads index csv
		self.index=self.indexsc.table

		self.ipsc=simplecsv(self.dir+"ips", "w+", delim=".") #IP simplecsv obj
		self.ips=[]
		for i in self.ipsc.table: #array from csv file
			temp=[] #temp array for storing values
			for j in i:
				temp.append(int(j)) #IPs must be converted into ints
			self.ips.append(temp) #appends IP to array

	def add(self, file, name, desc): #adds hashes and other info to index file
		row=[]
		with open(file, "r") as f: #TODO: pass tarfile to this
			row.append(b64.b64encode(hashlib.sha512(f.read().encode()).digest()).decode()) #saves file hash and full path to csv
			row.append(os.path.realpath(f.name))

		row.append(name)
		row.append(desc)
		self.indexsc.writerow(row) #push data to index csv

	def download(self):
		pass

	def upload(self, file, ip): #will upload file
		pass

	def zip(self, input, output): #zips up a file
		tar=tarfile.open(output+".tar.bz2", "w:bz2")
		tar.add(input) #works for folders to
		tar.close()

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
