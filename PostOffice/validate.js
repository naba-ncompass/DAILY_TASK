const Ajv = require("ajv");
const addFormats = require("ajv-formats");
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

const pinSchema = {
  type: "object",
  properties: {
    pin: { type: "string", pattern: "^[0-9]{6}$", minLength: 6 , maxLength: 6 },
  },
  required: ["pin"],
};

const validatePin = (req, res, next) => {
  return validate(ajv.compile(pinSchema), req.query, res, next);
};


module.exports = {
    validatePin
}