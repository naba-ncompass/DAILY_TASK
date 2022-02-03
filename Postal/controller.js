const fetch = require("node-fetch");
const { cacheData } = require("../Utilities/caching");
const { errorObjectCreator } = require("../Utilities/errorHandler");
const { makeResponse } = require("../Utilities/responseMaker");

const getPostal = async (req, res, next) => {
    try {
        const pincode = req.query.pin;
        const result = await fetch(
            `https://api.postalpincode.in/pincode/${pincode}`
        ).then((response) => response.json());
        if (result[0].Status === "Error") {
            throw new Error("invalid pincode");
        }
        else {
            await cacheData(pincode,JSON.stringify(result));
            res.send(makeResponse("fetching successful !!", result));
        }
    } catch (error) {
        let errorObject = errorObjectCreator(
            "error while fetching data",
            401,
            error
        );
        next(errorObject);
    }
};

module.exports = {
    getPostal,
};
