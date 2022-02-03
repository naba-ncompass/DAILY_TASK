const menu = require('./Student-console/console-menu')
const express = require('express')
const bodyParser = require("body-parser");
const app = express()
const compression = require('compression')
const config = require('./Config/config.json')
const studentRouter = require('./Students/routes')
const deviceRouter = require('./Device/routes')
const { customResponse } = require('./Utilities/custom-response')
const { globalErrCatcher } = require('./Utilities/errorhandling')

app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());
app.use(compression({ level  : 6}))
app.use('/student',studentRouter);
app.use('/device', deviceRouter)
app.use(globalErrCatcher)
//menu.menu()

app.use(function (req, res) {
    return customResponse({ err_code: 404 , message: "Page not Found"},res)
})

app.listen(config.PORT, () => {
    console.log(`App listening on port ${config.PORT}`)
  })