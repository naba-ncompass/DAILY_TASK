const axios = require('axios');
const responsehandler = require("../Utilities/response_handler");
const redis = require('redis');

const DEFAULT_EXPIRATION = 3600;

// const pincode = async (req,res) => {
//     try{
//         const pincode = req.query.pincode;
//         console.log(pincode)
//         const url = `https://api.postalpincode.in/pincode/${pincode}`;
//         // let data = await axios.get('https://api.postalpincode.in/pincode/110001');
//         const result = await axios.get(url)
//         const data = result.data;
//         const response = responsehandler.makeResponse("all data",data);
//         return res.status(200).send(response)
//         }
//     catch(error){
//         return res.status(500).json(responsehandler.makeErrorResponse("error while inserting employee data", error.message));

//     }
// }


const pincode = async (req,res) => {
    try{
        const redisClient = redis.createClient();
        await redisClient.connect();

        const pincode = req.query.pincode;
        const redix_value = await redisClient.get(pincode)
        console.log(redix_value)

        if (redix_value)
        {
            console.log("_---------------")
            // await redisClient.quit();
            res.status(400).send(JSON.parse(redix_value));
        }
        else{
            let results = await axios.get(`https://api.postalpincode.in/pincode/${pincode}`);
            console.log(results);
            if(results.data[0].Status !== "Error"){
                console.log('MISS')
                redisClient.setEx(pincode,3600, JSON.stringify(results.data))
                await redisClient.quit();
                return res.status(200).send(responsehandler.makeResponse("fetching",results.data));
                //json(JSON.parse(data))
            }else{
                console.log('HIT')
                return res.status(500).send(responsehandler.makeErrorResponse("Pincode does not exist",results.data));
            }
        }
            //res.json(results)
        }
    catch(error){
        return res.status(500).json(responsehandler.makeErrorResponse("error while inserting employee data", error.message));
    }
}

module.exports = 
{
    pincode
};