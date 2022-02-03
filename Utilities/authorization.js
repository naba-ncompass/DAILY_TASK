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
   next(err)
  }
};

//create token function
const createToken = (user) => {
  const token = jwt.sign(
    {
      username: user.username,
      id: user.id
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
