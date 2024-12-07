import urllib.request as u
import pyfiglet
from termcolor import colored

print(colored("************************************************************", "red"))
print(colored("************************************************************", "red"))
print(colored("*************** Website source code ************************", "magenta"))
print(colored("*******************🔥HACKER🔥*******************************", "magenta"))
print(colored("************************************************************", "red"))
print(colored("************************************************************", "red"))
print(colored("Loading ██████ 100% 🔴🔴🔴", "blue"))

banner = colored(pyfiglet.figlet_format("Website Cloud"), "yellow")
print(banner)

# User input for website name
print(colored("**********************************************", "red"))
web_name = input(colored("🔒 Enter Your Target Website:➤ ", "green"))
print(colored("**********************************************", "red"))

# Open the URL
try:
    source = u.urlopen(web_name)
    # Read the content
    source_read = source.read().decode('utf-8')
    # Print the content
    print(source_read)
except Exception as e:
    print(colored(f"Error: {e}", "red"))


