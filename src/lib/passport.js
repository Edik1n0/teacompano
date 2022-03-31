const passport = require('passport');
const pool = require('../db');
const helpers = require('./helpers');

const Strategy = require('passport-local').Strategy;

passport.use('local.signin', new Strategy({
    usernameField: 'peruser',
    passwordField: 'perpass',
    passReqToCallback: true
}, async (req, peruser, perpass, done) => {
    const rows = await pool.query('SELECT * FROM personal WHERE peruser = ?', [peruser]);
    if (rows.length > 0) {
        const user = rows[0];
        const validPassword = await helpers.matchPassword(perpass, user.perpass);
        if (validPassword) {
            done(null, user, req.flash('success', 'Bienvenid@' + user.peruser));
        } else {
            done(null, false, req.flash('message', 'La contraseña es incorrecta'));
        }
    } else {
        return done(null, false, req.flash('message', 'El nombre de usuario no existe'));
    }
}));

passport.use('local.signup', new Strategy({
    usernameField: 'peruser',
    passwordField: 'perpass',
    passReqToCallback: true
}, async (req, peruser, perpass, done) => {
    const { pernombre, percargo, perfoto, perdate, perid } = req.body;
    const newPer = {
        peruser,
        perpass,
        pernombre,
        percargo,
        perfoto,
        perdate,
        perid
    };
    newPer.perpass = await helpers.encryptPassword(perpass);
    const result = await pool.query('INSERT INTO personal SET ?', [newPer]);
    newPer.id = result.insertId;
    return done(null, newPer);
}));

passport.serializeUser((user, done) => {
    done(null, user.id); // Guardando el ID del usuario
});

passport.deserializeUser(async (id, done) => {
    const rows = await pool.query('SELECT * FROM personal WHERE id = ?', [id]);
    done(null, rows[0]);
});
