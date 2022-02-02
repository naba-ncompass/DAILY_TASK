const studentRouter = require("express").Router();

const {
  getInsert,
  getUpdate,
  getDelete,
  getSelect,
  getSelectAll,
  getLogin,
  getInsertMultiple
} = require("./controller");

const {
  validateInsert,
  validateUpdate,
  validateDelete,
  validateLogin,
  validateMultipleInsert
} = require("./validate");

const { auth } = require("../Utilities/authorization");

studentRouter.get("/all", auth, getSelectAll);
studentRouter.get("/one/:_id", auth, getSelect);
studentRouter.post("/signup", validateInsert, getInsert);
studentRouter.put("/update", auth, validateUpdate, getUpdate);
studentRouter.delete("/delete", auth, validateDelete, getDelete);
studentRouter.post("/login", validateLogin, getLogin);
studentRouter.post("/add-multiple",validateMultipleInsert,getInsertMultiple)

module.exports = studentRouter;
