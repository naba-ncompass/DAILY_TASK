const { executeQuery } = require("../Utilities/db");
const { makeResponse } = require("../Utilities/responseMaker");
const { encryptData } = require("../Utilities/encryptor");
const { tokenCreator } = require("./createToken");
const { errorObjectCreator } = require("../Utilities/errorHandler");
const jwt = require('jsonwebtoken');

// Default error code is set to 500 and it is changed whenever needed.
var errorCode = 500;

const readStudentData = async (req, res, next) => {
    try {
        let result = await executeQuery("select * from student").catch(
            function reject(error) {
                throw error;
            }
        );

        let response = makeResponse("query successful!!", result);
        return res.json(response);
    } catch (error) {
        let errorObject = errorObjectCreator(
            "error while reading student data",
            errorCode,
            error
        );
        next(errorObject);
    }
};

const readStudentById = async (req, res, next) => {
    try {
        // extracting data from query parameters
        let data = req.query;
        const inputData = [data.id];
        let query = `select * from student where id = ?`;
        let result = await executeQuery(query, inputData).catch(function reject(error) {
            throw error;
        });

        // checking if object result is empty or not
        if (Object.keys(result).length == 0) {
            errorCode = 404;
            throw new Error("id not found");
        } else {
            return res.json(makeResponse("query successful!!", result));
        }
    } catch (error) {
        let errorObject = errorObjectCreator(
            "error while reading student data by id",
            errorCode,
            error
        );
        next(errorObject);
    }
};

const studentSignup = async (req, res, next) => {
    try {
        let data = req.body;

        // encrypting the user entered password
        let encryptedPassword = encryptData(data.password);

        const inputData = [
            [
                [
                    data.id,
                    data.name,
                    data.department,
                    data.cgpa,
                    data.username,
                    encryptedPassword,
                    data.phone,
                ],
            ],
        ];

        let query = `insert into student(id, name, department, cgpa, username, password, phone) values ?`;
        const token = tokenCreator(data.username);
        let result = await executeQuery(query, inputData).catch(function reject(
            error
        ) {
            throw error;
        });

        return res.json(makeResponse(`Signup successfull your token = ${token}`));
    } catch (error) {
        let errorObject = errorObjectCreator(
            "error while signup",
            errorCode,
            error
        );
        next(errorObject);
    }
};

const updateStudentData = async (req, res, next) => {
    try {
        let data = req.body;
        const inputData = [Object.values(data)[1]];
        let token = req.header("authorization").split(" ")[1];
        let username = getUser(token);
        
        let query = `update student set ${data.column} = ? where username = '${username}'`;

        let result = await executeQuery(query, inputData).catch(function reject(
            error
        ) {
            throw error;
        });

        // checking if any data was affected or not
        if (result.affectedRows == 0) {
            errorCode = 404;
            throw new Error("id not found");
        }
        return res.json(makeResponse(`your updated ${data.column} is ${Object.values(data)[1]}`));
    } catch (error) {
        errorCode = 400;
        let errorObject = errorObjectCreator(
            "error while updating student data",
            errorCode,
            error
        );
        next(errorObject);
    }
};

const deleteStudentData = async (req, res, next) => {
    try {
        let token = req.header("authorization").split(" ")[1];
        let username = getUser(token);
        const inputData = [username];
        query = `delete from student where username = ?`;

        result = await executeQuery(query, inputData).catch(function reject(error) {
            throw error;
        });
        if (result.affectedRows == 0) {
            errorCode = 404;
            throw new Error("user not found");
        }
        return res.json(makeResponse(`records deleted for ${username}`));
    } catch (error) {
        let errorObject = errorObjectCreator(
            "error while deleting student data",
            errorCode,
            error
        );
        next(errorObject);
    }
};

const studentLogin = async (req, res, next) => {
    try {
        let data = req.body;
        let username = data.username;
        const inputData = [data.username];

        // encrypting the user entered password
        encryptedPassword = encryptData(data.password);
        query = `select password from student where username = ?`;

        result = await executeQuery(query, inputData).catch(function reject(error) {
            throw error;
        });

        if (Object.keys(result).length == 0) {
            errorCode = 404;
            throw new Error("username not valid");
        } else {
            if (result[0].password == encryptedPassword) {
                const token = tokenCreator(username);
                return res.json(makeResponse(`login successfull !!! token = ${token}`));
            } else {
                errorCode = 406;
                throw new Error("wrong password !!!");
            }
        }
    } catch (error) {
        let errorObject = errorObjectCreator(
            "error while student login",
            errorCode,
            error
        );
        next(errorObject);
    }
};

const insertStudentData = async (req, res, next) => {
    try {
        let data = req.body;

        const inputData = [];
        const dataArrayCollection = makeDataArray(data);

        inputData.push(dataArrayCollection);
        console.log(inputData);
        let query = `insert into student(id, name, department, cgpa, username, password, phone) values ?`;
        let result = await executeQuery(query, inputData).catch(function reject(
            error
        ) {
            throw error;
        });

        return res.json(makeResponse(result.affectedRows + " rows affected !!!"));
    } catch (error) {
        let errorObject = errorObjectCreator(
            "error while inserting student data",
            errorCode,
            error
        );
        next(errorObject);
    }
};

const makeDataArray = (data) => {
    const dataArrayCollection = [];
    for (let i = 0; i < Object.keys(data).length; i++) {
        //encrypting the user entered password
        tempData = data[i];
        let encryptedPassword = encryptData(tempData.password);

        const dataArray = [
            tempData.id,
            tempData.name,
            tempData.department,
            tempData.cgpa,
            tempData.username,
            encryptedPassword,
            tempData.phone,
        ];
        dataArrayCollection.push(dataArray);
    }
    return dataArrayCollection;
};

const getUser = (token) => {
    var decode = jwt.decode(token);
    return decode.username;
}

const checkUser = async (username) => {
        const inputData = [username];
        let query = `select * from student where username = ?`;
        let result = await executeQuery(query, inputData).catch(function reject(error) {
            throw error;
        });

        // checking if object result is empty or not
        if (Object.keys(result).length == 0) {
            return false;
        } else {
            return true;
        }
}

module.exports = {
    readStudentData,
    readStudentById,
    studentSignup,
    updateStudentData,
    deleteStudentData,
    studentLogin,
    insertStudentData,
    getUser,
    checkUser
}