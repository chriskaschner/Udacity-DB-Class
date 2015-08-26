#!/usr/bin/env python
#
# Setup for tournament.py

from tournament import *
import psycopg2

def testRegister():
    registerPlayer("Chandra Nalaar")
    registerPlayer("Markov Chaney")
    registerPlayer("Joe Malik")
    registerPlayer("Mao Tsu-hsi")
    registerPlayer("Atlanta Hope")

    # c = countPlayers()
    # if c != 1:
    #     raise ValueError(
    #         "After one player registers, countPlayers() should be 1.")
    # print "4. After registering a player, countPlayers() returns 1."


if __name__ == '__main__':
    testRegister()
    raw_input("Success, all players created! Press Enter to continue...")
    countPlayers()
    raw_input("Players counted. Press Enter to continue...")
    deletePlayers()
    countPlayers()
    raw_input("Success, all entries deleted! Press Enter to continue...")
    print "Success, all tests passed!"


