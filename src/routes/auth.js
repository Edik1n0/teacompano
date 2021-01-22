const express = require('express');
const router = express.Router();

const passport = require('passport');

router.get('/control/signup', (req, res) => {
    res.render('auth/signup');
});

router.post('/control/signup', passport.authenticate('local.signup', {
    successRedirect: '/control/perfil',
    failureRedirect: '/control/signup',
    failureFlash: true
}));

router.get('/control/perfil', (req, res) => {
    res.send('Vista del perfil');
});

module.exports = router;