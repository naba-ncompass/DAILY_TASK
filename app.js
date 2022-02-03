const express = require("express");
const config = require("./Config/config");
const studentRoute = require("./Student/routes");
const deviceRoute = require("./Device/routes");
const readWeather = require("./Postal/routes")
const { makeErrorResponse } = require("./Utilities/responseMaker");
const { errorHandler } = require("./Utilities/errorHandler");


const app = express();

const port = config.port_for_app;
const host = config.host_for_app;

app.use(studentRoute);
app.use(deviceRoute);
app.use(readWeather);
// for any other route which is not defined
app.use((req, res) => {
  res.status(404);
  res.json(makeErrorResponse("route does not exists"));
});
app.use(errorHandler);

app.listen(port, host, () => {
  console.log(`Node app listening on port ${host}:${port}`);
});
