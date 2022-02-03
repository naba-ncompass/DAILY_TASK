const express = require('express')
const { postalInformation } = require('./controller')
const { createErrorResponse } = require('../Utilities/errorHandler')
const { validateMiddleware } = require('./validation')

const postalRouter = express.Router()

postalRouter.use(validateMiddleware)

postalRouter.get("/getInfo",postalInformation)

postalRouter.use(createErrorResponse)

module.exports = postalRouter