--  script to lists all genres of the show Dexter.
SELECT A.name
FROM tv_genres A
WHERE id = (SELECT id FROM tv_shows WHERE title='Dexter')
ORDER BY A.name ASC;