exports.makeResponse = (message, data) => {
    let response = new Object();
    response = {
        success: true,
        data: data,
        message: message,
    };
    return response;
};

exports.makeErrorResponse = (message, error) => {
    let response = new Object();
    response = {
        success: false,
        message: message,
        error: error,
    };
    return response;
};
