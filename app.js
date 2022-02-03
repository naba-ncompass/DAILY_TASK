const config = require('./Config/config');
const express = require('express');
const employeeRoutes = require('./Employee/route');
const deviceRoutes = require('./Device/route');
const pincodes = require('./Pincode/route');
const compression = require('compression');

const app = express();

app.use(compression({
    level: 6
}))

app.use(employeeRoutes);
app.use(deviceRoutes);
app.use(pincodes);

app.get('/', (req, res) => {
    res.send('Hello World');
});

//app.get(('/pincode', pincodes));


app.listen(config.port, () => {
    console.log(`NODE JS  is running `);
});

app.use((req, res) => {
    res.status(404);
    res.send({ error: 'Route does not Exist', success: false });
});


app.use((error, req, res, next) => {
    res.status(500);
    res.send({error: 'Internal Server Error',success: false  });
});









// app.use((err, req, res, next) => {
//     res.status(err.status || 500);
//     res.send({
//         error: {
//             status: err.status || 500,
//             message: err.message
//         }
//     })
//     next(err);
// });