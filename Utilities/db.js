const mysql = require("mysql");
const config = require("../Config/config");

const connection = async () => {
    return new Promise(function (resolve, reject) {
        var con = mysql.createConnection({
            host: config["host_for_db"],
            user: config["user"],
            password: config["password"],
            database: config["database"],
        });
        con.connect(function (err) {
            if (err) reject(err);
            resolve(con);
        });
    });
};

exports.executeQuery = async (query, inputData = []) => {
        let con = await connection().catch(function reject(error,code) {
            errorCode = code;
            throw error;
        });
        return new Promise(function (resolve, reject) {
            con.query(query, inputData, function (err, result) {
                if (err) reject(err);
                resolve(result);
                con.destroy();
            });
        });
};
