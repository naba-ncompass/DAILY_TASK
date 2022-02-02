const db_ops = require('./controller-console')
const prompt = require('prompt-sync')({ sigint: true })
const { customResponse } = require('../Utilities/custom-response')

let insertInput = () => {
    let body = [];
    body.push(parseInt(prompt("Enter id :  ")));
    body.push(prompt("Enter name :  "));
    body.push(prompt("Enter email :   "));
    body.push(prompt("Enter password   :   "));
    body.push(prompt("Enter phone no    :   "))

    return body
}

let updateInput = () => {
    let body = [];

    body.push(prompt("Enter the new value     :   "));
    body.push(parseInt(prompt("Enter the id  :   ")));

    return body
}

let deleteInput = () => {
    let body = [];
    body.push(parseInt(prompt("Enter id of the row you want to delete    :   ")));
}

let selectInput = () => {
    let body = [];
    body.push(prompt("Enter id   :   "));

    return body
}

let menu = async () => {
    let k=0

    while (k!=1){

        console.log("\nINSERT - 1\nUPDATE - 2\nDELETE - 3\nSELECT ONE - 4\nSELECT ALL - 5\nEXIT - 6")
        let result 
        let op = parseInt(prompt("ENTER OPTION   :   "))
        switch(op){
            case 1:
                result = await db_ops.getInsert(insertInput())
                console.log(customResponse(result))
                break
            case 2:
                result = await db_ops.getUpdate(updateInput())
                console.log(customResponse(result))
                break
            case 3:
                result = await db_ops.getDelete(deleteInput())
                console.log(customResponse(result))
                break
            case 4:
                result = await db_ops.getSelect(selectInput())
                console.log(customResponse(result))
                break
            case 5:
                result = await db_ops.getSelectAll()
                console.log(customResponse(result))
                break
            case 6:
                k=1
                break
            default:
                console.log("wrong option")
        }
    }

}

module.exports = {
    menu
}