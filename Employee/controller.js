const executor = require("../Utilities/db");
const config = require("../Config/config");
const errorHandle = require('../Utilities/error_handler')
const responsehandler = require("../Utilities/response_handler");
const md5 = require("md5");
const jwt = require('jsonwebtoken')

const readEmployee = async (req, res,next) => {
    try {
        console.log("READING")
        let result = await executor
            .executeQuery("select * from employee")
            .catch(function reject(error) {
                throw error;
            });
            console.log("------------------------------------------------------------")
            console.log(result)
        //return res.status(200).send(result)    
        return res.status(200).json(responsehandler.makeResponse("query successful!!", result));
    // } catch (error) {
    //     return res.status(404).json(responsehandler.makeErrorResponse("error while reading employee data", error.message));
    }
    catch(err){
        let errorInstance = errorHandle.errorHandle(500,"Internal server error",err)
        next(errorInstance)
    }
};


const readEmployeeid = async (req, res,next) => {
    try {
        let email = req.email;
        // console.log("----------------------------------------")
        // console.log(email);
        const inputData = [email];
        query = `select * from employee where email = ?`;
        result = await executor
            .executeQuery(query, inputData)
            .catch(function reject(error) {
                throw error;
            });
            return res.status(200).send(result)
        }
    catch(err){
        let errorInstance = errorHandle.errorHandle(500,"Internal server error",err)
        next(errorInstance)
    }
};




const signupEmployee = async (req, res) => {
    try {
        let id = req.body.id;
        let first_name = req.body.first_name;
        let last_name = req.body.last_name;
        let email = req.body.email;
        let gender = req.body.gender;
        let phone = req.body.phone;
        let password = req.body.password;
        let passwordDigit = md5(password);
        const inputData = [[[id, first_name, last_name, email, gender, phone, passwordDigit]]];
        query = `insert into employee(id, first_name, last_name, email, gender, phone, password) values ?`;
        result = await executor
            .executeQuery(query, inputData)
            .catch(function reject(error) {
                throw error;
            });
        const tokens = jwt.sign(
            { email },
            config.token,
            {
                expiresIn: "5s",
            }
        );
        // save user token
        return res.status(200).json(responsehandler.makeTokenResponse("signup sucessfull", tokens));

    } catch (error) {
        return res.status(500).json(responsehandler.makeErrorResponse("error while inserting employee data", error.message));
    }
};



const insertEmployee = async (req, res) => {
    try {
        let users =[];
        req.body.forEach((user)=> {
            let passwordDigit = md5(user.password);
            users.push([ user.id, user.first_name, user.last_name, user.email, user.gender, user.phone, passwordDigit ]);
        }); 
        // const inputData = [[[id, first_name, last_name, email, gender, phone, passwordDigit]]];
        query = `insert into employee(id, first_name, last_name, email, gender, phone, password) values ?`;
        result = await executor
            .executeQuery(query, [users])
            .catch(function reject(error) {
                throw error;
            });
        // save user token
        return res.status(200).json(responsehandler.makeResponse(result.affectedRows + " rows affected"));

    } catch (error) {
        return res.status(500).json(responsehandler.makeErrorResponse("error while inserting employee data", error.message));
    }
};




const updateEmployee = async (req, res) => {
    try {
        let col = req.body.col;
        let detail = req.body.detail;
        let email = req.email; 
        const inputData = [detail, email];
        query = `update employee set ${col} = ? where email = ?`;
        result = await executor
            .executeQuery(query, inputData)
            .catch(function reject(error) {
                console.log(query);
                throw error;
            });

        return res.status(200).json(responsehandler.makeResponse(result.affectedRows + " rows affected"));
    } catch (error) {
        return res.status(500).json(responsehandler.makeErrorResponse("error while updating employee data", error.message));
    }
};


const deleteEmployee = async (req, res) => {
    try {
        let email = req.email;
        const inputData = [email];
        query = `delete from employee where email = ?`;

        result = await executor
            .executeQuery(query, inputData)
            .catch(function reject(error) {
                throw error;
            });
        return res.status(200).json(responsehandler.makeResponse(result.affectedRows + " rows affected"));
    } catch (error) {
        return res.status(500).json(responsehandler.makeErrorResponse("error while deleting employee data", error.message));
    }
    // return res.status(200).send(result)
    //     }
    // catch(err){
    //     let errorInstance = errorHandle.errorHandle(500,"Internal server error",err)
    //     next(errorInstance)
    // }
};

// deleteEmployee = async function () {
//     try {
//         let coloumn = prompt("Enter the coloumn to delete: ");
//         let detail = prompt("Enter the delete to delete: ");
//         console.log('hi');
//         const inputData = [coloumn, detail];
//         query = `delete from employee where ? = ?`%$[coloumn],$[detail];
//         result = await executor
//             .executeQuery(query, inputData)
//             .catch(function reject(error) {
//                 throw error;
//             });
//         console.log(query);
//         return responsehandler.makeResponse(result.affectedRows + " rows affected");
//     } catch (error) {
//         return responsehandler.makeErrorResponse("error while deleting employee data", error.message);
//     }
// };


const truncateEmployee = async () => {
    try {
        result = await executor
            .executeQuery("truncate table employee")
            .catch(function reject(error) {
                throw error;
            });
        return res.status(200).json(responsehandler.makeResponse("query successful!!", result));
    } catch (error) {
        return res.status(500).json(responsehandler.makeErrorResponse("error while truncating employee data", error.message));
    }
};


const signinEmployee = async (req, res) => {
    try {
        //console.log(req.body)
        let email = req.body.email;
        let password = req.body.password;
        let passwordDigit = md5(password);
        const inputData = [email];
        if (!(email && password)) {
            res.status(400).json(responsehandler.makeErrorResponse("All input is required SOMETHING IS MISSING", error.message));
        }
        else if (email && passwordDigit) {
            query = `SELECT password from employee WHERE email = ?`;
            console.log(query)
            let result = await executor.executeQuery(query, inputData)
                .catch(function reject(error) {
                    throw error;
                });
            console.log(result)
            if (Object.keys(result).length == 0) {
                errorCode = 404;
                throw new Error("username not valid");
            } else {
                if (passwordDigit == result[0].password) {

                    const tokens = jwt.sign(
                        { email },
                        config.token,
                        {
                            expiresIn: "5m",
                        }
                    );
                    return res.status(200).json(responsehandler.makeTokenResponse("signed in sucessfull", tokens));
                }
                else {
                    throw new Error("password not valid");
                }
            }
        }
        else {
            return res.status(500).json(responsehandler.makeErrorResponse("error while signing in  employee data", error.message));
        }
    } catch (error) {
        return res.status(500).json(responsehandler.makeErrorResponse("error while signing in  employee data", error.message));
    }
};




module.exports = {
    readEmployee,
    insertEmployee,
    signupEmployee,
    updateEmployee,
    deleteEmployee,
    truncateEmployee,
    readEmployeeid,
    signinEmployee
};



// jwt authoerization     compl
//  with expire time      compl
//  compression zlib      -----