const express = require("express");
const compression = require("compression");
const {validatorMiddleware} = require("../Student/validator")
const { validateToken } = require("./tokenValidation");
const {
    readStudentData,
    readStudentById,
    studentSignup,
    updateStudentData,
    deleteStudentData,
    studentLogin,
    insertStudentData
} = require("./controller");
const bodyParser = require("body-parser");


const router = express.Router();

router.use(compression({level:9}));
router.use(bodyParser.json());
router.use(express.static("public"));



router.get("/", validateToken, validatorMiddleware, readStudentData);

router.get("/readById", validateToken, validatorMiddleware, readStudentById);

router.post("/signup", validatorMiddleware, studentSignup);

router.post("/insert", validateToken, validatorMiddleware, insertStudentData);

router.put("/update", validateToken, validatorMiddleware, updateStudentData);

router.delete("/delete", validateToken, validatorMiddleware, deleteStudentData);

router.post("/login", validatorMiddleware, studentLogin);

module.exports = router;