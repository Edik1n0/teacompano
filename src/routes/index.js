const express = require('express');
const router = express.Router();
const pool = require('../db');

router.get('/', (req, res) => {
    res.render('layouts/home');
});

router.get('/nosotros', (req, res) => {
    res.render('layouts/nosotros');
});

router.get('/contacto', (req, res) => {
    res.render('layouts/contacto');
});

router.get('/politica-privacidad', (req, res) => {
    res.render('layouts/politica-privacidad');
});

router.get('/politica-cookies', (req, res) => {
    res.render('layouts/politica-cookies');
});

router.get('/servicios', (req, res) => {
    res.render('layouts/servicios');
});

router.get('/formulario-solicitud', (req, res) => {
    res.render('layouts/formulario-solicitud');
});

router.get('/formulario-socios', (req, res) => {
    res.render('layouts/formulario-socios');
});

router.get('/msgok', (req, res) => {
    req.flash('success', 'Sus datos se han enviado correctamente');
    res.render('layouts/home');
});

module.exports = router;