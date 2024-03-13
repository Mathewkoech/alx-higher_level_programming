-- lists all shows without comedy show in the database hbtn_0d_tv shows
SELECT title FROM tv_shows
WHERE NOT IN (
      SELECT title FROM tv_shows
      JOIN tv_show_genres ON tv_shows.id = show_id
      JOIN tv_genres ON genre_id = tv_genres.id WHERE `name` = "Comedy")
ORDER BY title;
