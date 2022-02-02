const Joi = require("Joi")

const Schema = Joi.object({
    time1: Joi.string().max(8).pattern(new RegExp("^[0-1][0-9]:[0-5][0-9]:[0-5][0-9]$|^[2][0-3]:[0-5][0-9]:[0-5][0-9]")).required(),
    time2: Joi.string().max(8).pattern(new RegExp("^[0-1][0-9]:[0-5][0-9]:[0-5][0-9]$|^[2][0-3]:[0-5][0-9]:[0-5][0-9]")).required(),
    device:Joi.string().max(3).pattern(new RegExp("^D[1-3]$"))
})

const validateParams  = (body) =>{
    return Schema.validate(body,{abortEarly: false})
}

const createValidationErrorResponse = (error) =>{
    let validationErrorResponse = new Object()
    validationErrorResponse.status = 400
    validationErrorResponse.message = error.details
    validationErrorResponse.success = false
    return validationErrorResponse
}

const validateMiddleware = async (req,res,next) =>{
    let validationResult = validateParams(req.query)
    if(validationResult.error){
        validationErrorResponse = createValidationErrorResponse(validationResult.error)
        res.status(400).send(validationErrorResponse)
    }
    else{
        next()
    }
}

module.exports = {
    validateMiddleware
}