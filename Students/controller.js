const md5 = require("md5");
const db = require("../Utilities/db-operations");
const { customResponse } = require("../Utilities/custom-response");
const { createToken } = require("../Utilities/authorization");

const getInsert = async (req, res, next) => {
  try {
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
    let result = await db
      .executeQuery(query, [body])
      .catch(function reject(err) {
        next(Error(err.sqlMessage));
        return null;
      });

    if (result !== null) {
      let user = { username: req.body.username, id: req.body.id };
      let token = createToken(user);
      let newresult = {
        code: 200,
        message: `${result.affectedRows} student added to db`,
        token: token,
      };

      return customResponse(newresult, res);
    }
  } catch (err) {
    next(err);
  }
};

const getInsertMultiple = async (req, res, next) => {
  try {
    let users = [];
    req.body.forEach((user) => {
      let hash = md5(user.password);
      users.push([user.id, user.username, user.email, hash, user.phone_no]);
    });

    let query =
      "INSERT INTO Students(id,username,email,password,phone_no) VALUES ?";
    let result = await db
      .executeQuery(query, [users])
      .catch(function reject(err) {
        next(Error(err.sqlMessage));
        return null;
      });

    if (result !== null) return customResponse(result, res);
  } catch (err) {
    next(err);
  }
};

const getUpdate = async (req, res, next) => {
  try {
    let body = [req.body.new_value];
    let query = `UPDATE Students SET ${req.body.column} = ? WHERE id= ${req.userData.id} `;

    let result = await db.executeQuery(query, body).catch(function reject(err) {
      next(Error(err.sqlMessage));
      return null;
    });

    if (result !== null) return customResponse(result, res);
  } catch (err) {
    next(err);
  }
};

const getDelete = async (req, res, next) => {
  try {
    body = [req.userData.id];
    let query = "DELETE FROM Students WHERE id=?";

    let result = await db.executeQuery(query, body).catch(function reject(err) {
      next(Error(err.sqlMessage));
      return null;
    });

    if (result !== null) return customResponse(result, res);
  } catch (err) {
    next(err);
  }
};

const getSelect = async (req, res, next) => {
  try {
    let body = req.params._id;
    let query = "SELECT * FROM Students WHERE id=?";

    let result = await db.executeQuery(query, body).catch(function reject(err) {
      next(Error(err.sqlMessage));
      return null;
    });

    if (result !== null) {
      result.currentUser = req.userData.username;
      return customResponse(result, res);
    }
  } catch (err) {
    next(err);
  }
};

const getSelectAll = async (req, res, next) => {
  try {
    let body = [];
    let query = "SELECT * FROM Students";
    let result = await db.executeQuery(query, body).catch(function reject(err) {
      next(Error(err.sqlMessage));
      return null;
    });

    if (result !== null) {
      result.currentUser = req.userData.username;
      return customResponse(result, res);
    }
  } catch (err) {
    next(err);
  }
};

const getLogin = async (req, res, next) => {
  try {
    let username = req.body.username;
    let user_pass = req.body.password;

    let query = "SELECT * FROM Students WHERE username = ?";
    let body = [username];

    let result = await db.executeQuery(query, body).catch(function reject(err) {
      next(Error(err.sqlMessage));
      return null;
    });

    if (result !== null) {
      //check if user exists
      if (result.length === 0) {
        next(Error("user does not exist"));
      } else {
        let user = { username: req.body.username, id: result[0].id };
        let token = createToken(user);
        password = result[0].password;
        let hash = md5(user_pass);
        if (password === hash) {
          return customResponse(
            { code: 200, message: "login successful", token: token },
            res
          );
        } else {
          next(Error("login unsuccesfull"));
        }
      }
    }
  } catch (err) {
    next(err);
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
  getInsertMultiple,
};
