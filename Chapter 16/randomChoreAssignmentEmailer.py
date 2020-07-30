"""
Assign randomised chores to people and email them their appointed task.
"""

import random
import smtplib


def get_chore(email, last_chore):
    """
    Randomly selects a chore that isn't the 'last_chore the person had.
    """
    chore_list = chores[:]
    try:
        chore_list.remove(last_chore)
    except ValueError:
        pass
    if chore_list:
        new_chore = random.choice(chore_list)
        chore_assignments[email] = new_chore
        chores.remove(new_chore)
    else:
        print('Reshuffling as a chore would have to have been repeated.')


def send_chore(email, chosen_chore):
    """
    Emails the address with chore details.
    """
    smtp_obj.sendmail('Example@Email.com', email, 'Subject: This Weeks Chore.'
                                                  '/n You have been randomly assigned ' + chosen_chore
                      + '. You will not receive this chore next time.')


with open('last_chores.txt') as f:
    last_chores = f.readlines()
