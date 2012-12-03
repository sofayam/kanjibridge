CREATE DATABASE kanjibridge;

use kanjibridge;


CREATE TABLE kanji (

       id INT,
       glyph char(4),
       onyomi varchar(100),
       kunyomi varchar(100),
       keyword varchar(100),
       meaning varchar(100),
       PRIMARY KEY(id)
);


#       id INT NOT NULL AUTO_INCREMENT,

# INSERT INTO kanji VALUES (1, '')