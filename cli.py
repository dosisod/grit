from grit import grit

def main():
	gg=grit("config/")
	gg.add("test.py","123","321")
	gg.exit()

if __name__=="__main__":
	main()
