CREATE TABLE tagless
(
	id INTEGER PRIMARY KEY,
	path TEXT NOT NULL,
	name TEXT NOT NULL
);
--
CREATE TABLE tags
(
	id INTEGER PRIMARY KEY,
	name TEXT NOT NULL,
	parent TEXT
);