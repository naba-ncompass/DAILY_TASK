const jwt = require('jsonwebtoken');
const config = require("../Config/config.json")

const tokenCreator = (username) => {

    let jwtSecretKey = config.JWT_SECRET_KEY;
    let data = {
        username: username,
    }
    return jwt.sign(data, jwtSecretKey, { expiresIn: "30m" });
}

module.exports = {
    tokenCreator
}