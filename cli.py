from grit import grit

def main():
	gg=grit("config/")
	
	gg.select()
	
	#gg.add("test.py","123","321")
	#gg.zip("test.py","out")
	gg.exit()

if __name__=="__main__":
	main()