#!/usr/bin/env python
#
# Setup for tournament.py

from tournament import *

def deleteRows():
    pg = psycopg2.connect("dbname=tournament")
    c = pg.cursor()
    c.execute("DELETE FROM players")
    print "It is finished"

    pg.commit()
    pg.close()
    

if __name__ == '__main__':
    deleteRows()
#    print "Rows cleared"


