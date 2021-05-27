-- Creating user with password and granting all privileges
sudo mysql –u root –p
IF NOT EXISTS CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY user_0d_1_pwd;
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
