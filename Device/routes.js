const express = require("express");
const compression = require("compression");
const { readDeviceData, peakConsumption, sumConsumption, duplicateData } = require("./controller");
const { validatorMiddleware } = require("./validator");

const router = express.Router();

router.use(compression({level:9}));
router.use(express.static("public"));



router.get("/deviceRead",validatorMiddleware, readDeviceData);

router.get("/peak",validatorMiddleware, peakConsumption);

router.get("/sum",validatorMiddleware, sumConsumption);

router.get("/duplicate",validatorMiddleware, duplicateData);


module.exports = router;