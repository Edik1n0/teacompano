const express = require('express');
const router = express.Router();

router.get('/', (req, res) => {
    res.render('layouts/home');
});

router.get('/servicios', (req, res) => {
    res.render('layouts/servicios');
});

module.exports = router;