const express = require('express');
const morgan = require('morgan');
const exphbs = require('express-handlebars');
const path = require('path');

// Init
const app = express();

// Sett
app.set('port', process.env.PORT || 8000);
app.set('views', path.join(__dirname, 'views'));
app.engine('.hbs', exphbs({
    defaultLayout: 'main',
    layoutsDir: path.join(app.get('views'), 'layouts'),
    partialsDir: path.join(app.get('views'), 'partials'),
    extname: '.hbs',
    helpers: require('./lib/handlebars')
}));
app.set('view engine', '.hbs');

// Middle
app.use(morgan('dev'));
app.use(express.urlencoded({extended: false}));
app.use(express.json());

// Global
app.use((req, res, next) => {
    next();
});

// Routes
app.use(require('./routes'));
app.use(require('./routes/auth'));
app.use(require('./routes/users'));

// Public
app.use(express.static(path.join(__dirname, 'public')));

// Start
app.listen(app.get('port'), () => {
    console.log('Servidor en el puerto', app.get('port'));
});