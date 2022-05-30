PRAGMA FOREIGN_KEYS = ON;

DROP TABLE IF EXISTS countries;
DROP TABLE IF EXISTS cities;

CREATE TABLE countries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR
);

CREATE TABLE cities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR,
    country_id INT,
    visited BOOLEAN,
        FOREIGN KEY (country_id)
            REFERENCES countries(id)

);

