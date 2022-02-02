const { fetchResults } = require('../Utilities/db')
const { errorHandle } = require('../Utilities/errorHandler')
const { createResponse } = require('../Utilities/responseHandler')
const md5 = require('md5')
const { jwtSign } = require('../Utilities/auth')



// read all the students present in the database
const readAllStudents = async (req,res,next) =>{
    try{
        let sqlQuery = "SELECT id,name,dept,username,password FROM STUDENTS"
        results = await fetchResults(sqlQuery)

        let response = createResponse(results,"Read all data")
        res.status(200).send(response)
    }
    catch(err){
        let errorInstance = errorHandle(500,"Internal server error",err)
        next(errorInstance)
    }

}


// reading student whose id is given
const readSpecificStudent = async (req,res,next) =>{
    try{
        const { id } = req.query 
        let _id = Number(id)

        let sqlQuery = `SELECT id,name,dept,username,password FROM STUDENTS WHERE ID = (?)`
        let sqlValue = [_id]
        result = await fetchResults(sqlQuery,sqlValue)

        let response = createResponse(result,"Read the data")
        // if the no result then 404 error
        if(result.length===0){
            let errorInstance = errorHandle(404,"Not Found")
            next(errorInstance)
            return
        }
        res.status(200).send(response)
    }
    catch(err){
        let errorInstance = errorHandle(500,"Internal server error",err)
        next(errorInstance)
    }
}


// insert multiple student record
const insertMultipleStudents = async(req,res,next) =>{
    try{
        let items = []
        req.body.forEach((body) => {
            let item = Object.values(body)
            let password = item[item.length-1]
            let passwordDisgest = md5(password)
            item[item.length-1] = passwordDisgest // item[item.length-1] contains password
            items.push(item)
        })

        let sqlQuery = `INSERT INTO STUDENTS (id,name,dept,username,password) values ?`
        let sqlValue = [items]
        result = await fetchResults(sqlQuery,sqlValue)

        let response = createResponse(result.affectedRows,`${result.affectedRows} row/s inserted`)
        res.status(200).send(response)
    }
    catch(err){
        let errorInstance = errorHandle(500,"Internal server error",err)
        next(errorInstance) 
    }
}


// student signup
const signingStudent = async(req,res,next) =>{
    try{
        const {id,name,dept,username,password} = req.body
        let _id = id
        let passwordDigest = md5(password)

        let sqlQuery = `INSERT INTO STUDENTS (id,name,dept,username,password) value (?) `
        let sqlValue = [[_id,name,dept,username,passwordDigest]]
        result = await fetchResults(sqlQuery,sqlValue)

        // creating token using jwt
        const token = jwtSign({id:id})
        let response = createResponse(result.affectedRows,'successful Signin',token)
        res.status(200).send(response)
    }
    catch(err){
        let errorInstance = errorHandle(500,"Internal server error",err)
        next(errorInstance) 
    }
}


// update the student data
const updateStudent = async (req,res,next) =>{
    try{
        const id = req.userId
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
        let errorInstance;
        if(err.name==="No Access") errorInstance = errorHandle(403,"Forbidden",err)
        else errorInstance = errorHandle(500,"Internal server error",err)
        next(errorInstance)
    }
}


// delete the student
const deleteStudent = async (req,res,next) =>{
    try{
        const id = req.userId
        _id = Number(id)


        let sqlQuery = `DELETE FROM STUDENTS WHERE ID = (?)`
        let sqlValue = [_id]
        result = await fetchResults(sqlQuery,sqlValue)

        let response = createResponse(result.affectedRows,`${result.affectedRows} row/s deleted`)
        res.status(200).send(response)
    }
    catch(err){
        let errorInstance = errorHandle(500,"Internal server error",err)
        next(errorInstance)
    }
}


// login
const loginStudent = async(req,res,next) =>{
    try{
        const { id, username, password } = req.body
        let passwordDigest = md5(password)

        let sqlQuery = `SELECT EXISTS (SELECT username from students where username = (?) and password = (?) and id = (?)) as present`
        let sqlValue = [username,passwordDigest,id]
        let result = await fetchResults(sqlQuery,sqlValue)
        
        // if the username,password,id not corrent then give error message with check username,password,id
        if(result[0].present===0){
            let errorInstance = errorHandle(404,"Not Found, please check username,password,id")
            //res.status(errorInstance.code).send(errorInstance)
            next(errorInstance)
            return
        }
        
        const token = jwtSign({id:id})
        response = createResponse(result[0].present,'Login in Successful',token)
        res.status(200).send(response)
    }
    catch(err){
        let errorInstance = errorHandle(500,"Internal server error",err)
        next(errorInstance) 
    }
}


module.exports = {
    readAllStudents,
    readSpecificStudent,
    insertMultipleStudents,
    signingStudent,
    updateStudent,
    deleteStudent,
    loginStudent
}