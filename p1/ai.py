from states import *
from tokens import *
import sys
class ai:
	state = None
	def __init__(self):
		self.state = intro(self)
		self.name = None
		self.dir = False
	def run(self,inp):
		if self.dir:
			self.state.run(self,inp)
		else:
			inp = tokenizer(inp)
			for word in inp:
				if word == "quit":
					sys.exit()
				elif word == "restart":
					self.__init__()
					print("!!suscelfuly reset the bot!!")
			self.state.run(self,inp)
def tokenizer (inp):
	inp = conv(inp)
	output = []
	for word in inp:
		add = ["undifend", word]
		try:
			add = ["number", int(word)]
		except:
			for token in tokens:
				for words in token["words"]:
						if word == words:
								if token["only"]:
									add = token["id"]
								else:
									add = [token["id"], word]
		output.append(add)
	return output
def conv(inp):
	inp = list(inp)
	i = ""
	output = []
	for k in inp:
		if k == " ":
			output.append(i)
			i = ""
		else:
			i += k
	output.append(i)
	return output