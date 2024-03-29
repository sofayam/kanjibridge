CREATE DATABASE kanjibridge DEFAULT CHARACTER SET 'UTF8';

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

CREATE TABLE kanjitags (
       id INT,
       name TEXT,
       created TIMESTAMP DEFAULT NOW()
);

CREATE TABLE wordtags (
       id INT,
       name TEXT,
       created TIMESTAMP DEFAULT NOW()
);

CREATE TABLE words (
       id INT NOT NULL AUTO_INCREMENT,
       kanji varchar(40),
       kana TEXT,
       english TEXT,
       PRIMARY KEY (id),
       created TIMESTAMP DEFAULT NOW()
) DEFAULT CHARACTER SET 'UTF8' ;

CREATE TABLE onyomi (
       yomi TEXT,
       id INT
);