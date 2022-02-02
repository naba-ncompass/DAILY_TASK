const mysql = require('mysql')
const config = require('../Config/config.json')

connectToDB = () => {
    return new Promise(function( resolve,reject){
        let con = mysql.createConnection({
            host: config.DB_HOST,
            user: config.DB_USER,
            password: config.DB_PASS,
            database: config.DB,
            insecureAuth : true
        })
        con.connect(function(err){
            if (err){
                reject(err)
            }
            resolve(con)
        })

    })
}

let executeQuery = async (query,body) => {

    try{
        let con = await connectToDB().catch(function reject(err){
            throw err
        })
    
        return new Promise( function(resolve,reject){
            con.query(query,body,function(err,result){
                if (err){
                   reject(err)
                };
                resolve(result)
                con.destroy()
            })
        })
    }catch(err){
        return new Promise( function(resolve,reject){
            reject(err)
        })
    }

}


module.exports = {
    executeQuery
}