const express = require('express');
const routerdevice = express.Router();
const bodyParser = require('body-parser');
const controller = require('../Device/controller');
const validate = require('../Device/validation');

routerdevice.use(bodyParser.json());
routerdevice.use(express.static('public'));

// read device
routerdevice.get('/readdevice', validate.devicevalidation, controller.readDevice);

// max device
routerdevice.get('/maxdevice', validate.devicevalidation, controller.maxDevice);

// sum device 
routerdevice.get('/sumdevice', validate.devicevalidation, controller.sumDevice);

// duplicate device
routerdevice.get('/duplicatedevice', validate.devicevalidation, controller.duplicateDevice);


module.exports = routerdevice;

