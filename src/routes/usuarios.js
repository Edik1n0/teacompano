const express = require('express');
const router = express.Router();
const pool = require('../db');

router.post('/formulario-solicitud', async (req, res) => {
    const {nombreuser, teluser, emailuser, addressuser, serviceuser, descuser } = req.body;
    const newReg = {
        nombreuser,
        teluser,
        emailuser,
        addressuser,
        serviceuser,
        descuser
    };
    await pool.query ('INSERT INTO registros SET ?', [newReg]);
    req.flash('success', 'Sus datos se han enviado correctamente');
    res.redirect('/');
});

router.post('/formulario-socios', async (req, res) => {
    const {titular, cargo, contacto, ecorpo, addcorpo, alianza, descorpo} = req.body;
    const newAli = {titular, cargo, contacto, ecorpo, addcorpo, alianza, descorpo};
    await pool.query ('INSERT INTO aliados SET ?', [newAli]);
    req.flash('success', 'Sus datos se han enviado correctamente');
    res.redirect('/');
});

module.exports = router;