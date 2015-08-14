from os import system, popen
from time import sleep
system('clear')
# in which I attempt to reproduce the machinations of the game engine 

class screen():
	def colsize(self): 
		c = popen('stty size').read().split()
		return int(c[1])

	def rowsize(self):
		r = popen('stty size').read().split()
		return int(r[0])

	def clear(self):
		clearscreen = popen('clear').read()
		return clearscreen

	def half(self):
		pass

	def p(self, string1):
		n = (self.colsize()/2-(len(string1))/2) * " "
		print n, string1

	def nonp(self, string1):
		n = (self.colsize()/2-(len(string1))/2) * " "
		print n,

	def r(self, string1):
		n = (self.colsize() - len(string1)) * " "
		print n,

class Scene(object):
	def enter(self): 
		print "This is not yet configured." 
		exit(1)

class TheEntrance(Scene):

	def enter(self):
		c = screen()
		c.p("What you see is ordinary beyond belief.")
		c.p("Your eyes behold a living room with a couch.")
		c.p("There is also a chair, a color television set,")
		c.p("and a rug that is a brown oval that blends with")
		c.p("the rest of the floor.")
		c.p("WHY ARE YOU HERE?")
		c.nonp("Would you like to go to the next room? (y/n)")
		g = raw_input("Would you like to go to the next room? (y/n)")
		if g == "y": 
			val = Kitchen()
			return val.enter()
		elif g == "n":
			val = Exit()
			return val.enter()
			exit(1)
		else: 
			c.p("I don't get '" + g + ".'")
			c.p("Skedaddle.\n\n")
			exit(1)

class Kitchen(Scene):
	def enter(self):
		c = screen()
		c.p("\n")
		c.p("You are now in the kitchen.")
		c.p("If possible, this is even less exciting!")
		c.p("Pots, pans, a stove, microwave, counter...")
		c.p("If these things excite you, feed yourself")
		c.p("a snack right away!\n\n")
		return None

class Exit(Scene):
	def enter(self):
		c = screen()
		c.p("\n")
		c.p("You leave as you entered this world. Naked.")
		c.p("Also, it's raining.")
		c.p("' '" * 10 + "\n\n")
		exit(1)


def main():
	scene1 = TheEntrance()
	scene1.enter()

if __name__ == "__main__": main()

