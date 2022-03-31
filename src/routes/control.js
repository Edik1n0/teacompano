const express = require('express');
const router = express.Router();
const passport = require('passport');
const { isLoggedIn, isNotLoggedIn } = require('../lib/auth');

const pool = require('../db');

router.get('/control/', isNotLoggedIn, (req, res) => {
    res.render('control/');
});

router.get('/control/registro-personal', isLoggedIn, (req, res) => {
    res.render('control/registro-personal');
});

router.get('/control/perfil', isLoggedIn, (req, res) => {
    res.render('control/perfil');
});

router.post('/control/registro-personal', passport.authenticate('local.signup', {
    successRedirect: '/control/perfil',
    failureRedirect: '/control/',
    failureFlash: true
}));


module.exports = router;