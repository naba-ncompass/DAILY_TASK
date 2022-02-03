const mysql = require('mysql');
const config = require('../Config/config');
const responsehandler = require("../Utilities/response_handler");

async function connection() {
    return new Promise(function (resolve, reject) {
        var con = mysql.createConnection({
            host: config['host'],
            user: config['user'],
            password: config['password'],
            database: config['database'],
            token: config['token']
        });
        con.connect(function (err) {
            if (err)
            {
                 reject(err);
            }
            resolve(con);
        });
    });
}


const executeQuery = async function (query, inputData = []) {
    try {
        let con = await connection().catch(function reject(error) {
            // 503
            throw error;
            //return res.status(503).json(responsehandler.makeResponse("authentication failed"));

        });
        return new Promise(function (resolve, reject) {
            con.query(query, inputData, function (err, result) {
                if (err) reject(err);
                resolve(result);
            });
            con.end(error => error ? reject(error) : resolve());
        });
    } catch (error) {
        return responsehandler.makeErrorResponse("AUTHENTICATION FAILED ");
        // return reject.status(404).json(responsehandler.makeErrorResponse("AUTHENTICATION FAILED", error.message));
    } finally {
        console.log('HAVE A NICE DAY ')
    }
}


module.exports = {
    executeQuery
};



// mysqlconnection.connect(function(err) {
//   if (err) throw err;
//   console.log("Connected!");
//   var sql = "INSERT INTO employee (id, first_name,last_name,email,gender,phone,password) VALUES (3,'meghna','lal','meghna@gmail.com','F','0369368367','meghna20013')";
//   mysqlconnection.query(sql, function (err, result) {
//     if (err) throw err;
//     console.log("1 record inserted");
//   });
// });

// get_all = ()=> {
//   let conn = connectTODB()
//   let query= ("SELECT * FROM employee")
//   conn.query(query,function(err, result){
//       if(err) throw err;
//       console.log(result)
//       conn.end()
//     })
// }

// insert = (body) => {
//   let conn = connectTODB()
//   let query= 'INSERT INTO employee VALUES(?,?,?,?,?,?,?)'
//   conn.query(query,[body.id,body.first_name,body.last_name,body.email,body.gender,body.phone,body.password],function(err, result){
//     if(err) throw err;
//     console.log(result)
//     // conn.end()
//   })
// }

// update = (body) => {
//   let conn = connectTODB()
//   let query= 'UPDATE employee SET first_name = ?  WHERE id = ?;'
//   conn.query(query,[body.first_name,body.id],function(err, result){
//     if(err) throw err;
//     console.log(result)
//     // conn.end()
//   })
// }

// deleteDB_id =(body) => {
//   let conn = connectTODB()
//   let query= ('DELETE FROM employee WHERE ? = ?')
//   conn.query(query,[body.coloumn,body.id],function(err, result){
//     if(err) throw err;
//     console.log(result)
//     // conn.end()
//   })
// }

// truncateDB = ()=> {
//   let conn = connectTODB()
//   let query= ("TRUNCATE TABLE employee;")
//   conn.query(query,function(err, result){
//       if(err) throw err;
//       console.log(result)
//       // conn.end()
//     })
// }

// closeDB =()=> {
//   let conn = connectTODB()
//   console.log("CONNECTION IS ESTABLISED BUT YOU CHOICE TO EXIT")
//   conn.end()
// }


// module.exports = {
//   insert,
//   update,
//   deleteDB_id,
//   get_all,
//   truncateDB,
//   closeDB
//  };