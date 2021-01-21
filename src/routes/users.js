const express = require('express');
const router = express.Router();

const pool = require('../db');

router.get('/add', (req, res) => {
    res.render('usuarios/add');
});

router.post('/add', async (req, res) => {
    const {username, email, phone, description} = req.body;
    const newComUser = {
        username,
        email,
        phone,
        description
    };
    await pool.query('INSERT INTO usuarios SET ?', [newComUser]);
    res.render('/');
});

module.exports = router;