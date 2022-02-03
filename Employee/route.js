const express = require('express');
const router = express.Router();
const bodyParser = require('body-parser');
const controller = require('../Employee/controller');
const validation = require('../Employee/validation');
const authorization = require('../Utilities/authorization');

router.use(bodyParser.json());
router.use(express.static('public'));

// get all employees
router.get('/read',    controller.readEmployee);

// insert multiple employee 
router.post('/insert', validation.validateArrayofObjects ,controller.insertEmployee);

// get employee by ID
router.get('/readid',    authorization, validation.adduservalidation, controller.readEmployeeid);

// delete employee
router.delete('/delete', authorization, validation.adduservalidation, controller.deleteEmployee);

// update employee
router.post('/update',   authorization, validation.adduservalidation, controller.updateEmployee);

// signup employee 
router.post('/signup', validation.adduservalidation, controller.signupEmployee);

// signin employee
router.post('/signin', validation.addsigninvalidation, controller.signinEmployee);

// truncate employee
router.delete('/truncate', authorization, controller.truncateEmployee);




module.exports = router;

