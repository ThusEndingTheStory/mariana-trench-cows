import os

class colors:
	red = "\033[0;31m"
	green = "\033[0;32m"
	orange = "\033[0;33m"
	blue = "\033[0;34m"
	purple = "\033[0;35m"
	cyan = "\033[0;36m"
	white = "\033[0;37m" 
	black = "\033[0;30m"
	dark_black = "\033[0;90m"
	light_red = "\033[0;91m"
	light_green = "\033[0;92m"
	yellow = "\033[0;93m"
	light_blue = "\033[0;94m"
	magenta = "\033[0;95m"
	light_cyan = "\033[0;96m"
	light_white = "\033[0;97m"
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
