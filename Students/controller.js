const md5 = require("md5");
const db = require("../Utilities/db-operations");
const { customResponse } = require("../Utilities/custom-response");
const { createToken } = require("../Utilities/authorization");

const getInsert = async (req, res) => {
  const hash = md5(req.body.password);
  let body = [
    req.body.id,
    req.body.username,
    req.body.email,
    hash,
    req.body.phone_no,
  ];

  let query =
    "INSERT INTO Students(id,username,email,password,phone_no) VALUES (?)";
  let result = await db.executeQuery(query, [body]).catch(function reject(err) {
    return { err_code: 500, message: err.sqlMessage };
  });

  if ("err_code" in result) {
    return customResponse(result, res);
  } else {
    //if no error create token and send new result obj
    let token = createToken(req.body.username);
    let newresult = {
      code: 200,
      message: `${result.affectedRows} student added to db`,
      token: token,
    };

    return customResponse(newresult, res);
  }
};

const getInsertMultiple = async (req, res) => {
  let users = [];
  req.body.forEach((user) => {
    let hash = md5(user.password);
    users.push([
      user.id,
      user.username,
      user.email,
      hash,
      user.phone_no,
    ]);
  });

  let query =
    "INSERT INTO Students(id,username,email,password,phone_no) VALUES ?";
  let result = await db.executeQuery(query, [users]).catch(function reject(err) {
    return { err_code: 500, message: err.sqlMessage };
  });

  return customResponse(result,res)
};

const getUpdate = async (req, res) => {
  let body = [req.body.new_value, req.body.id];
  let query = `UPDATE Students SET ${req.body.column} = ? WHERE id=?`;

  let result = await db.executeQuery(query, body).catch(function reject(err) {
    return { err_code: 500, message: err.sqlMessage };
  });

  return customResponse(result, res);
};

const getDelete = async (req, res) => {
  body = [req.body.id];
  let query = "DELETE FROM Students WHERE id=?";

  let result = await db.executeQuery(query, body).catch(function reject(err) {
    return { err_code: 500, message: err.sqlMessage };
  });

  return customResponse(result, res);
};

const getSelect = async (req, res) => {
  let body = req.params._id;
  let query = "SELECT * FROM Students WHERE id=?";

  let result = await db.executeQuery(query, body).catch(function reject(err) {
    return { err_code: 500, message: err.sqlMessage };
  });

  result.currentUser = req.userData.username;
  return customResponse(result, res);
};

const getSelectAll = async (req, res) => {
  let body = [];
  let query = "SELECT * FROM Students";
  let result = await db.executeQuery(query, body).catch(function reject(err) {
    return { err_code: 500, message: err.sqlMessage };
  });

  result.currentUser = req.userData.username;
  return customResponse(result, res);
};

const getLogin = async (req, res) => {
  let username = req.body.username;
  let user_pass = req.body.password;

  let query = "SELECT password FROM Students WHERE username = ?";
  let body = [username];

  let result = await db.executeQuery(query, body).catch(function reject(err) {
    return err;
  });

  //check if user exists
  if (result.length === 0) {
    return customResponse(
      { err_code: 404, message: "user does not exist" },
      res
    );
  } else {
    let token = createToken(req.body.username);
    password = result[0].password;
    let hash = md5(user_pass);
    if (password === hash) {
      return customResponse(
        { code: 200, message: "login successful", token: token },
        res
      );
    } else {
      return customResponse(
        { code: 401, message: "login unsuccessful - password wrong" },
        res
      );
    }
  }
};

module.exports = {
  getInsert,
  getUpdate,
  getDelete,
  getSelect,
  getSelectAll,
  customResponse,
  getLogin,
  getInsertMultiple
};
