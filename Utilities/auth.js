const jwt = require('jsonwebtoken')
const config = require('../Config/config.json')
const { errorHandle } = require('../Utilities/errorHandler')


const jwtSign = (params) => {
    return jwt.sign(params,config.jwt_secret_key,{expiresIn:'2h'})
}


const verifyToken = (req,res,next) =>{
    const token = req.rawHeaders[1].split(" ")[1] 

    if(!token){
        let err = new Error()
        err.message = "Token not found"
        let errorInstance = errorHandle(403,"Forbidden",err)
        return next(errorInstance)
    }

    try{
        const decoded = jwt.verify(token,config.jwt_secret_key)
        req.userId = decoded.id
        next();
    }
    catch(err){
        let errorInstance = errorHandle(401,"Unauthorized",err)
        next(errorInstance)
    }
}


module.exports = {
    jwtSign,
    verifyToken
}