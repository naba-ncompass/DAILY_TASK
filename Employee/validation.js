const joi = require('joi')

const inputUser = joi.object({
  id: joi.number().min(1).max(100),
  first_name: joi.string().min(1).max(10),
  last_name: joi.string().min(1).max(10),
  email: joi.string().email().lowercase(),
  gender: joi.string().valid("m", "f", "o"),
  phone: joi.number().min(1000000000).max(9999999999),
  password: joi.string().pattern(new RegExp("^[a-zA-Z0-9]{3,30}$")).min(4).max(15),
}).unknown(true);

const signinUser = joi.object({
  email: joi.string().email().lowercase(),
  password: joi.string().pattern(new RegExp("^[a-zA-Z0-9]{3,30}$")).min(4).max(15),
});

const adduservalidation = async (req, res, next) => {
  const value = await inputUser.validate(req.body);
  if (value.error) {
    res.json({
      success: 0,
      message: value.error.details[0].message
    })
  } else {
    next();
  }
};

const addsigninvalidation = async (req, res, next) => {
  const value = await signinUser.validate(req.body);
  if (value.error) {
    res.json({
      success: 0,
      message: value.error.details[0].message
    })
  } else {
    next();
  }
};


const arrayOfSchema = joi.array().items(inputUser)


const validateArrayofObjects = async (req, res, next) => {
  const value = await arrayOfSchema.validate(req.body,{abortEarly: false});
  if (value.error) {
    // for (let i = 0; i < value.error.details.length ; i++) 
    //   {
      console.log("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
      console.log(value.error._original.value)
        res.json({
          message: value.error.message
          //message: value.error._original
      })
      // res.json({
      //   message: value.error._original
      // })
    // }
  } else {
    next();
  }
};





module.exports = {
  adduservalidation,
  addsigninvalidation,
  validateArrayofObjects
}