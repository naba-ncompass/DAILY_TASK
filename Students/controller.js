const { fetchResults } = require('../Utilities/db')
const { createErrorResponse } = require('../Utilities/errorHandler')
const { createResponse } = require('../Utilities/responseHandler')
const md5 = require('md5')
const { jwtSign } = require('../Utilities/auth')


// check where that id have access to the functions or not
const haveAccess = async (checkId) =>{
    let access = await fetchResults(`SELECT username FROM STUDENTS where id = (?)`,[checkId])
    if(access.length===0) return res.status(403).send({message:"Forbidden",success:false})
}


// read all the students present in the database
const readAllStudents = async (req,res) =>{
    try{
        await haveAccess(req.userId)

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


// reading student whose id is given
const readSpecificStudent = async (req,res) =>{
    try{
        await haveAccess(req.userId)

        const { id } = req.query 
        let _id = Number(id)

        let sqlQuery = `SELECT id,name,dept,username,password FROM STUDENTS WHERE ID = (?)`
        let sqlValue = [_id]
        result = await fetchResults(sqlQuery,sqlValue)

        let response = createResponse(result,"Read the data")
        // if the no result then 404 error
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


// insert multiple student record
const insertMultipleStudents = async(req,res) =>{
    try{
        await haveAccess(req.userId)

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
        customError = createErrorResponse(err,"Internal Server Error",500)
        res.status(500).send(customError)
    }
}


// student signup
const signingStudent = async(req,res) =>{
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
        customError = createErrorResponse(err,"Internal Server Error",500)
        res.status(500).send(customError)
    }
}


// update the student data
const updateStudent = async (req,res) =>{
    try{
        await haveAccess(req.userId)

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


// delete the student
const deleteStudent = async (req,res) =>{
    try{
        await haveAccess(req.userId)

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


// login
const loginStudent = async(req,res) =>{
    try{
        const { id, username, password } = req.body
        let passwordDigest = md5(password)

        let sqlQuery = `SELECT EXISTS (SELECT username from students where username = (?) and password = (?) and id = (?)) as present`
        let sqlValue = [username,passwordDigest,id]
        let result = await fetchResults(sqlQuery,sqlValue)
        
        // if the username,password,id not corrent then give error message with check username,password,id
        if(result[0].present===0){
            return res.status(404).send({status:404,message:"Not found, please check the username,password and id",success:false})
        }
        
        const token = jwtSign({id:id})
        response = createResponse(result[0].present,'Login in Successful',token)
        res.status(200).send(response)
    }
    catch(err){
        console.log(err)
        customError = createErrorResponse(err,"Internal Server Error",500)
        res.status(500).send(customError)
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