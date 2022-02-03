const express = require("express");
const compression = require("compression");
const { getPostal } = require("./controller");
const { validatorMiddleware } = require("./validator");
const { checkCacheData } = require("../Utilities/caching");

const router = express.Router();

router.use(compression({level:9}));
router.use(express.static("public"));

router.get("/postal",validatorMiddleware, checkCacheData, getPostal);


module.exports = router;