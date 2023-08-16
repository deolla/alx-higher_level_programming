-- lists all genres in the database hbtn_0d_tvshows_rate by their rating.
SELECT CONCAT(tv_genres.name, ' - ', SUM(tv_shows.rating)) AS genre_rating
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
GROUP BY tv_genres.name
ORDER BY SUM(tv_shows.rating) DESC;
