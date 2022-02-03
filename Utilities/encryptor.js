const md5 = require('md5');

const encryptData = (input) => {
    let encryptedInput = md5(input);
    return encryptedInput;
}

module.exports = {
    encryptData
}