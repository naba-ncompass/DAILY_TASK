const Joi = require("Joi")


const Schema = Joi.object({
    id: Joi.number().min(1).required(),
    name:Joi.string().pattern(new RegExp("^[A-Z]")),
    dept:Joi.string().pattern(new RegExp("^[A-Z]")),
    username:Joi.string().email(),
    password: Joi.string()
})


const validateParams  = (body) =>{
    return Schema.validate(body)
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




module.exports = {
    validateMiddleware 
}