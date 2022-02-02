const { fetchResults } = require('../Utilities/db')
const { createErrorResponse } = require('../Utilities/errorHandler')
const { createResponse } = require('../Utilities/responseHandler')

const getPeakConsumption = async(req,res) =>{
    try{
        const { time1, time2, device } = req.query 
        let sqlQuery = `SELECT MAX(CONSUMPTION),DEVICE FROM DC where TIME(TIME) > ? and TIME(TIME) < ? group by DEVICE having DEVICE = ?`
        let sqlValue = [time1,time2,device]
        results = await fetchResults(sqlQuery,sqlValue,1) // 1 for selecting database which contains DC table

        let response = createResponse(results,"get peak consumption")
        res.status(200).send(response)
    }
    catch(err){
        customError = createErrorResponse(err,"Internal Server Error",500)
        res.status(500).send(customError)
    }
}

const getSumConsumption = async(req,res) =>{
    try{
        const { time1, time2, device } = req.query 
        let sqlQuery = `SELECT SUM(CONSUMPTION),DEVICE FROM DC where TIME(TIME) > ? and TIME(TIME) < ? group by DEVICE having DEVICE = ?`
        let sqlValue = [time1,time2,device]
        results = await fetchResults(sqlQuery,sqlValue,1) 

        let response = createResponse(results,"get sum consumption")
        res.status(200).send(response)
    }
    catch(err){
        customError = createErrorResponse(err,"Internal Server Error",500)
        res.status(500).send(customError)
    }
}

const getDuplicateTime = async(req,res) =>{
    try{
        const { time1, time2, device } = req.query 
        let sqlQuery = `SELECT DEVICE,TIME,COUNT(TIME) as COUNT FROM DC where TIME(TIME) > ? and TIME(TIME) < ? group by DEVICE, TIME HAVING COUNT(TIME)>1 and DEVICE = ?`
        let sqlValue = [time1,time2,device]
        results = await fetchResults(sqlQuery,sqlValue,1) 

        let response = createResponse(results,"get duplicate time")
        res.status(200).send(response)
    }
    catch(err){
        customError = createErrorResponse(err,"Internal Server Error",500)
        res.status(500).send(customError)
    }
}

module.exports = {
    getPeakConsumption,
    getSumConsumption,
    getDuplicateTime
}