const { customResponse } = require("../Utilities/custom-response");
const db = require("../Utilities/db-operations");

const sum = async (req, res) => {
  let body = [req.body.device, req.body.from, req.body.to];
  let query =
    "SELECT device ,SUM(consumption)  FROM Device WHERE device=? AND time(time) BETWEEN ? AND ? GROUP BY device;";
  let result = await db.executeQuery(query, body).catch(function reject(err) {
    return { err_code: 500, message: err.sqlMessage };
  });

  return customResponse(result, res);
};

const peak = async (req, res) => {
  let body = [req.body.device, req.body.from, req.body.to];
  let query =
    "SELECT device ,MAX(consumption)  FROM Device WHERE device=? AND time(time) BETWEEN ? AND ? GROUP BY device;";
  let result = await db.executeQuery(query, body).catch(function reject(err) {
    return { err_code: 500, message: err.sqlMessage };
  });

  return customResponse(result, res);
};
module.exports = {
  sum,
  peak,
};
