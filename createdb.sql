CREATE DATABASE kanjibridge;

use kanjibridge;

CREATE TABLE kanji (
       id INT,
       glyph char(4),
       onyomi TEXT,
       kunyomi TEXT,
       keyword TEXT,
       meaning TEXT,
       PRIMARY KEY(id)
);


#       id INT NOT NULL AUTO_INCREMENT,

# INSERT INTO kanji VALUES (1, '')

CREATE TABLE kanjitags (
       id INT,
       name TEXT
);


CREATE TABLE words (
       id INT NOT NULL AUTO_INCREMENT,
       kanji varchar(40),
       kana TEXT,
       english TEXT,
       PRIMARY KEY (id)
);

CREATE TABLE onyomi (
       yomi TEXT,
       id INT
);