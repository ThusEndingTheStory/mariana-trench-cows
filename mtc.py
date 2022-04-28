import os

class colors:
	Red = "\033[0;31m"
	Green = "\033[0;32m"
	Orange = "\033[0;33m"
	Blue = "\033[0;34m"
	Purple = "\033[0;35m"
	Cyan = "\033[0;36m"
	White = "\033[0;37m" 
	Black = "\033[0;30m"
	black = "\033[0;90m"
	red = "\033[0;91m"
	green = "\033[0;92m"
	yellow = "\033[0;93m"
	blue = "\033[0;94m"
	magenta = "\033[0;95m"
	cyan = "\033[0;96m"
	white = "\033[0;97m"
	cyan_back="\033[0;46m"
	pink_back="\033[0;45m"
	white_back="\033[0;47m"
	blue_back="\033[0;44m"
	orange_back="\033[0;43m"
	green_back="\033[0;42m"
	red_back="\033[0;41m"
	grey_back="\033[0;40m"
	bold = "\033[1m"
	underline = "\033[4m"
	italic = "\033[3m"
	darken = "\033[2m"
	normal = "\033[0m"

class console:
	def write(text, color=None):
		if color == None:
			print(text)
		else:
			print(color + text + colors.normal)

	def clear():
		os.system("clear")

	def newline(width=None, char="–"):
		size = os.get_terminal_size()[0]
		if width == None:
			print(char*size)
		else:
			print(char*round(int(width)))
