-- CREATE TABLE nurse(
--     id INT(11) NOT NULL,
--     username VARCHAR(16) NOT NULL,
--     password VARCHAR(60) NOT NULL,
--     fullname VARCHAR(100) NOT NULL
-- );

-- ALTER TABLE nurse
--     ADD PRIMARY KEY (id);

-- ALTER TABLE nurse
--     MODIFY id INT(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT = 2;

-- CREATE TABLE usuarios (
--     id INT(11) NOT NULL,
--     username VARCHAR(60) NOT NULL,
--     phone VARCHAR(60) NOT NULL,
--     email VARCHAR(60) NOT NULL,
--     description TEXT,
--     user_id INT(11),
--     created_at timestamp NOT NULL DEFAULT current_timestamp,
--     CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES users(id)
-- );

-- ALTER TABLE usuarios
--     ADD PRIMARY KEY (id);

-- ALTER TABLE usuarios
--     MODIFY id INT(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT = 2;

-- CREATE TABLE suser(
--      id INT(11) NOT NULL,
--      fullname VARCHAR(60) NOT NULL,
--      username VARCHAR(16) NOT NULL,
--      email VARCHAR(60) NOT NULL,
--      phone VARCHAR(50) NOT NULL,
--      password VARCHAR(60) NOT NULL,
-- );