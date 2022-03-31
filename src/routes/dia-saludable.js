const express = require('express');
const router = express.Router();
const pool = require('../db');
const { isLoggedIn, isNotLoggedIn } = require('../lib/auth');

router.get('/dia-saludable', isNotLoggedIn, async (req, res) => {
    const blog = await pool.query('SELECT * FROM blog');
    res.render('dia-saludable/', { blog });
});

router.get('/dia-saludable/articulos/:id', isNotLoggedIn, async (req, res) => {
    const {id} = req.params;
    const blogdos = await pool.query('SELECT * FROM blogdos WHERE id = ?', [id]);
    res.render('dia-saludable/articulo', { blog: blogdos[0] });
});

router.get('/dia-saludable/add', isLoggedIn, (req, res) => {
    res.render('dia-saludable/add');
});

router.post('/dia-saludable/add', isLoggedIn, async (req, res) => {
    const {
        tema,
        urlimg,
        enlace,
        piefoto,
        miniatura,
        titulo,
        subtitulo,
        subtitleone,
        paraguno,
        subtitledos,
        paragdos,
        subtitletres,
        paragtres,
        subtitlecuatro,
        paragcuatro,
        subtitlecinco,
        paragcinco,
        subtitleseis,
        paragseis,
        autor,
        city
    } = req.body;
    const newBlog = {
        tema,
        urlimg,
        enlace,
        piefoto,
        miniatura,
        titulo,
        subtitulo,
        subtitleone,
        paraguno,
        subtitledos,
        paragdos,
        subtitletres,
        paragtres,
        subtitlecuatro,
        paragcuatro,
        subtitlecinco,
        paragcinco,
        subtitleseis,
        paragseis,
        autor,
        city
    };
    await pool.query('INSERT INTO blogdos SET ?', [newBlog]);
    //req.flash('success', 'Artículo enviado satisfactoriamente');
    res.redirect('/dia-saludable');
});

module.exports = router;