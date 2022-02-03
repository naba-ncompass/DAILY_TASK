//funtion to create custom error response
const errorResponse = (result,res) => {
  let resObj = {};
  resObj.success = false;
  //422 -> specifically validation error
    resObj.message = result.message;
    resObj.status = result.err_code;
  return res.status(resObj.status).json(resObj);
};

//function to customize delete and update responses
const singleResponse = (affectedRows) => {
  let resObj = {};
  if (affectedRows > 0) {
    resObj.success = true;
    resObj.message = `no of records changed ${affectedRows}`;
    resObj.status = 201;
  } else {
    resObj.success = false;
    resObj.message = "record does not exist";
    resObj.status = 404;
  }
  return resObj;
};

//function to customize select responses
const multiResponse = (result) => {
  let resObj = {};
  if (result.length == 0) {
    resObj.success = false;
    resObj.message = "record doesn't exist";
    resObj.status = 404;
  } else {
    resObj.success = true;
    resObj.data = result;
    resObj.currentUser = result.currentUser;
    resObj.status = 200;
  }

  return resObj;
};

const customResponse = (result, res) => {
  let resObj = {};

  //customizes login and insert responses
  if ("token" in result) {
    resObj.success = true;
    resObj.message = result.message;
    resObj.token = result.token;
    resObj.status = 200;
  } else if (result.constructor.name === "OkPacket") {
    resObj = singleResponse(result.affectedRows);
  } else {
    resObj = multiResponse(result);
  }

  return res.status(resObj.status).json(resObj);
};

module.exports = {
  errorResponse,
  customResponse,
};
