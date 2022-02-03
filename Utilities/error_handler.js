const errorHandle = (statusCode,info,error=new Error()) =>{
    errorInstance = new Error()
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
// const express = require('express');

// function handleError(
//   err: TypeError | CustomError,
//   req: Request,
//   res: Response,
//   next: NextFunction
// ) {
//   let customError = err;

//   if (!(err instanceof CustomError)) {
//     customError = new CustomError(
//       'Oh no, this is embarrasing. We are having troubles my friend'
//     );
//   }
//   res.status((customError as CustomError).status).send(customError);
// };

// export default handleError;