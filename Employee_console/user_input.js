const controller = require('../Employee/controller');
const prompt = require('prompt-sync')();
userOptions = async function () {
    var f = 1;
    while (f === 1) {
        console.log('\n C.for insert \n R.for read \n U.for update \n D.for delete \n T.for Truncate \n RID.for Readid \n X.to exit \n ')
        let choice = prompt('YOUR CHOICE:')
        switch (choice) {
            case 'R':
                result = await controller.readEmployee();
                console.log(result);
                break;
            case 'C':
                result = await controller.insertEmployee();
                console.log(result);
                break;
            case 'U':
                result = await controller.updateEmployee();
                console.log(result);
                break;
            case 'D':
                result = await controller.deleteEmployee();
                console.log(result);
                break;
            case 'T':
                result = await controller.truncateEmployee();
                console.log(result);
                break;
            case 'RID':
                result = await controller.readEmployeeid();
                console.log(result);
                break;
            case 'X':
                f = 0;
                console.log('TERMINATING CRUD OPERATION..');
                break;
            default:
                console.log('                    wrong choice');
                break;
        }
    }
}
module.exports = {
    userOptions
};




// // const fs = importDir({directoryPath:'./Utilities/db'});
// // console.info(fs);
// function naba(){
//     console.log('Available Options:\n C=INSERT \nI=INSERT \n R=Read \n U=Update \n D=Delete \n T= TRUNCATE \n X= CLOSE ');
//     const choice = prompt('Choose your option = ')
//     // conn = db.connect()
//     try{
//         if (choice == 'C'){
//             let id = prompt('Enter id of Student: ')
//             let first_name = prompt('Enter FRIST name of Student: ')
//             let last_name = prompt('Enter LASTname of Student: ')
//             let email = prompt('ENTER email id:')
//             let gender = prompt('ENTER gender: ')
//             let phone = prompt('Enter Phone Number: ')
//             let password = prompt('Enter Password Number: ')
//             let body = {
//                 id: id,
//                 first_name: first_name,
//                 last_name: last_name,
//                 email: email,
//                 gender: gender,
//                 phone: phone,
//                 password: password
//                 }
//                 db.insert(body)
//             }

//         else if (choice == 'R'){
//             const result = db.get_all();
//             }
//         else if (choice == 'U'){
//             console.log("ITS JUST FOR UPDATEING FOR PARTICULAR ID's NAME")
//             let id = prompt("WHICH ID YOU WANT TO UPDATE: ")
//             let first_name = prompt("WHAT NAME WOULD YOU LIKE TO UPDATE: ")
//             let body = {
//                 id: id,
//                 first_name: first_name,
//                 }
//                 db.update(body)
//             }
//         else if (choice == 'D'){
//             let coloumn = prompt("WHICH COLOUMN YOU WANT TO DELETE: ")
//             let id = prompt("YOU WANT TO DELETE which : ")
//             let body = {
//                 coloumn : coloumn,
//                 id: id
//                 }
//             db.deleteDB_id(body);
//             }
//         else if (choice == 'T'){
//             const result = db.truncateDB();
//             }
//         else if (choice == 'X'){
//             const result = db.closeDB();
//             }
//         else {
//             console.log('Wrong choice, You are going exist.');
//             }
//     }catch (error){
//         console.log("YOU ARE WRONG", error);

//     }
// }

// module.exports = {
//     naba
// }

// // naba();
