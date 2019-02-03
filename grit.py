import os
import hashlib
import tarfile
import requests
import base64 as b64
from simplecsv import simplecsv

class grit:
	def __init__(self, dir, quiet=False):
		if not quiet:
			print("GRIT - Decentralized Code Storage - github.com/dosisod/GRIT\n") #prints banner
	
		self.dir=dir #folder storing IPs and index
		self.home=os.getcwd() #stores where this file is ran from
		if not os.path.exists(self.dir):
			os.makedirs(self.dir)

		self.indexsc=simplecsv(self.dir+"index", "a+") #reads index csv
		self.index=self.indexsc.table

		self.ipsc=simplecsv(self.dir+"ips", "a+", delim=".") #IP simplecsv obj
		self.ips=[]
		for i in self.ipsc.table: #array from csv file
			temp=[] #temp array for storing values
			for j in i:
				temp.append(int(j)) #IPs must be converted into ints
			self.ips.append(temp) #appends IP to array

	def ask(self): #ask for desc and name for file
		print("These are for your own reference, others will not see this")
		self.name=input("  Name your project: ")
		self.desc=input("  Describe your project: ")

	def add(self, file, name, desc): #adds hashes and other info to index file
		row=[]
		with open(file, "rb") as f: #TODO: pass tarfile to this
			row.append(b64.b64encode(hashlib.sha512(f.read()).digest()).decode()) #saves file hash and full path to csv
			row.append(os.path.realpath(f.name))

		row.append(name)
		row.append(desc)
		self.indexsc.writerow(row) #push data to index csv

	def download(self):
		pass

	def uploader(self, file): #uploader loop
		pass
		#loop through ip list
		
	def upload(self, file, ip): #will upload file
		pass

	def zip(self, input, output): #zips up a file
		self.tarn=output+".tar.bz2"
		tar=tarfile.open(output+".tar.bz2", "w:bz2")
		tar.add(input) #works for folders to
		tar.close()

	def select(self): #file(s) to upload
		while True:
			cwd=os.getcwd()+"/" #default path is current dir
		
			path=input("Base path of project ("+cwd+"): ") #get path to root of file, enter is current dir
			if not path:
				path=cwd

			file=input("File/folder name of project: ")

			self.filen=path+file

			if os.path.exists(self.filen):
				break
			else:
				print("Project \""+self.filen+"\" not found\n")

		self.ask() #get descriptors for file
		self.zip(self.filen, self.dir+"last") #zip file
		self.add(self.tarn, self.name, self.desc) #add file info to index
		self.uploader(self.filen) #sends file to uploader

	def merge(self, ips): #appends unique IPs to IP file
		with open(self.dir+"ips", "a") as f:
			newips=[] #var for storing new IPs
			for i in ips:
				if i not in self.ips:
					newips.append(i) #append to new list if not in current list
			self.ipsc.writerows(newips)

	def exit(self): #closes everything down
		self.ipsc.close()