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

-- CREATE TABLE pacientes (
--     id INT(11) NOT NULL,
--     pacientenombre VARCHAR(60) NOT NULL,
--     pacienteedad VARCHAR(10) NOT NULL,
--     pacienteeps VARCHAR(60) NOT NULL,
--     pacientediagnostico VARCHAR(60) NOT NULL,
--     pacienteservicio VARCHAR(60) NOT NULL,
--     pacientetel VARCHAR(60) NOT NULL,
--     pacienteingreso VARCHAR(60) NOT NULL,
--     pacientesalida VARCHAR(60) NOT NULL,
--     pacienteresponsable VARCHAR(60) NOT NULL,
--     pacienteparentezco VARCHAR(60) NOT NULL,
--     nurse_id INT(11),
--     created_at timestamp NOT NULL DEFAULT current_timestamp,
--     ADD CONSTRAINT fk_pacient FOREIGN KEY (nurse_id) REFERENCES enfermeras(id)
-- );

-- CREATE TABLE enfermeras(
--     id INT(11) NOT NULL,
--     enfermera VARCHAR(16) NOT NULL,
--     pass VARCHAR(60) NOT NULL,
--     nombre VARCHAR(100) NOT NULL
-- );

-- ALTER TABLE pacientes
--     ADD evolucion VARCHAR(500) NOT NULL,
--     ADD pacientepeso VARCHAR(20) NOT NULL,
--     ADD pacientedieta VARCHAR(60) NOT NULL,
--     ADD pacienteoxigeno VARCHAR(60) NOT NULL,
--     ADD tratamiento TEXT NOT NULL,
--     ADD plan TEXT NOT NULL;

-- ALTER TABLE pacientes
--     MODIFY evolucion VARCHAR(500) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT = 2;