-- Write a script that lists all cities contained in the database hbtn_0d_usa.
 Cada registro debe mostrar: ciudades.id - ciudades.nombre - estados.nombre
    Los resultados deben estar ordenados de forma ascendente por cities.id
    Sólo se puede utilizar una sentencia SELECT
    El nombre de la base de datos se pasará como argumento del comando mysql

SELECT cities.id, cities.name, states.name FROM cities INNER JOIN states ORDER BY cities.id ASC;