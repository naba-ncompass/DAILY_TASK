const { fetchResults } = require('../Utilities/db')
const { errorHandle } = require('../Utilities/errorHandler')
const { createResponse } = require('../Utilities/responseHandler')

const getPeakConsumption = async(req,res,next) =>{
    try{
        const { time1, time2, device } = req.query 
        let sqlQuery = `SELECT MAX(CONSUMPTION),DEVICE FROM DC where TIME(TIME) > ? and TIME(TIME) < ? group by DEVICE having DEVICE = ?`
        let sqlValue = [time1,time2,device]
        results = await fetchResults(sqlQuery,sqlValue,1) // 1 for selecting database which contains DC table

        let response = createResponse(results,"get peak consumption")
        res.status(200).send(response)
    }
    catch(err){
        let errorInstance = errorHandle(500,"Internal server error",err)
        next(errorInstance)
    }
}

const getSumConsumption = async(req,res,next) =>{
    try{
        const { time1, time2, device } = req.query 
        let sqlQuery = `SELECT SUM(CONSUMPTION),DEVICE FROM DC where TIME(TIME) > ? and TIME(TIME) < ? group by DEVICE having DEVICE = ?`
        let sqlValue = [time1,time2,device]
        results = await fetchResults(sqlQuery,sqlValue,1) 

        let response = createResponse(results,"get sum consumption")
        res.status(200).send(response)
    }
    catch(err){
        let errorInstance = errorHandle(500,"Internal server error",err)
        next(errorInstance)
    }
}

const getDuplicateTime = async(req,res,next) =>{
    try{
        const { time1, time2, device } = req.query 
        let sqlQuery = `SELECT DEVICE,TIME,COUNT(TIME) as COUNT FROM DC where TIME(TIME) > ? and TIME(TIME) < ? group by DEVICE, TIME HAVING COUNT(TIME)>1 and DEVICE = ?`
        let sqlValue = [time1,time2,device]
        results = await fetchResults(sqlQuery,sqlValue,1) 

        let response = createResponse(results,"get duplicate time")
        res.status(200).send(response)
    }
    catch(err){
        let errorInstance = errorHandle(500,"Internal server error",err)
        next(errorInstance)
    }
}

module.exports = {
    getPeakConsumption,
    getSumConsumption,
    getDuplicateTime
}