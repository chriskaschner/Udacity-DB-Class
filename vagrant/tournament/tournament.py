#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2

def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    pg = connect()
    c = pg.cursor()
    c.execute("DELETE FROM matches")
    pg.commit()
    pg.close()

def deletePlayers():
    """Remove all the player records from the database."""
    pg = connect()
    c = pg.cursor()
    c.execute("DELETE FROM players")
    pg.commit()
    pg.close()

def deleteTournaments():
    """Remove all the tournments records from the database."""
    pg = connect()
    c = pg.cursor()
    c.execute("DELETE FROM tournmaents")
    pg.commit()
    pg.close()

def deleteScoreboards():
    """Remove all the scoreboard records from the database."""
    pg = connect()
    c = pg.cursor()
    c.execute("DELETE FROM scoreboard")
    pg.commit()
    pg.close()

def createTournament(name):
    """Create new tournament"""
    pg = connect()
    c = pg.cursor()
    c.execute("INSERT INTO tournaments (name) VALUES (%s) RETURNING tid", (name,))
    tid = c.fetchone()[0]
    pg.commit()
    pg.close()
    return tid

def countPlayers(tid):
    """Returns the number of players currently registered."""
    pg = connect()
    c = pg.cursor()
    c.execute("SELECT count(*) AS num_players FROM players")
    num_players = c.fetchone()[0]
    pg.commit()
    pg.close()
    return num_players

def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    pg = connect()
    c = pg.cursor()
    c.execute("INSERT INTO players (name) VALUES (%s) RETURNING id", (name,))
    player_id = c.fetchone()[0]
    c.execute("INSERT INTO scoreboard (player, score, matches, bye) VALUES (%s,%s,%s,%s)", (player_id,0,0,0))
    c.execute("INSERT INTO results (player, wins, matches) VALUES (%s,%s,%s)", (player_id,0,0))
    pg.commit()
    pg.close()

def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    pg = connect()
    c = pg.cursor()
    c.execute("SELECT distinct results.player AS id, players.name AS name, results.wins AS wins, results.matches AS matches  FROM players, results WHERE players.id = results.player ORDER BY wins DESC")
    standings = c.fetchall()
    pg.commit()
    pg.close()
    return standings

    # SELECT scoreboard.player, players.name as name, results.wins AS wins, results.matches AS matches  FROM scoreboard, players, results WHERE players.id = scoreboard.player;


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    pg = connect()
    c = pg.cursor()
    temp_tournament_name = "temp place holder name"
    tid = createTournament(temp_tournament_name)
    c.execute("INSERT INTO matches (winner, loser) VALUES (%s, %s)", (winner, loser,))
    c.execute("UPDATE results SET wins = wins+1 WHERE player = (%s)", (winner,))
    c.execute("UPDATE results SET matches = matches+1 WHERE player = (%s) OR player = (%s)", (winner,loser,))
    pg.commit()
    pg.close()

def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    final_list = []
    standings = playerStandings()
    i = 0
    x = len(standings)
    while i < x:
        id1 = standings[i][0]
        name1 = standings[i][1]
        id2 = standings[i+1][0]
        name2 = standings[i+1][1]
        result = (id1, name1, id2, name2)
        final_list.append(result)
        i += 2
    return final_list


