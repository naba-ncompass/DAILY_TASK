const joi = require('joi')

const input_device = joi.object({
  time1: joi.string().min(1).max(8).pattern(new RegExp("^[0-1][0-9]:[0-5][0-9]:[0-5][0-9]$|^[2][0-3]:[0-5][0-9]:[0-5][0-9]$")),
  time2: joi.string().min(1).max(8).pattern(new RegExp("^[0-1][0-9]:[0-5][0-9]:[0-5][0-9]$|^[2][0-3]:[0-5][0-9]:[0-5][0-9]$")),
  device: joi.string().min(2).max(2),
});

const devicevalidation = async (req, res, next) => {
  const value = await input_device.validate(req.body);
    if (value.error) {
      res.json({
        success: 0,
        message: value.error.details[0].message
      })
    } else {
      next();
    }
  
};


module.exports = { devicevalidation};
