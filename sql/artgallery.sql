-- SQL Code for Database Creation (Forward Engineering)
-- Database: `art_gallery`

CREATE DATABASE IF NOT EXISTS `art_gallery`;
USE `art_gallery`;

-- Table `artist`
CREATE TABLE IF NOT EXISTS `artist` (
    `artist_id` INT NOT NULL AUTO_INCREMENT,
    `artist_name` VARCHAR(255) NOT NULL,
    `country` VARCHAR(255) NOT NULL,
    PRIMARY KEY (`artist_id`)
) ENGINE = InnoDB;

ALTER TABLE `artist`
MODIFY COLUMN `artist_id` INT NULL;

-- Table `artist`
ALTER TABLE `artist`
ADD COLUMN  `local` VARCHAR(255) NOT NULL,
ADD COLUMN  `dod` INT NOT NULL,
ADD COLUMN  `dob` INT NOT NULL,
ADD COLUMN  `dod` INT NOT NULL,
ADD COLUMN  `artist_middlename` VARCHAR(255) NOT NULL,
ADD COLUMN  `artist_lastname` VARCHAR(255) NOT NULL,
ENGINE = InnoDB; 

-- Table `artwork`
CREATE TABLE IF NOT EXISTS `artwork` (
    `artwork_id` INT NOT NULL AUTO_INCREMENT,
    `artist_id` INT NOT NULL,
    `title` VARCHAR(255) NOT NULL,
    `year` INT,
    `period` VARCHAR(255),
    `description` TEXT,
    `type` VARCHAR(255), -- Note: 'type' can be a reserved keyword. If issues persist, consider renaming (e.g., `artwork_type`).
    `location` VARCHAR(255),
    `donated` BOOLEAN,
    `file` VARCHAR(255),
    PRIMARY KEY (`artwork_id`),
    INDEX `fk_artwork_artist1_idx` (`artist_id`), -- Removed ASC and VISIBLE
    CONSTRAINT `fk_artwork_artist1`
        FOREIGN KEY (`artist_id`)
        REFERENCES `art_gallery`.`artist` (`artist_id`) -- This assumes a database 'art_gallery' and table 'artist' exist.
        ON DELETE NO ACTION
        ON UPDATE NO ACTION
) ENGINE = InnoDB;


-- Table `keyword`
CREATE TABLE IF NOT EXISTS `keyword` (
    `keyword_id` INT NOT NULL AUTO_INCREMENT,
    `keyword` VARCHAR(255) NOT NULL UNIQUE, -- Keywords should be unique
    PRIMARY KEY (`keyword_id`)
) ENGINE = InnoDB;

-- Table `keybridge` (Linking table for Artwork and Keyword)
CREATE TABLE IF NOT EXISTS `keybridge` (
    `artwork_id` INT NOT NULL,
    `keyword_id` INT NOT NULL,
    PRIMARY KEY (`artwork_id`, `keyword_id`),
    INDEX `fk_keybridge_artwork1_idx` (`artwork_id`), -- Removed ASC and VISIBLE
    INDEX `fk_keybridge_keyword1_idx` (`keyword_id`), -- Removed ASC and VISIBLE
    CONSTRAINT `fk_keybridge_artwork1`
        FOREIGN KEY (`artwork_id`)
        REFERENCES `art_gallery`.`artwork` (`artwork_id`)
        ON DELETE CASCADE -- If artwork is deleted, links should also be deleted
        ON UPDATE NO ACTION,
    CONSTRAINT `fk_keybridge_keyword1`
        FOREIGN KEY (`keyword_id`)
        REFERENCES `art_gallery`.`keyword` (`keyword_id`)
        ON DELETE CASCADE -- If keyword is deleted, links should also be deleted
        ON UPDATE NO ACTION
) ENGINE = InnoDB;


-- ============================================================================
-- SQL INSERT Statements for 'artist' table
-- ============================================================================
-- Make sure to run these inserts before the artwork inserts.
-- Assumed artist table structure:
-- CREATE TABLE artist (
--     artist_id INT AUTO_INCREMENT PRIMARY KEY,
--     fname VARCHAR(255),
--     mname VARCHAR(255),
--     lname VARCHAR(255) NOT NULL,
--     dob INT,
--     dod INT,
--     country VARCHAR(255),
--     local VARCHAR(1) -- Or BOOLEAN, adjust 'y'/'n' if needed
-- );
-- ----------------------------------------------------------------------------

INSERT INTO artist (artist_name, artist_middlename, artist_lastname, dob, dod, country, local) VALUES ('Vincent', NULL, 'van Gogh', 1853, 1890, 'France', 'n');
INSERT INTO artist (artist_name, artist_middlename, artist_lastname, dob, dod, country, local) VALUES ('Rembrandt', 'Harmenszoon', 'van Rijn', 1606, 1669, 'Netherlands', 'n');
INSERT INTO artist (artist_name, artist_middlename, artist_lastname, dob, dod, country, local) VALUES ('Leonardo', NULL, 'da Vinci', 1452, 1519, 'Italy', 'n');
INSERT INTO artist (artist_name, artist_middlename, artist_lastname, dob, dod, country, local) VALUES ('Venture', 'Lonzo', 'Coy', 1965, NULL, 'United States', 'y');
INSERT INTO artist (artist_name, artist_middlename, artist_lastname, dob, dod, country, local) VALUES ('Deborah', NULL, 'Gill', 1970, NULL, 'United States', 'y');
INSERT INTO artist (artist_name, artist_middlename, artist_lastname, dob, dod, country, local) VALUES ('Claude', NULL, 'Monet', 1840, 1926, 'France', 'n');
INSERT INTO artist (artist_name, artist_middlename, artist_lastname, dob, dod, country, local) VALUES ('Pablo', NULL, 'Picasso', 1904, 1973, 'Spain', 'n');
INSERT INTO artist (artist_name, artist_middlename, artist_lastname, dob, dod, country, local) VALUES ('Michelangelo', 'di Lodovico', 'Simoni', 1475, 1564, 'Italy', 'n');

-- ============================================================================
-- SQL INSERT Statements for 'artwork' table
-- ============================================================================
-- These inserts rely on the 'artist' table being populated first.
-- The artist_id is fetched using a subquery based on artist's fname and lname.
-- Assumed artwork table structure:
-- CREATE TABLE artwork (
--     artwork_id INT AUTO_INCREMENT PRIMARY KEY,
--     artist_id INT NOT NULL,
--     title VARCHAR(255) NOT NULL,
--     year INT,
--     period VARCHAR(255),
--     description TEXT,
--     type VARCHAR(255),
--     location VARCHAR(255),
--     donated BOOLEAN,
--     file VARCHAR(255),
--     FOREIGN KEY (artist_id) REFERENCES artist(artist_id)
-- );

DELETE FROM artist
WHERE artist_id BETWEEN 10 AND 16;

DELETE FROM artist
WHERE artist_name = 'Claude' 
  AND artist_lastname = 'Monet'
  AND artist_id = 5;
  
DELETE FROM artwork WHERE artist_id = 5;
DELETE FROM artist WHERE artist_id = 5;

DELETE FROM artist
WHERE artist_name = 'Claude'
  AND artist_lastname = 'Monet'
  AND country = 'France'
  AND dob = 1840
  AND dod = 1926
LIMIT 1;



SELECT artwork_id,title,artist_name,country,artist_lastname,artist_middlename
FROM `art_gallery`.`artwork`,`artist`;

SELECT artist_name,artist_name,country,artist_lastname,artist_middlename
FROM `art_gallery`.`artist`,`artwork`;


DELETE FROM artist
WHERE artist_id = 4;

DELETE FROM artwork WHERE artist_id = 3;
-- Depois:
DELETE FROM artist WHERE artist_id = ID_DO_ARTISTA;

-- ----------------------------------------------------------------------------

INSERT INTO artwork (artist_id, title, year, period, type, file) VALUES ((SELECT artist_id FROM artist WHERE artist_name = 'Vincent' AND artist_lastname = 'van Gogh'), 'Irises', 1889, 'Impressionism', 'Oil', 'irises.jpg');
INSERT INTO artwork (artist_id, title, year, period, type, file) VALUES ((SELECT artist_id FROM artist WHERE artist_name = 'Vincent' AND artist_lastname = 'van Gogh'), 'The Starry Night', 1889, 'Post-Impressionism', 'Oil', 'starrynight.jpg');
INSERT INTO artwork (artist_id, title, year, period, type, file) VALUES ((SELECT artist_id FROM artist WHERE artist_name = 'Vincent' AND artist_lastname = 'van Gogh'), 'Sunflowers', 1888, 'Post-impressionism', 'Oil', 'sunflowers.jpg');
INSERT INTO artwork (artist_id, title, year, period, type, file) VALUES ((SELECT artist_id FROM artist WHERE artist_name = 'Rembrandt' AND artist_lastname = 'van Rijn'), 'Night Watch', 1642, 'Baroque', 'Oil', 'nightwatch.jpg');
INSERT INTO artwork (artist_id, title, year, period, type, file) VALUES ((SELECT artist_id FROM artist WHERE artist_name = 'Rembrandt' AND artist_lastname = 'van Rijn'), 'Storm on the Sea of Galilee', 1633, 'Dutch Golden Age', 'Oil', 'stormgalilee.jpg');
INSERT INTO artwork (artist_id, title, year, period, type, file) VALUES ((SELECT artist_id FROM artist WHERE artist_name = 'Leonardo' AND artist_lastname = 'da Vinci'), 'Head of a Woman', 1508, 'High Renaissance', 'Oil', 'headwoman.jpg');
INSERT INTO artwork (artist_id, title, year, period, type, file) VALUES ((SELECT artist_id FROM artist WHERE artist_name = 'Leonardo' AND artist_lastname = 'da Vinci'), 'Last Supper', 1498, 'Renaissance', 'Tempra', 'lastsupper.jpg');
INSERT INTO artwork (artist_id, title, year, period, type, file) VALUES ((SELECT artist_id FROM artist WHERE artist_name = 'Leonardo' AND artist_lastname = 'da Vinci'), 'Mona Lisa', 1517, 'Renaissance', 'Oil', 'monalisa.jpg');
INSERT INTO artwork (artist_id, title, year, period, type, file) VALUES ((SELECT artist_id FROM artist WHERE artist_name = 'Venture' AND artist_lastname = 'Coy'), 'Hillside Stream', 2005, 'Modern', 'Oil', 'hillsidestream.jpg');
INSERT INTO artwork (artist_id, title, year, period, type, file) VALUES ((SELECT artist_id FROM artist WHERE artist_name = 'Venture' AND artist_lastname = 'Coy'), 'Old Barn', 1992, 'Modern', 'Oil', 'oldbarn.jpg');
INSERT INTO artwork (artist_id, title, year, period, type, file) VALUES ((SELECT artist_id FROM artist WHERE artist_name = 'Deborah' AND artist_lastname = 'Gill'), 'Beach Baby', 1999, 'Modern', 'Watercolor', 'beachbaby.jpg');
INSERT INTO artwork (artist_id, title, year, period, type, file) VALUES ((SELECT artist_id FROM artist WHERE artist_name = 'Claude' AND artist_lastname = 'Monet'), 'Women in the Garden', 1866, 'Impressionism', 'Oil', 'womengarden.jpg');
INSERT INTO artwork (artist_id, title, year, period, type, file) VALUES ((SELECT artist_id FROM artist WHERE artist_name = 'Pablo' AND artist_lastname = 'Picasso'), 'Old Guitarist', 1904, 'Modern', 'Oil', 'guitarist.jpg');
