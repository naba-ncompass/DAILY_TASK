const { errorHandle } = require('../Utilities/errorHandler')
const { createResponse } = require('../Utilities/responseHandler')
const axios = require('axios')
const Redis = require('redis')

const redisConnect = async() =>{
    const redisClient = Redis.createClient(6379)
    redisClient.on('error',(err)=>{
        console.log('Redis Client Error')
    })
    await redisClient.connect()
    return redisClient
}

const postalInformation = async (req,res,next) =>{
    try{
        const { pincode } = req.query

        let redisClient = await redisConnect()

        let data = await redisClient.get(`${pincode}`)
        if(data!==null){
            await redisClient.quit()
            data = JSON.parse(data)
            const response = createResponse(data,"Read all data")
            return res.status(200).send(response)
        }

        const url = `https://api.postalpincode.in/pincode/${pincode}`
        let results = await axios.get(url)

        let newData = results.data
        if(newData[0].Status==="Error"){
            let err = new Error();
            err.message= newData[0].Message
            let errorInstance = errorHandle(404,"Not Found",err)
            throw errorInstance
        }
        else{
            redisClient.setEx(`${pincode}`,3600,JSON.stringify(newData))
            await redisClient.quit()
            const response = createResponse(newData,"Read all data")
            res.status(200).send(response)
        }
    }
    catch(err){
        next(err)
    }
}

module.exports = {
   postalInformation
}