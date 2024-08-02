from termcolor import colored
from colorama import init

init()  # Initialize colorama for Windows compatibility
rainbow_text = colored("R", "red") + colored("a", "yellow") + colored("i", "green") + \
               colored("n", "cyan") + colored("b", "blue") + colored("o", "magenta") + \
               colored("w", "red")

print(rainbow_text)