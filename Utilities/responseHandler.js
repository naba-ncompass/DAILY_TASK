const createResponse = (result=[],message=[],jwtToken=[],success=true) =>{
    let response = new Object();
    if(result.length!==0) response.data = result;
    if(message.length!==0)response.message = message;
    response.success = success;
    if(jwtToken.length!==0) response.token = jwtToken
    return response
}

module.exports = {
    createResponse
}