-- Write a script that creates the MySQL server user user_0d_1. 
CREATE USER 'user_0d_1'@'localhost' IDENTIFIED WIDTH authentication_plugin BY 'user_0d_1_pwd';
GRANT PRIVILEGE ON database.table TO 'user_0d_1'@'localhost';
