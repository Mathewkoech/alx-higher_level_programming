-- lists all shows contained in the database hbtn_0d_tvshows.
-- Each record should display: tv_shows.title - tv_show_genres.genre_id
-- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
-- If a show doesn’t have a genre, display NULL
SELECT title, genre_id FROM tv_show_genres
RIGHT JOIN tv_shows ON id = show_id
ORDER BY title, genre_id;
