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
        subject: 'Nueva historia clínica',
        text: 'Se ha actualizado una historia clínica'
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
            //res.redirect('/personal/historias/agregar');
        }
    });
};