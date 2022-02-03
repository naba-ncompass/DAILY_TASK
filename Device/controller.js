const { executeQuery } = require("../Utilities/db");
const { errorObjectCreator } = require("../Utilities/errorHandler");
const { makeResponse } = require("../Utilities/responseMaker");

var errorCode = 500;

exports.readDeviceData = async (req, res, next) => {
    try {
        let data = req.query;
        const inputData = [data.device];
        let query = `select * from uc3 where device = ?`;
        let result = await executeQuery(query, inputData).catch(function reject(
            error
        ) {
            throw error;
        });
        let response = makeResponse("query successful!!", result);
        return res.json(response);
    } catch (error) {
        let errorObject = errorObjectCreator(
            "error while reading device data",
            errorCode,
            error
        );
        next(errorObject);
    }
};

exports.peakConsumption = async (req, res, next) => {
    try {
        let data = req.query;
        const inputData = [data.time1, data.time2, data.device];
        let query = `select max(CONSUMPTION), DEVICE FROM uc3 where TIME(TIME) > ? AND TIME(TIME) < ? group by DEVICE having DEVICE = ?`;
        let result = await executeQuery(query, inputData).catch(function reject(
            error
        ) {
            throw error;
        });

        let response = makeResponse("query successful!!", result);
        return res.json(response);
    } catch (error) {
        let errorObject = errorObjectCreator(
            "error while reading peak consumption",
            errorCode,
            error
        );
        next(errorObject);
    }
};

exports.sumConsumption = async (req, res, next) => {
    try {
        let data = req.query;
        const inputData = [data.time1, data.time2, data.device];
        let query = `select sum(CONSUMPTION), DEVICE FROM uc3 where TIME(TIME) > ? AND TIME(TIME) < ? group by DEVICE having DEVICE = ?`;
        let result = await executeQuery(query, inputData).catch(function reject(
            error
        ) {
            throw error;
        });

        let response = makeResponse("query successful!!", result);
        return res.json(response);
    } catch (error) {
        let errorObject = errorObjectCreator(
            "error while reading sum of consumption",
            errorCode,
            error
        );
        next(errorObject);
    }
};

exports.duplicateData = async (req, res, next) => {
    try {
        let data = req.query;
        const inputData = [data.time1, data.time2, data.device];
        let query = `select DEVICE, TIME, COUNT(TIME), CONSUMPTION FROM uc3 where TIME(TIME) > ? AND TIME(TIME) < ? group by DEVICE, TIME HAVING COUNT(TIME)>1 and DEVICE = ?`;
        let result = await executeQuery(query, inputData).catch(function reject(
            error
        ) {
            throw error;
        });

        let response = makeResponse("query successful!!", result);
        return res.json(response);
    } catch (error) {
        let errorObject = errorObjectCreator(
            "error while reading duplicate time data",
            errorCode,
            error
        );
        next(errorObject);
    }
};
