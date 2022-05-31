PRAGMA FOREIGN_KEYS = ON;

DROP TABLE IF EXISTS countries;
DROP TABLE IF EXISTS cities;

CREATE TABLE countries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR,
    continent VARCHAR
);

CREATE TABLE cities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR,
    country INT,
    visited BOOLEAN,
        FOREIGN KEY (country)
            REFERENCES countries(id) ON DELETE CASCADE

);