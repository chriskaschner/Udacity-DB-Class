-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

CREATE TABLE players (
        id serial primary key,
        name text
);

CREATE TABLE tournaments (
	tournament_id SERIAL primary key,
	name TEXT
);

CREATE TABLE matches (
	match_id SERIAL,
	tournament_id INT REFERENCES tournaments(tournament_id),
	winner INT REFERENCES players(id),
	loser INT REFERENCES players(id),
	draw INT
);

CREATE TABLE scoreboard (
	match_id SERIAL,
	tournament_id INT REFERENCES tournaments(tournament_id)
	winner INT REFERENCES players(id),
	loser INT REFERENCES players(id),
	draw INT
);

