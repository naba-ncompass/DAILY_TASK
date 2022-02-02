const express = require('express')
const studentRoute = require('./Students/route')
const deviceRouter = require('./Device/route')
const config = require('./Config/config.json')
const compression = require('compression')

app = express()


app.use(compression({
    level:6
}))

app.use(express.json())
app.use(express.urlencoded({ extended: true }))

app.use('/records',studentRoute) 
app.use('/device',deviceRouter)

app.use((req, res)=>{
    res.status(404);
    res.send({message:"Not found",status:404,success:false});
})

const port = config.app_config.port
const host = config.app_config.host
app.listen(port,host, ()=>{
    console.log(`App is running at port ${port} and host ${host}`);
})