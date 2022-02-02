const express = require('express')
const deviceRouter = express.Router()
const { getPeakConsumption,getSumConsumption,getDuplicateTime } = require('./controller')
const { validateMiddleware } = require('./validation')
const { createErrorResponse } = require('../Utilities/errorHandler')

deviceRouter.use(validateMiddleware)
deviceRouter.get('/getPeakConsumption',getPeakConsumption)
deviceRouter.get('/getSumConsumption',getSumConsumption)
deviceRouter.get('/getDuplicateTime',getDuplicateTime)

deviceRouter.use(createErrorResponse)

module.exports = deviceRouter