SELECT name FROM people JOIN stars ON people.id = stars.person_id WHERE stars.movie_id = (SELECT id FROM movies WHERE title = 'Toy Story');
