const { makeErrorResponse } = require("./responseMaker")

const errorHandler = (err, req, res, next) => {
    res.status(err.code);
    res.json(makeErrorResponse(err.message,err.error));
  }

const errorObjectCreator = (message,errorCode,error) => {
    let errorObject = new Error;
    errorObject = {
        message:message,
        code:errorCode,
        error:error.message
    };
    return errorObject
}

module.exports = {
    errorHandler,
    errorObjectCreator
}

