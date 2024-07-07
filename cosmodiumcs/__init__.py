#!/bin/python3
# cosmodiumcs python library
# created by : bluecosmo

# debugging & logging
ccs_confirm = lambda message: print(f"[+] {message}")
ccs_deny = lambda message: print(f"[-] {message}")
ccs_error = lambda message: print(f"[!] ERROR : {message}")
ccs_info = lambda message: print(f"[$] {message}")
ccs_input = lambda message: print(f"[~] {message} : ") # TODO: get user input??
ccs_pending = lambda message: print(f"[*] {message}...")
ccs_warning = lambda message: print(f"[!] {message}")
