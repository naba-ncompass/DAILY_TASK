const express = require('express');
const router = express.Router();
const bodyParser = require('body-parser');
const controller = require('../Employee/controller');
const validation = require('../Employee/validation');
const authorization = require('../Utilities/authorization');

router.use(bodyParser.json());
router.use(express.static('public'));

// get all employees
router.get('/noderead',    controller.readEmployee);

// insert multiple employee 
router.post('/nodeinsert', validation.validateArrayofObjects ,controller.insertEmployee);

// get employee by ID
router.get('/nodereadid',    authorization, validation.adduservalidation, controller.readEmployeeid);

// delete employee
router.delete('/nodedelete', authorization, validation.adduservalidation, controller.deleteEmployee);

// update employee
router.post('/nodeupdate',   authorization, validation.adduservalidation, controller.updateEmployee);

// signup employee 
router.post('/nodesignup', validation.adduservalidation, controller.signupEmployee);

// signin employee
router.post('/nodesignin', validation.addsigninvalidation, controller.signinEmployee);

// truncate employee
router.delete('/nodetruncate', authorization, controller.truncateEmployee);




module.exports = router;

