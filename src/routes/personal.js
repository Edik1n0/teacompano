const express = require('express');
const router = express.Router();
const pool = require('../db');
const { isLoggedIn, isNotLoggedIn } = require('../lib/auth');

router.get('/personal/perfil', isLoggedIn, async (req, res) => {
    const personal = await pool.query('SELECT * FROM personal');
    res.render('personal/perfil', { personal });
});

router.get('/personal/agregar', isLoggedIn, (req, res) => {
    res.render('personal/agregar');
});

router.post('/agregar-paciente', isLoggedIn, async (req, res) => {
    const { pacientenombre,
        pacienteedad,
        pacientetel,
        pacientecorreo,
        pacienteingreso,
        pacientesalida,
        pacienteeps,
        pacienteparentezco,
        pacientediagnostico,
        pacienteservicio } = req.body;

    const newPaciente = {
        pacientenombre,
        pacienteedad,
        pacientetel,
        pacientecorreo,
        pacienteingreso,
        pacientesalida,
        pacienteeps,
        pacienteparentezco,
        pacientediagnostico,
        pacienteservicio
    };
    await pool.query('INSERT INTO pacientes SET ?', [newPaciente]);
    res.send('recibido');
});

router.get('/personal/lista', isLoggedIn, async (req, res) => {
    const pacientes = await pool.query('SELECT * FROM pacientes');
    res.render('personal/listado', { pacientes })
});

router.get('/personal/solicitud/:id', isLoggedIn, async (req, res) => {
    const { id } = req.params;
    const registros = await pool.query('SELECT * FROM registros WHERE id = ?', [id]);
    res.render('personal/solicitud', { registros: registros[0] });
});

router.get('/personal/solicitudes', isLoggedIn, async (req, res) => {
    const registros = await pool.query('SELECT * FROM registros');
    res.render('personal/solicitudes', { registros })
});

router.get('/personal/individual/:id', isLoggedIn, async (req, res) => {
    const { id } = req.params;
    const pacientes = await pool.query('SELECT * FROM pacientes WHERE id = ?', [id]);
    res.render('personal/individual', { pacientes: pacientes[0] });
});

module.exports = router;