const errorHandle = (statusCode,info,error=new Error()) =>{
    let errorInstance = new Error()
    errorInstance.code = statusCode
    errorInstance.info = info
    errorInstance.name = error.name
    if(error.message.length!==0) errorInstance.message = error.message
    errorInstance.success = false
    return errorInstance

}
const createErrorResponse = (err,req,res,next) =>{
    res.status(err.code).send(err)    
}


module.exports = {
    createErrorResponse,
    errorHandle
}