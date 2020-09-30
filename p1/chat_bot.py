from ai import *
def redy(inp):
	inp = list(inp)
	while True:
		try:
			inp.remove(".")
		except:
			try:
				inp.remove(",")
			except:
				try:
					inp.remove("!")
				except:
					try:
						inp.remove("?")
					except:
						i = ""
						for k in inp:
							i += k
						return i.lower()
ai = ai()
while True:
	inp = input("user: ")
	inp = redy(inp)
	try:
		ai.run(inp)
	except Exception as e: print(e)