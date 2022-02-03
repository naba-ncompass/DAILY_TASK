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

const insertSchema = {
  type: "object",
  properties: {
    id: { type: "integer" },
    username: { type: "string" },
    email: { type: "string", format: "email" },
    password: { type: "string", minLength: 8 },
    phone_no: { type: "string", pattern: "^(\\+\\d{1,3}[- ]?)?\\d{10}$" },
  },
  required: ["id", "username", "email", "password"],
};

const validateInsert = (req, res, next) => {
  return validate(ajv.compile(insertSchema), req.body, res, next);
};

const validateMultipleInsert = (req, res, next) => {
  const multipleInsertSchema = {
    type: "array",
    items: insertSchema,
  };

  return validate(ajv.compile(multipleInsertSchema), req.body, res, next);
};

const validateUpdate = (req, res, next) => {
  const updateSchema = {
    type: "object",
    properties: {
      column: { enum: ["username", "email", "phone_no"] },
      new_value: { type: "string" },
    },
    required: ["column", "new_value"],
  };

  return validate(ajv.compile(updateSchema), req.body, res, next);
};

const validateDelete = (req, res, next) => {
  const deleteSchema = {
    type: "object",
    properties: {
      id: { type: "integer" },
    },
    required: ["id"],
  };

  return validate(ajv.compile(deleteSchema), req.body, res, next);
};

const validateLogin = (req, res, next) => {
  const loginSchema = {
    type: "object",
    properties: {
      username: { type: "string" },
      password: { type: "string", minLength: 8 },
    },
    required: ["username", "password"],
  };

  return validate(ajv.compile(loginSchema), req.body, res, next);
};

module.exports = {
  validateInsert,
  validateUpdate,
  validateDelete,
  validateLogin,
  validateMultipleInsert,
};
