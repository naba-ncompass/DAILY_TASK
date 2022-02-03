const express = require('express');
const bodyParser = require('body-parser');
const controller = require('../Pincode/controller');
const validation = require('../Pincode/validation');
const errorHandle = require('../Utilities/error_handler')
const router = express.Router();

router.use(bodyParser.json());
router.use(express.static('public'));

// get all 
router.get('/pincode', validation.pincodevalidation, controller.pincode);

// router.get('/pincode', async (req,res)=> {
//     const address = req.query




// });




module.exports = router;