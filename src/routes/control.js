const express = require('express');
const router = express.Router();
const webpush = require('web-push');
require('dotenv').config();

const pool = require('../db');

module.exports = router;