const jwt = require("jsonwebtoken");
const config = require("../Config/config");
const responsehandler = require("./response_handler")

const verifyToken = (req, res, next) => {

  try {
    const token = req.rawHeaders[1].split(" ")[1] || req.headers["access_token"];
    if (!token) {
      return res.status(403).json(responsehandler.makeResponse("A token is required for authentication"));
    }
    const decoded = jwt.verify(token, config.token);
    req.email = decoded.email;
  } catch (err) {
    return res.status(401).json(responsehandler.makeErrorResponse(err.name));
  }
  return next();
};


module.exports =  verifyToken;