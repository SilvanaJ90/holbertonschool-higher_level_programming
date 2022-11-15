-- script that lists all Comedy shows in the database hbtn_0d_tvshows.
SELECT A.title
FROM tv_shows A
LEFT JOIN tv_show_genres B
ON A.id = B._show_id
LEFT JOIN tv_genres C
ON B.genre = C.id
WHERE B.name = 'Comedy'
ORDER BY A.title ASC;