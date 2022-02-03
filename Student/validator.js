const Joi = require("joi");
const { errorObjectCreator } = require("../Utilities/errorHandler");

const schema = Joi.object({
    id: Joi.string().pattern(new RegExp("^S+[0-9]+$")).min(4).max(4),

    name: Joi.string(),

    department: Joi.string(),

    cgpa: Joi.number().max(10).min(0),

    username: Joi.string().email(),

    password: Joi.string(),

    phone: Joi.string().min(10).max(10).pattern(new RegExp("^[0-9]+$")),
}).unknown(true);

const validateData = (data) => {
    return schema.validate(data);
};

const validateInsertData = (data) => {
    const arraySchema = Joi.array().items(schema);
    return arraySchema.validate(data,{ abortEarly: false });
}

const validatorMiddleware = (req, res, next) => {
    var errorCode = 400;
    if(req.method === "GET"){
        var data = req.query;
    }
    else{
        var data = req.body;
    }
    
    if (Object.prototype.toString.call(data) === '[object Array]'){
        var validationResult =  validateInsertData(data);
        if (validationResult.error) {
            let validationError = validationResult.error.details;
            var errorArray = [];
            for(let i=0;i<validationError.length;i++){
                let errorContent = `${validationError[i].context.value} at ${validationError[i].context.key} is not allowed because ${validationError[i].message}`
                errorArray.push(errorContent);
            }
            let errorObject = errorObjectCreator(
                "error in validation !!!!",
                errorCode,
                new Error(errorArray.join('---------------'))
            );
            next(errorObject);
        }
        else{
            next();
        }
    }
    else{
        let validationResult = validateData(data);
        if (validationResult.error) {
            let errorObject = errorObjectCreator(
                "error in validation !!!!",
                errorCode,
                validationResult.error
            );
            next(errorObject);
        }
        else{
            next();
        }    
    }
}

module.exports = {
    validatorMiddleware
}