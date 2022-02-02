const Joi = require("Joi")


const Schema = Joi.object({
    id: Joi.number().min(1).required(),
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



const createValidationErrorResponse = (error) =>{
    let validationErrorResponse = new Object()
    validationErrorResponse.status = 400
    validationErrorResponse.message = error.details
    validationErrorResponse.success = false
    return validationErrorResponse
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
        validationErrorResponse = createValidationErrorResponse(validationResult.error)
        res.status(400).send(validationErrorResponse)
    }
    else{
        next()
    }
}

const validateArrayofObjectsMiddleware = async (req,res,next) =>{
    let validationResult = validateArrayOfParams(req.body)
    if(validationResult.error){
        validationErrorResponse = createValidationErrorResponse(validationResult.error)
        res.status(400).send(validationErrorResponse)
    }
    else{
        next()
    }
}




module.exports = {
    validateMiddleware,
    validateArrayofObjectsMiddleware
}