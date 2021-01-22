const express = require('express');
const passport = require('passport');
const router = express.Router();

const pool = require('../db');
const { isLoggedIn, isNotLoggedIn } = require('../lib/auth');

router.get('/', (req, res) => {
    res.render('layouts/home');
});

router.get('/servicios', (req, res) => {
    res.render('layouts/servicios');
});

router.get('/servicios/acompanamiento-citas-medicas', (req, res) => {
    res.render('servicios/acompanamiento-citas-medicas');
});

router.get('/servicios/asesoria-juridica-salud', (req, res) => {
    res.render('servicios/asesoria-juridica-salud');
});

router.get('/servicios/consulta-medica', (req, res) => {
    res.render('servicios/consulta-medica');
});

router.get('/servicios/enfermeria-domicilio', (req, res) => {
    res.render('servicios/enfermeria-domicilio');
});

router.get('/servicios/enfermeria-intrahospitalario', (req, res) => {
    res.render('servicios/enfermeria-intrahospitalario');
});

router.get('/control', isNotLoggedIn, (req, res) => {
    res.render('control/');
});

router.post('/control/', isNotLoggedIn, (req, res, next) => {
    passport.authenticate('local.signin', {
        successRedirect: '/control/perfil',
        failureRedirect: '/control/',
        failureFlash: true
    })(req, res, next);
});

router.get('/control/users', isLoggedIn, async(req, res) => {
    const usuarios = await pool.query('SELECT * FROM usuarios');
    console.log(usuarios);
    res.render('control/users', {usuarios});
});

router.get('/control/users/delete/:id', isLoggedIn, async (req, res) => {
    const { id } = req.params;
    await pool.query('DELETE FROM usuarios WHERE id = ?', [id]);
    req.flash('success', 'Usuario eliminado satisfactoriamente')
    res.redirect('/control/users');
});

module.exports = router;