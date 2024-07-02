# Project 5 Part 2
# Noah McAllister
# noahmcallister.github.io
# COP2002.0M1
# 6/29/2024
# Program that provides a menu of various terms that can be accessed by inputting the assigned number to the term.

import random

# Parallel arrays: Port numbers and corresponding protocols
port_numbers = [20, 21, 22, 23, 25, 53, 67, 68, 80, 110, 137, 139, 143, 161, 162, 389, 443, 445, 3389]
protocols = ["FTP", "FTP", "SSH", "Telnet", "SMTP", "DNS", "DHCP", "DHCP", "HTTP", "POP3", "NetBIOS", "NetBIOS", "IMAP", "SNMP", "SNMP", "LDAP", "HTTPS", "SMB", "RDP"]

def get_protocol_by_port(port):
    for i in range(len(port_numbers)):
        if port_numbers[i] == port:
            return protocols[i]
    return None

def get_port_by_protocol(protocol):
    for i in range(len(protocols)):
        if protocols[i] == protocol:
            return port_numbers[i]
    return None

def display_main_menu():
    print("\nMain Menu:")
    print("1. Given a port number, identify the PROTOCOL (use abbreviation).")
    print("2. Given a port protocol, identify a port NUMBER.")
    print("3. Exit")
    choice = input("\nChoice: ")
    return choice

def prompt_user_choice():
    while True:
        choice = display_main_menu()
        if choice == "1":
            print("\nOption 1: Identify the port's PROTOCOL.")
            print("----------------------------------------")
            while True:
                random_port = random.choice(port_numbers)
                user_input = input("\nWhat is the protocol for port {} (m=Main Menu)? ".format(random_port))
                if user_input == "m":
                    break
                elif user_input == "":
                    continue
                protocol = get_protocol_by_port(random_port)
                if user_input == protocol:
                    print("Correct answer!")
                else:
                    print("Incorrect. The correct answer is {}.".format(protocol))
        elif choice == "2":
            print("\nOption 2: Identify the port's NUMBER.")
            print("----------------------------------------")
            while True:
                random_protocol = random.choice(protocols)
                user_input = input("\nWhat is the number for protocol {} (m=Main Menu)? ".format(random_protocol))
                if user_input == "m":
                    break
                elif user_input == "":
                    continue
                port = get_port_by_protocol(random_protocol)
                try:
                    user_port = int(user_input)
                    if user_port == port:
                        print("Correct answer!")
                    else:
                        print("Incorrect. The correct answer is {}.".format(port))
                except ValueError:
                    print("Invalid input. Please enter a valid port number.")
        elif choice == "3":
            print("\nProgram Complete. I hope this has helped in studying for the CompTIA A+ certification.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

def main():
    prompt_user_choice()

if __name__ == "__main__":
    main()
