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
	tid SERIAL primary key,
	name TEXT
);

CREATE TABLE matches (
	match_id SERIAL primary key,
	tid INT REFERENCES tournaments(tid),
	winner INT REFERENCES players(id),
	loser INT REFERENCES players(id),
	draw INT
);

CREATE TABLE scoreboard (
	match_id SERIAL,
	player INT REFERENCES players(id) ON DELETE CASCADE,
	score INT,
	matches INT,
	bye INT
);

CREATE TABLE results (
        player INT REFERENCES players(id) ON DELETE CASCADE,
        wins INT,
        matches INT
);

