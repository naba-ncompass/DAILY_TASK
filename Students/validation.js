const Joi = require("Joi")
const { errorHandle } = require('../Utilities/errorHandler')


const Schema = Joi.object({
    id: Joi.number().min(1),
    name:Joi.string().pattern(new RegExp("^[A-Z]")),
    dept:Joi.string().pattern(new RegExp("^[A-Z]")),
    username:Joi.string().email(),
    password: Joi.string()
})

const validateParams  = (body) =>{
    return Schema.validate(body,{abortEarly: false})
}

// for validating array of objects
const arrayOfSchema = Joi.array().items(Schema)

const validateArrayOfParams = (body) =>{
    return arrayOfSchema.validate(body,{abortEarly: false})
}


const validateMiddleware = async (req,res,next) =>{
    let validationResult 
    const method = await req.method
    if(method === 'POST') validationResult = validateParams(req.body)
    else if(method === 'PUT'){
        body = {...req.query,...req.body}
        validationResult = validateParams(body)
    }
    else validationResult = validateParams(req.query)
    if(validationResult.error){
        let errorInstance = errorHandle(400,"Bad Request",validationResult.error)
        return next(errorInstance)
    }
    else{
        next()
    }
}

// only require for validation of array of objects
const validationErrorMessage = (error) =>{
    let messages = []
    error.details.forEach((detail)=>{
        let rowNumber = detail.path[0]
        let detailMessage = detail.message
        let id = error._original[rowNumber].id
        let message = `In id: ${id}, the error is ${detailMessage}`
        messages.push(message)
    })
    return messages
}

const validateArrayofObjectsMiddleware = async (req,res,next) =>{
    let validationResult = validateArrayOfParams(req.body)
    if(validationResult.error){
        let err = new Error()
        err.name = validationResult.error.name
        err.message = validationErrorMessage(validationResult.error)
        let errorInstance = errorHandle(400,"Bad Request",err)
        return next(errorInstance)
    }
    else{
        next()
    }
}




module.exports = {
    validateMiddleware,
    validateArrayofObjectsMiddleware
}