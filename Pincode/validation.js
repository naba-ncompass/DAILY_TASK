const joi = require('joi')
const responsehandler = require("../Utilities/response_handler");

const schema = joi.object({
    pincode: joi.string().pattern(new RegExp("^[0-9]{6}$")).required()
});

const pincodevalidation = (req, res, next) => {
    const value = schema.validate(req.query);
    if (value.error) {
      res.json({
        success: 0,
        message: value.error.details[0].message
      })
    //    return res.status(400).json(responsehandler.makeErrorResponse(" wrong pin code data not found "));

    } else {
      next();
    }
};
  
module.exports = {
    pincodevalidation
  };