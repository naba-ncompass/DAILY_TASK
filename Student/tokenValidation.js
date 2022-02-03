const config = require("../Config/config.json");
const jwt = require("jsonwebtoken");
const { errorObjectCreator } = require("../Utilities/errorHandler");
const {checkUser} = require("../Student/controller")

const validateToken = async (req, res, next) => {
    let jwtSecretKey = config.JWT_SECRET_KEY;

    try {
        try {
            var token = req.header("authorization").split(" ")[1];
        } catch (error) {
                let errorObject = errorObjectCreator(
                    "Log in and provide token to access data !!!",
                    401,
                    error
                );
                next(errorObject);
        }
        const verified = jwt.verify(token, jwtSecretKey);
        var username = verified.username;
        if (verified) {
            let availability = await checkUser(username);
            if (availability){
                next();
            }
            else{
                throw new Error("user not found!!");
            }            
        } else {
            throw new Error("user not verified!!");
        }
    } catch (error) {
        if (error.message === "jwt expired") {
            var errorObject = errorObjectCreator(
                "User token expired !!!",
                401,
                new Error("token expired")
            );
           
        } else {
            var errorObject = errorObjectCreator(
                "token verification failed",
                401,
                error
            );
        }
        next(errorObject);
    }
};

module.exports = {
    validateToken,
};
