const deviceRouter = require("express").Router()
const { sum , peak , duplicate} = require('./controller')
const { validateDevice } = require('./validate')

deviceRouter.get("/sum",validateDevice,sum)
deviceRouter.get("/peak",validateDevice,peak)
deviceRouter.get("/duplicate/:device",duplicate)

module.exports = deviceRouter
