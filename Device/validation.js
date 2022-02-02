const Joi = require("Joi")
const { errorHandle } = require('../Utilities/errorHandler')

const Schema = Joi.object({
    time1: Joi.string().max(8).pattern(new RegExp("^[0-1][0-9]:[0-5][0-9]:[0-5][0-9]$|^[2][0-3]:[0-5][0-9]:[0-5][0-9]")).required(),
    time2: Joi.string().max(8).pattern(new RegExp("^[0-1][0-9]:[0-5][0-9]:[0-5][0-9]$|^[2][0-3]:[0-5][0-9]:[0-5][0-9]")).required(),
    device:Joi.string().max(3).pattern(new RegExp("^D[1-3]$"))
})

const validateParams  = (body) =>{
    return Schema.validate(body,{abortEarly: false})
}


const validateMiddleware = async (req,res,next) =>{
    if(req.query.time1 >= req.query.time2){
        let err = new Error()
        err.message = "time1 is greate than or equal to time2"
        let errorInstance = errorHandle(400,"Bad Request",err)
        return next(errorInstance)
    }
    let validationResult = validateParams(req.query)
    if(validationResult.error){
        let errorInstance = errorHandle(400,"Bad Request",validationResult.error)
        next(errorInstance)
    }
    else{
        next()
    }
}

module.exports = {
    validateMiddleware
}