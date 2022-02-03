const Ajv = require("ajv");
const addFormats = require("ajv-formats");
const { errorResponse } = require("../Utilities/custom-response");
const ajv = new Ajv({ allErrors: true });
addFormats(ajv);

//parses list of errors
const parseErrors = (errors) => {
  let parsedErr = [];
  errors.forEach((error) => {
    parsedErr.push(error.instancePath.slice(1) + " " + error.message);
  });

  let err = new Error(parsedErr)
  err.name = 'ValidationError'
  return err
};

//verifies validation and parses and customizes response
const validate = (ajvValidate, body, res, next) => {
  const valid = ajvValidate(body);
  if (!valid) {
    const errors = ajvValidate.errors;
    next(parseErrors(errors))
  } else {
    return next();
  }
};


const validateDevice = (req, res, next) => {
    const deviceSchema = {
      type: "object",
      properties: {
        device: { enum: ["D1", "D2", "D3"] },
        from: { type: "string" , pattern: '^(?:(?:([01]?\\d|2[0-3]):)?([0-5]?\\d):)?([0-5]?\\d)$'},
        to: { type: "string" , pattern: '^(?:(?:([01]?\\d|2[0-3]):)?([0-5]?\\d):)?([0-5]?\\d)$'},
      },
      required: ["device", "from", "to"],
    };
  
    return validate(ajv.compile(deviceSchema), req.body, res, next);
  };


  module.exports = {
    validateDevice
  }