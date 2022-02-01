const jwt = require('jsonwebtoken')
const config = require('../Config/config.json')


const jwtSign = (params) => {
    return jwt.sign(params,config.jwt_secret_key,{expiresIn:'2h'})
}


const verifyToken = (req,res,next) =>{
    const token = req.rawHeaders[1].split(" ")[1] 

    if(!token) return res.status(403).send({message:"A token is required",success:false})

    try{
        const decoded = jwt.verify(token,config.jwt_secret_key)
        req.userId = decoded.id
        return next();
    }
    catch(err){
        return res.status(401).send({message:err.name,success:false})
    }
}


module.exports = {
    jwtSign,
    verifyToken
}