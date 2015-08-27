#!/usr/bin/env python
#
# Setup for tournament.py

from tournament import *
tid = 5

def testRegister():
    registerPlayer("Chandra Nalaar")
    registerPlayer("Markov Chaney")
    registerPlayer("Joe Malik")
    registerPlayer("Mao Tsu-hsi")
    registerPlayer("Atlanta Hope")
    registerPlayer("Melpomene Murray")
    registerPlayer("Randy Schwartz")

    # c = countPlayers()
    # if c != 1:
    #     raise ValueError(
    #         "After one player registers, countPlayers() should be 1.")
    # print "4. After registering a player, countPlayers() returns 1."


if __name__ == '__main__':
    # testRegister()
    # raw_input("Success, all players created! Press Enter to continue...")
    # countPlayers(tid)
    # raw_input("Players counted. Press Enter to continue...")
    # createTournament("Titiiez")
    # deletePlayers()
    # countPlayers()
    # raw_input("Success, all entries deleted! Press Enter to continue...")
    # reportMatch(111, 116)
    print swissPairings()
    print "Success, all tests passed!"


