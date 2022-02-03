const { errorResponse } = require("./custom-response");

const globalErrCatcher = (err, req, res, next) => {
  if (!err) {
    return next();
  }

  if (err.name === "TypeError") {
    return errorResponse(
      { err_code: 401, message: "Please enter token" },
      res
    );
  } else if (err.name === "TokenExpiredError") {
    return errorResponse(
      { err_code: 401, message: "Token has expired , login again" },
      res
    );
  } else if (err.name === "JsonWebTokenError") {
    return errorResponse(
      { err_code: 401, message: "Please enter a correct token" },
      res
    );
  }
  else if(err.name === "ValidationError"){
      return errorResponse(
          { err_code : 422 , message: err.message},
          res
      )
  }
  else{
    errorResponse({ err_code: 500, message: err.message }, res);
  }
 
};

module.exports = {
  globalErrCatcher,
};
