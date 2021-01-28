const nodemailer = require('nodemailer');
// email sender function
exports.sendEmail = function (req, res) {
    // Definimos el transporter
    const transporter = nodemailer.createTransport({
        service: 'Gmail',
        auth: {
            user: 'kinotrance@gmail.com',
            pass: 'Edi1017194099'
        }
    });
    // Definimos el email
    const mailUser = {
        from: 'kinotrance@gmail.com',
        to: 'teacompano300@gmail.com',
        subject: 'Nuevo servicio solicitado',
        text: 'Se ha registrado un nuevo usuario'
    };
    // Enviamos el email
    transporter.sendMail(mailUser, function (error, info) {
        if (error) {
            console.log(error);
            //res.send(500, error.message);
            res.redirect('/');
        } else {
            console.log("Email sent");
            //res.status(200).jsonp(req.body);
            req.flash('success', 'Datos registrado correctamente');
            res.redirect('/');
        }
    });
};

exports.sendNurseEmail = function (req, res) {
    // Definimos el transporter
    const transporter = nodemailer.createTransport({
        service: 'Gmail',
        auth: {
            user: 'kinotrance@gmail.com',
            pass: 'Edi1017194099'
        }
    });
    // Definimos el email
    const mailUser = {
        from: 'kinotrance@gmail.com',
        to: 'teacompano300@gmail.com',
        subject: 'Nuevo servicio solicitado',
        text: 'Se ha registrado una nueva Historia Clínica'
    };
    // Enviamos el email
    transporter.sendMail(mailUser, function (error, info) {
        if (error) {
            console.log(error);
            //res.send(500, error.message);
            //res.redirect('/personal/');
        } else {
            console.log("Email sent");
            //res.status(200).jsonp(req.body);
            //req.flash('success', 'Datos registrados correctamente');
            res.render('enfermeras/agregar');
        }
    });
};