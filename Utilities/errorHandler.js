const errorHandle = (error) =>{
    return Object.keys(error).reduce((obj,k)=>{
        obj[k] = error[k];
        return obj
    },{});
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