const express = require('express')
const studentRouter = express.Router()
const { readAllStudents, readSpecificStudent,insertStudent,updateStudent,deleteStudent } = require('./controller')
const { validateMiddleware } = require('./validation')

studentRouter.get('/getAll',readAllStudents)
studentRouter.get('/get',validateMiddleware,readSpecificStudent)
studentRouter.post('/post',validateMiddleware,insertStudent)
studentRouter.put('/update',validateMiddleware,updateStudent)
studentRouter.delete('/delete',validateMiddleware,deleteStudent)


module.exports = studentRouter
