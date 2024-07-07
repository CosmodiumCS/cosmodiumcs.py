#!/bin/python3
# cosmodiumcs python library
# create by : bluecosmo

# imports
from cosmodiumcs import *

def main():
    ccs_confirm("Access granted")
    ccs_deny("Permission denied")
    ccs_error("Wrong password, try again")
    ccs_info("Created by : bluecosmo")
    ccs_input("Enter your name")
    ccs_pending("Connecting")
    ccs_warning("User activity is being logged")

if __name__ == "__main__":
    main()
