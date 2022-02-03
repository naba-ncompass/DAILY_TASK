const { customResponse } = require("../Utilities/custom-response");
const db = require("../Utilities/db-operations");

const sum = async (req, res,next) => {
  let body = [req.body.device, req.body.from, req.body.to];
  let query =
    "SELECT device ,SUM(consumption)  FROM Device WHERE device=? AND time(time) BETWEEN ? AND ? GROUP BY device;";
  let result = await db.executeQuery(query, body).catch(function reject(err) {
    next(Error(sql.message))
    return null
  });

  if(result!==null)return customResponse(result, res);
};

const peak = async (req, res,next) => {
  let body = [req.body.device, req.body.from, req.body.to];
  let query =
    "SELECT device ,MAX(consumption)  FROM Device WHERE device=? AND time(time) BETWEEN ? AND ? GROUP BY device;";
  let result = await db.executeQuery(query, body).catch(function reject(err) {
    next(Error(sql.message))
    return null
  });

  if(result!==null)return customResponse(result, res);
};

const duplicate = async(req,res,next) => {

  let device = req.params.device
  let query = "SELECT time, COUNT(*) AS count FROM Device WHERE device=? GROUP BY time HAVING COUNT(*)"

  let result = await db.executeQuery(query,device).catch(function reject(err) {
    next(Error(sql.message))
    return null
  });

  if(result!==null)return customResponse(result,res)
}
module.exports = {
  sum,
  peak,
  duplicate
};
