const express = require('express');
const passport = require('passport');
const router = express.Router();
const { isLoggedIn, isNotLoggedIn } = require('../lib/auth');

const pool = require('../db');

router.get('/personal', isNotLoggedIn, (req, res) => {
    res.render('personal/');
});

router.post('/personal', (req, res, next) => {
    passport.authenticate('local.signin', {
        successRedirect: '/personal/perfil',
        failureRedirect: '/personal/',
        failureFlash: true
    })(req, res, next);
});

router.get('/salir', isLoggedIn, (req, res) => {
    req.logOut();
    req.flash('success', 'Ha cerrado sesión correctamente');
    res.redirect('/');
});

module.exports = router;