-- lists all genres of the show Dexter.
SELECT name FROM tv_genre
JOIN tv_shows_genre ON tv_genre.id = genre_id
JOIN tv_shows ON tv_show.id = show_id
WHERE title = 'Dexter'
ORDER BY `name`
