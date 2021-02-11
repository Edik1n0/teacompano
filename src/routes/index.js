const express = require('express');
const passport = require('passport');
const router = express.Router();
const EmailCtrl = require('./nodemailer');
const pool = require('../db');
const { isLoggedIn, isNotLoggedIn } = require('../lib/auth');


router.get('/', (req, res) => {
    res.render('layouts/home');
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
    res.render('control/users', {usuarios});
});

router.get('/control/historias', async (req, res) => {
    const pacientes = await pool.query('SELECT * FROM pacientes');
    res.render('control/historias', { pacientes });
});

router.get('/control/pacientes/eliminar/:id', isLoggedIn, async (req, res) => {
    const { id } = req.params;
    await pool.query('DELETE FROM pacientes WHERE id = ?', [id]);
    req.flash('success', 'Usuario eliminado satisfactoriamente')
    res.redirect('/control/historias');
});

router.post('/usuarios/add', async (req, res) => {
    const {username, email, phone, description} = req.body;
    const newComUser = {
        username,
        email,
        phone,
        description
    };
    await pool.query('INSERT INTO usuarios SET ?', [newComUser]);
    req.flash('success', 'Mensaje enviado satisfactoriamente');
    res.redirect('/');
});

router.get('/control/users/delete/:id', isLoggedIn, async (req, res) => {
    const { id } = req.params;
    await pool.query('DELETE FROM usuarios WHERE id = ?', [id]);
    req.flash('success', 'Usuario eliminado satisfactoriamente')
    res.redirect('/control/users');
});


module.exports = router;