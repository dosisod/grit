from grit import grit

def main():
	gg=grit("config/")
	gg.merge([[1,2,3,4],[1,1,1,1]])
	gg.exit()

if __name__=="__main__":
	main()
