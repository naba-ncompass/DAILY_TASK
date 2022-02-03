const Joi = require("Joi")
const { errorHandle } = require('../Utilities/errorHandler')

const Schema = Joi.object({
    pincode: Joi.string().pattern(new RegExp("^[0-9]{6}$")).required()
})

const validateParams  = (queryParams) =>{
    return Schema.validate(queryParams)
}

const validateMiddleware = async (req,res,next) =>{
    let validationResult=validateParams(req.query)
    if(validationResult.error){
        let errorInstance = errorHandle(400,"Bad Request",validationResult.error)
        return next(errorInstance)
    }
    else{
        next()
    }
}

module.exports = {
    validateMiddleware
}