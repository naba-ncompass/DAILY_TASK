const express = require('express')
const studentRouter = express.Router()
const { readAllStudents, readSpecificStudent,signingStudent,updateStudent,deleteStudent,loginStudent, insertMultipleStudents } = require('./controller')
const { validateMiddleware,validateArrayofObjectsMiddleware } = require('./validation')
const { verifyToken } = require('../Utilities/auth')
const { createErrorResponse } = require('../Utilities/errorHandler')

studentRouter.get('/getAll',verifyToken,readAllStudents)
studentRouter.get('/get',verifyToken, validateMiddleware,readSpecificStudent)
studentRouter.post('/insert',verifyToken,validateArrayofObjectsMiddleware,insertMultipleStudents)
studentRouter.post('/signin',validateMiddleware,signingStudent)
studentRouter.put('/update',verifyToken, validateMiddleware,updateStudent)
studentRouter.delete('/delete',verifyToken, validateMiddleware,deleteStudent)
studentRouter.post('/login',validateMiddleware,loginStudent)

studentRouter.use(createErrorResponse)


module.exports = studentRouter
