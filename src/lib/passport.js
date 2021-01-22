const passport = require('passport');
const Strategy = require('passport-local').Strategy;

const pool = require('../db');
const helpers = require('./helpers');

passport.use('local.signin', new Strategy({
    usernameField: 'username',
    passwordField: 'password',
    passReqToCallback: true
}, async (req, username, password, done) => {
    console.log(req.body);
    const rows = await pool.query('SELECT * FROM nurse WHERE username = ?', [username]);
    if (rows.length > 0) {
        const user = rows[0];
        const validPassword = await helpers.matchPassword(password, user.password);
        if (validPassword) {
            done(null, user, req.flash('success', 'Bienvenid@' + user.username));
        } else {
            done(null, false, req.flash('message', 'La contraseña es incorrecta'));
        }
    } else {
        return done(null, false, req.flash('message', 'El nombre de usuario no existe'));
    }
}));

passport.use('local.signup', new Strategy({
   usernameField: 'username',
   passwordField : 'password',
   passReqToCallback: true
}, async (req, username, password, done) => {
    const { fullname } = req.body;
    const newUser = {
        username,
        password,
        fullname
    };
    newUser.password = await helpers.encryptPassword(password);
    const result = await pool.query('INSERT INTO nurse SET ?', [newUser]);
    newUser.id = result.insertId;
    return done(null, newUser);
}));

passport.serializeUser((user, done) => {
    done(null, user.id);
});

passport.deserializeUser( async(id, done) => {
    const rows = await pool.query('SELECT * FROM nurse WHERE id = ?', [id]);
    done(null, rows[0]);
});