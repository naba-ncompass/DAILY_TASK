const Joi = require("joi");
const { errorObjectCreator } = require("../Utilities/errorHandler");

const schema = Joi.object({
    pin: Joi.string().pattern(new RegExp("^[0-9]{6}$")).required(),
});

const validateData = (data) => {
    return schema.validate(data);
};

const validatorMiddleware = (req, res, next) => {
    var errorCode = 400;
    var validationResult = validateData(req.query);
    if (validationResult.error) {
        let errorObject = errorObjectCreator(
            "error in validation !!!!",
            errorCode,
            validationResult.error
        );
        next(errorObject);
    } else {
        next();
    }
};

module.exports = {
    validatorMiddleware,
};
