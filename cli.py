from grit import grit

def main():
	gg=grit("config/") #open in folder config
	
	gg.select() #asks for what files we want
	
	gg.exit()

if __name__=="__main__":
	main()