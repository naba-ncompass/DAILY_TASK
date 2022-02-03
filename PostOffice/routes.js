const addressRouter = require("express").Router();
const { getAddress } = require('./controller')
const { validatePin } = require('./validate')


addressRouter.get('/getdata',validatePin,getAddress)


module.exports = addressRouter