const deviceRouter = require("express").Router()
const { sum , peak } = require('./controller')

deviceRouter.get("/", (req,res) => {
    res.send("check")
})

deviceRouter.get("/sum",sum)
deviceRouter.get("/peak",peak)

module.exports = deviceRouter
