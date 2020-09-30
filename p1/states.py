from time import ctime
from config import *
from random import randint
from ball import *
from respons import *
def rep (reps):
	return reps[int(randint(0,len(reps)-1))]
class intro:
	def __init__(self,ai):
		ai.dir = False
	def run (self,ai,inp):
		for word in inp:
			if word == "hello":
				print("bot: " + rep(hello))
				ai.state = name(ai)
class name:
	def __init__(self,ai):
		ai.dir = False
	def run(self,ai,inp):
		for word in inp:
			try:
				word.remove("undifend")
				ai.name = word[0]
				print("bot: " + rep(namequess) + " " + ai.name + "?")
				ai.state = nameright(ai)
				break
			except:
				self.me = True
class nameright:
	def __init__(self,ai):
		ai.dir = False
	def run(self,ai,inp):
		for word in inp:
			try:
				word.remove("answer")
				if word[0] == "yes":
					print("bot: " + rep(namerig) + ai.name + "!")
					ai.state = nutral(ai)
				else:
					print("bot: " + rep(namewrong))
					ai.state = name(ai)
			except:
				self.me = True
class nutral:
	def __init__(self,ai):
		ai.dir = False
	def run(self,ai,inp):
		sent = ""
		und = 0
		rand = []
		for word in inp:
			if word == "time":
				print("bot: " + rep(time) + ctime())
			elif word == "thanks":
				print("bot: " + rep(thanks))
			elif word[0] == "question":
				if word[1] == "who" or word[1] == "what":
					sent = "what"
				elif word[1] == "why":
					sent = "why"
				und += 1
			elif word == "bot":
				if sent == "what":
					print("bot: " + rep(am) + author)
				elif sent == "why":
					print("bot: " + rep(why))
				else:
					und += 1
			elif word == "rep_thanks":
				print("bot: " + rep(rep_thanks))
			elif word == "random":
				sent = "random"
			elif word[0] == "number":
				if sent == "random":
					rand.append(word[1])
			elif word == "user":
				sent += " user"
			elif word[0] == "object":
				if word[1] == "name" and sent == "what user":
					print("bot: " + rep(nameget) + ai.name)
			elif word == "ball":
				print(" 8 ball: " + rep(ans))
				break
			elif word[0] == "action":
				if word[1] == "play":
					sent = "play"
			elif word[0] == "games" and sent == "play":
				if word[1] == "echo":
					ai.state = echo(ai)
				elif word[1] == "quess":
					ai.state = quess(ai)
			else:
				und += 1
			if len(rand) == 2:
				print("bot: " + rep(random) + str(randint(rand[0],rand[1])))
		if und == len(inp):
			print("bot: sorry, I dont have a respond to that string, you can ask " + author + " to make it work.")
class echo:
	def __init__(self,ai):
		print("bot: " + rep(game))
		ai.dir = True
	def run(self,ai,inp):
		if inp == "quit" or inp == "stop":
			print("bot: " + rep(gamestop))
			ai.state = nutral(ai)
		else:
			print("bot: " + inp)
class quess:
	def __init__(self,ai):
		ai.dir = False
		self.num = randint(0,quedif)
		print("bot: " + rep(game))
	def run(self,ai,inp):
		for word in inp:
			if word[0] == "number":
				num = word[1]
				if num < self.num:
					print("bot: " + rep(small))
				elif num > self.num:
					print("bot: " + rep(big))
				else:
					print("bot: " + rep(correct))
					ai.state = nutral(ai)
			elif word == "stop":
				print("bot: " + rep(gamestop))
				ai.state = nutral(ai)