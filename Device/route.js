const express = require('express')
const deviceRouter = express.Router()
const { getPeakConsumption,getSumConsumption,getDuplicateTime } = require('./controller')
const { validateMiddleware } = require('./validation')

deviceRouter.use(validateMiddleware)
deviceRouter.get('/getPeakConsumption',getPeakConsumption)
deviceRouter.get('/getSumConsumption',getSumConsumption)
deviceRouter.get('/getDuplicateTime',getDuplicateTime)

module.exports = deviceRouter