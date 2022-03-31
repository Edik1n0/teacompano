const bcrypt = require('bcryptjs');
const helpers = {};

helpers.encryptPassword = async (perpass) => {
    const salt = await bcrypt.genSalt(10);
    const hash = await bcrypt.hash(perpass, salt);
    return hash;
};

helpers.matchPassword = async (perpass, savedPassword) => {
    try {
        return await bcrypt.compare(perpass, savedPassword);
    } catch(e) {
        console.log(e);
    }
};

module.exports = helpers;