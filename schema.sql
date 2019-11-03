CREATE TABLE quote (id integer primary key, content text not null, category text not null, authorid integer REFERENCES author(id));
CREATE TABLE author (id integer primary key, name text not null);
