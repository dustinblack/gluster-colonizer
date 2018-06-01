from termios import tcflush, TCIOFLUSH
import sys
import readline
from subprocess import *
import shlex

def user_input(msg, initial=''):
    # Function to capture raw_input w/ key buffer flush
    tcflush(sys.stdin, TCIOFLUSH)
    readline.set_startup_hook(lambda: readline.insert_text(initial))
    keyin = raw_input(msg)
    return keyin

def yes_no(answer, abortSetup='', do_return=False, default='yes'):
    # Simple yes/no prompt function
    yes = set(['yes', 'y', 'ye'])
    no = set(['no', 'n'])
    if default is 'no':
        no.add('')
    else:
        yes.add('')
    while True:
        choice = user_input(answer).lower()
        if choice in yes:
            return True
        elif choice in no:
            if do_return:
                return False
            else:
                abortSetup("Deployment cancelled by user.")
        else:
            print "Please enter either 'yes' or 'no'\r\n"
