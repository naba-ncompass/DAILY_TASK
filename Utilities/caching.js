const redis = require("redis");
const { errorObjectCreator } = require("./errorHandler");
const { makeResponse } = require("./responseMaker");

const cacheData = async (pincode,data) => {
    const client = redis.createClient();
    client.on('error', (err) => console.log('Redis Client Error'+err));
    await client.connect();
    await client.setEx(pincode, 1500, data);
    await client.quit();
}

const checkCacheData = async (req, res, next) => {
    const pincode = req.query.pin;
    const client = redis.createClient();
    client.on('error', (err) => {
        let errorObject = errorObjectCreator(
            "error while fetching data",
            401,
            err
        );
        next(errorObject);
    });
    await client.connect();
    let result = await client.get(pincode);
    await client.quit();
    if (result === null){
        next();
    }
    else{
        res.send(makeResponse("query successful",JSON.parse(result)));
    }
}

module.exports = {
    cacheData,
    checkCacheData
}