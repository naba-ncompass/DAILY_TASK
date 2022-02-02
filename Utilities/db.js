const mysql = require('mysql')
const config = require('../Config/config.json')


const openConnection = (dbIndex) =>{
    const con = mysql.createConnection({  
        host:config.db_config.host,
        user:config.db_config.user,
        password:config.db_config.password,
        database:config.db_config.database[dbIndex]
    })
    return new Promise((resolve,reject) => {
        con.connect((err)=>{
            if(err) reject(err)
            resolve(con)
        })
    })
}

// execute the sql query
const executeQuery = (con,sqlQuery,value=[]) =>{
    return new Promise((resolve,reject)=>{
        con.query(sqlQuery,value,(err,result)=>{
            if(err) reject(err)
            resolve(result)
            con.destroy()
        })
    })
}

// fetch results after sql query
const fetchResults = async(sqlQuery,value,dbIndex=0) =>{
    let result
    try{
        con = await openConnection(dbIndex)
        result = await executeQuery(con,sqlQuery,value)
        return result
    }catch(err){
        throw err
    }
}


module.exports = {
    fetchResults
}