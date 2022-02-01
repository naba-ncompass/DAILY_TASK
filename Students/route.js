const express = require('express')
const studentRouter = express.Router()
const { readAllStudents, readSpecificStudent,signingStudent,updateStudent,deleteStudent,loginStudent } = require('./controller')
const { validateMiddleware } = require('./validation')
const { verifyToken } = require('../Utilities/auth')

studentRouter.get('/getAll',verifyToken,readAllStudents)
studentRouter.get('/get',verifyToken, validateMiddleware,readSpecificStudent)
studentRouter.post('/signin',validateMiddleware,signingStudent)
studentRouter.put('/update',verifyToken, validateMiddleware,updateStudent)
studentRouter.delete('/delete',verifyToken, validateMiddleware,deleteStudent)
studentRouter.post('/login',validateMiddleware,loginStudent)


module.exports = studentRouter
