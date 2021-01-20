const express = require('express');
const router = express.Router();

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

module.exports = router;