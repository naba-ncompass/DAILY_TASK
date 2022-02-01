const errorHandle = (error) =>{
    const errorInstance = Object.keys(error).reduce((obj,k)=>{
        obj[k] = error[k];
        return obj
    },{})
    errorInstance.name = error.name
    errorInstance.message = error.message
    return errorInstance

}
const createErrorResponse = (error,message,statusCode) =>{
    const errorData = errorHandle(error);
    let errorResponse = new Object();
    errorResponse.status = statusCode
    errorResponse.success = false;
    errorResponse.data = errorData;
    errorResponse.message = message;
    return errorResponse
    
}


module.exports = {
    createErrorResponse,
}