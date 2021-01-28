const express = require('express');
const router = express.Router();
const EmailCtrl = require('./nodemailer');

const pool = require('../db');

router.get('/add', (req, res) => {
    res.render('usuarios/add');
});

router.post('/add', EmailCtrl.sendEmail, async (req, res) => {
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

module.exports = router;