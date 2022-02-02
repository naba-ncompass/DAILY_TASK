const db = require("../Utilities/db-operations");
const prompt = require("prompt-sync")({ sigint: true });

let getInsert = async (body) => {

  query = "INSERT INTO Students(id,username,email,password) VALUES (?)";
  let result = await db.executeQuery(query, [body]).catch(function reject(err) {
    return err;
  });

  return result;
};

let getUpdate = async (body) => {

  query = "UPDATE Students SET username = ? WHERE id=?";

  let result = await db.executeQuery(query, body).catch(function reject(err) {
    return err;
  });
  return result;
};

let getDelete = async (body) => {

  query = "DELETE FROM Students WHERE id=?";

  let result = await db.executeQuery(query, body).catch(function reject(err) {
    return err;
  });
  return result;
};

let getSelect = async (body) => {

  let query = "SELECT * FROM Students WHERE id=?";

  let result = await db.executeQuery(query, body).catch(function reject(err) {
    return err;
  });
  return result;
};

let getSelectAll = async () => {
  let body = [];
  query = "SELECT * FROM Students";
  let result = await db.executeQuery(query, body).catch(function reject(err) {
    return err;
  });
  return result;
};

let customResponse = (res) => {
  let resObj = {
    success: false,
    message: "",
  };
  
  if ("sqlMessage" in res) {
    resObj.message = res.sqlMessage;
  } else if ("affectedRows" in res) {
    resObj.success = true;
    resObj.message = `no of rows changed ${res.affectedRows}`;
  } else {
    resObj.success = true;
    resObj.data = res;
  }

  return resObj;
};
module.exports = {
  getInsert,
  getUpdate,
  getDelete,
  getSelect,
  getSelectAll,
  customResponse,
};
