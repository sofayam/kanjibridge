CREATE DATABASE kanjibridge;

use kanjibridge;

CREATE TABLE kanji (
       id INT,
       glyph char(4),
       onyomi varchar(400),
       kunyomi varchar(400),
       keyword varchar(400),
       meaning varchar(400),
       PRIMARY KEY(id)
);


#       id INT NOT NULL AUTO_INCREMENT,

# INSERT INTO kanji VALUES (1, '')

CREATE TABLE kanjitags (
       id INT,
       name varchar(40)
);


CREATE TABLE words (
       id INT NOT NULL AUTO_INCREMENT,
       kanji varchar(40),
       kana varchar(400),
       english varchar(400),
       PRIMARY KEY (id)
);