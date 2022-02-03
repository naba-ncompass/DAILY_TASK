const executor = require("../Utilities/db");
const responsehandler = require("../Utilities/response_handler");


const readDevice = async (req, res) => {
    try {
        let device = req.body.device;
        const inputData = [device];
        query = `select * from uc3 where device = ?`;
        result = await executor
            .executeQuery(query, inputData)
            .catch(function reject(error) {
                throw error;
            });

            // console.log("READING")
            // result = await executor
            //     .executeQuery("select * from uc3")
            //     .catch(function reject(error) {
            //         throw error;
            //     });
        return res.status(200).json(responsehandler.makeResponse("query successful!!", result));
    } catch (error) {
        return res.status(500).json(responsehandler.makeErrorResponse("error while reading employee by id ", error.message));
    }
};



const maxDevice = async (req, res) => {
    try {
        let time1 = req.body.time1;
        let time2 = req.body.time2;
        let device = req.body.device;
        const inputData = [time1,time2,device];
        if(time1<= time2) 
        {
        query = `select max(CONSUMPTION), device FROM uc3 where TIME(TIME) >  ? AND TIME(TIME) < ? group by device having device = ?`;
        result = await executor
            .executeQuery(query, inputData)
            .catch(function reject(error) {
                throw error;
            });
            return res.status(200).json(responsehandler.makeResponse("query successful!!", result));
         }
        else{
            return res.status(500).json(responsehandler.makeErrorResponse("NOT POSSIBLE TIME 1 is more than time 2 "));
    }
    } catch (error) {
        return res.status(500).json(responsehandler.makeErrorResponse("error while reading employee by id ", error.message));
    }
};



const sumDevice = async (req, res) => {
    try {
        let time1 = req.body.time1;
        let time2 = req.body.time2;
        let device = req.body.device;
        const inputData = [time1,time2,device];
        if(time1<= time2) 
        {
        query = `select sum(CONSUMPTION), device FROM uc3 where TIME(TIME) >  ? AND TIME(TIME) < ? group by device having device = ?`;
        result = await executor
            .executeQuery(query, inputData)
            .catch(function reject(error) {
                throw error;
            });
        return res.status(200).json(responsehandler.makeResponse("query successful!!", result));
    }
    else{
        return res.status(500).json(responsehandler.makeErrorResponse("NOT POSSIBLE TIME 1 is more than time 2 "));
    }
    } catch (error) {
        return res.status(500).json(responsehandler.makeErrorResponse("error while reading employee by id ", error.message));
    }
};


const duplicateDevice = async (req, res) => {
    try {
        let time1 = req.body.time1;
        let time2 = req.body.time2;
        let device = req.body.device;
        const inputData = [time1,time2,device];

        if(time1<= time2) 
        {
            console.log("HI")
            query = `select device, TIME, COUNT(TIME), CONSUMPTION FROM uc3 where TIME(TIME) >  ? AND TIME(TIME) < ? group by device, TIME HAVING COUNT(TIME)>1 and device = ?`;
            result = await executor
            .executeQuery(query, inputData)
            .catch(function reject(error) {
                throw error;
            });
            return res.status(200).json(responsehandler.makeResponse("query successful!!", result));
        }
        else{
            return res.status(500).json(responsehandler.makeErrorResponse("NOT POSSIBLE TIME 1 is more than time 2 "));
        }

            } catch (error) {
        return res.status(500).json(responsehandler.makeErrorResponse("error while reading uc3 by id ", error.message));
    }
};




module.exports = {
    readDevice,
    maxDevice,
    sumDevice,
    duplicateDevice
};

