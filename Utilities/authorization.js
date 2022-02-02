const jwt = require("jsonwebtoken");
const config = require("../Config/config.json");
const { customResponse } = require("./custom-response");


//authorization middle ware
const auth = (req, res, next) => {
  try {
    const token = req.headers.authorization.split(" ")[1];
    const decoded = jwt.verify(token, config.JWTKEY);
    req.userData = decoded;
    next();
  } catch (err) {
    
    if (err.name === "TypeError") {
      return customResponse(
        { err_code: 401, message: "Please enter token" },
        res
      );
    } else if (err.name === "TokenExpiredError") {
      return customResponse(
        { err_code: 401, message: "Token has expired , login again" },
        res
      );
    } else if (err.name === "JsonWebTokenError") {
      return customResponse(
        { err_code: 401, message: "Please enter a correct token" },
        res
      );
    }
    return customResponse({ err_code: 401, message: err.message }, res);
  }
};

//create token function
const createToken = (user) => {
  const token = jwt.sign(
    {
      username: user,
    },
    config.JWTKEY,
    { expiresIn: "5m" }
  );

  return token;
};

module.exports = {
  auth,
  createToken,
};
