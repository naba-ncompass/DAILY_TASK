const Joi = require("joi");
const { errorObjectCreator } = require("../Utilities/errorHandler");

const schema = Joi.object({
    device: Joi.string().pattern(new RegExp("^D[1-3]$")).min(2).max(2),

    time1: Joi.string()
        .pattern(
            new RegExp(
                "^[0-1][0-9]:[0-5][0-9]:[0-5][0-9]$|^[2][0-3]:[0-5][0-9]:[0-5][0-9]"
            )
        )
        .min(8)
        .max(8),

    time2: Joi.string()
        .pattern(
            new RegExp(
                "^[0-1][0-9]:[0-5][0-9]:[0-5][0-9]$|^[2][0-3]:[0-5][0-9]:[0-5][0-9]"
            )
        )
        .min(8)
        .max(8),
}).unknown(true);

const validateData = (data) => {
    return schema.validate(data);
};

const validatorMiddleware = (req, res, next) => {
    var errorCode = 400;
    data = req.query;
    var validationResult = validateData(data);
    if (validationResult.error) {
        let errorObject = errorObjectCreator(
            "error in validation !!!!",
            errorCode,
            validationResult.error
        );
        next(errorObject);
    } else {
        if(Object.keys(data).length > 1){
            if(data.time1 < data.time2){
                next();
            }
            else{
                let errorObject = errorObjectCreator(
                    "time1 is not smaller than time2",
                    errorCode,
                    new Error("time not compatible")
                );
                next(errorObject);
            }
        }
        else{
            next();
        }
        
    }
};

module.exports = {
    validatorMiddleware,
};
