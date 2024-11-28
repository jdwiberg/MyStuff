

CREATE TABLE students (
    id INTEGER,
    student_name TEXT,
    PRIMARY KEY(id)
);

CREATE TABLE houses (
    id INTEGER,
    house TEXT,
    head TEXT,
    PRIMARY KEY(id)
);

CREATE TABLE relationships (
    id INTEGER,
    house_id INTEGER,
    student_id INTEGER,
    PRIMARY KEY(id),
    FOREIGN KEY(house_id) REFERENCES houses(id),
    FOREIGN KEY(student_id) REFERENCES students(id)
);
