const { fetchResults } = require('../Utilities/db')
const { createErrorResponse } = require('../Utilities/errorHandler')


const createResponse = (result,message=[],success = true) =>{
    let response = new Object();
    response.data = result;
    response.message = message;
    response.success = success;
    return response
}


const readAllStudents = async (req,res,next) =>{
    try{
        let sqlQuery = "SELECT id,name,dept,username,password FROM STUDENTS"
        results = await fetchResults(sqlQuery)

        let response = createResponse(results,"Read all data")
        res.status(200).send(response)
    }
    catch(err){
        customError = createErrorResponse(err,"Internal Server Error",500)
        res.status(500).send(customError)
    }

}


const readSpecificStudent = async (req,res,next) =>{
    try{
        const { id } = req.query 
        let _id = Number(id)

        let sqlQuery = `SELECT id,name,dept,username,password FROM STUDENTS WHERE ID = (?)`
        let sqlValue = [_id]
        result = await fetchResults(sqlQuery,sqlValue)

        let response = createResponse(result,"Read the data")
        if(result.length===0){
            res.status(404).send({status:404,message:"Not found",success:false})
            return
        }
        res.status(200).send(response)
    }
    catch(err){
        customError = createErrorResponse(err,"Internal Server Error",500)
        res.status(500).send(customError)
    }
}



const insertStudent = async(req,res,next) =>{
    try{
        const {id,name,dept,username,password} = req.body
        let _id = id

        let sqlQuery = `INSERT INTO STUDENTS (id,name,dept,username,password) values ? `
        let sqlValue = [[[_id,name,dept,username,password]]]
        result = await fetchResults(sqlQuery,sqlValue)

        let response = createResponse(result.affectedRows,`${result.affectedRows} row/s inserted`)
        res.status(200).send(response)
    }
    catch(err){
        customError = createErrorResponse(err,"Internal Server Error",500)
        res.status(500).send(customError)
    }
}



const updateStudent = async (req,res,next) =>{
    try{
        const { id } = req.query
        _id = Number(id)

        let columnName = Object.keys(req.body)[0]
        let columnValue = Object.values(req.body)[0]

        let sqlQuery = `UPDATE STUDENTS SET ${columnName} = (?) WHERE ID = (?)`;
        let sqlValue = [columnValue,_id]
        result = await fetchResults(sqlQuery,sqlValue)

        let response = createResponse(result.affectedRows,`${result.affectedRows} row/s updated`)
        res.status(200).send(response)
    }
    catch(err){
        customError = createErrorResponse(err,"Internal Server Error",500)
        res.status(500).send(customError)
    }
}


const deleteStudent = async (req,res,next) =>{
    try{
        const { id } = req.query
        _id = Number(id)

        let sqlQuery = `DELETE FROM STUDENTS WHERE ID = (?)`
        let sqlValue = [_id]
        result = await fetchResults(sqlQuery,sqlValue)

        let response = createResponse(result.affectedRows,`${result.affectedRows} row/s deleted`)
        res.status(200).send(response)
    }
    catch(err){
        customError = createErrorResponse(err,"Internal Server Error",500)
        res.status(500).send(customError)
    }
}


module.exports = {
    readAllStudents,
    readSpecificStudent,
    insertStudent,
    updateStudent,
    deleteStudent
}