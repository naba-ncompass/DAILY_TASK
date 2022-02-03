const makeResponse = (message, data = []) => {
    let response = new Object();
    response = {
        success: true,
        data: data,
        message: message,
    };
    return response;
};

const makeTokenResponse = (message, data = [], tokens) => {
    let response = new Object();
    response = {
        success: true,
        data: data,
        message: message,
        token: tokens,
    };
    return response;
};


const makeErrorResponse = (message, error) => {
    let response = new Object();
    response = {
        success: false,
        message: message,
        error: error
    }
    return response
}

module.exports = {
    makeErrorResponse,
    makeResponse,
    makeTokenResponse
};