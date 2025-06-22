async function processResponse(response, handlerName) {
    try {
        return await response;
    } catch (error) {
        console.error(`Error processing ${handlerName}:`, error.message);
        throw error;
    }
}

export async function setLogin(response) {
    const data = await processResponse(response, 'Login');
    console.log(data.status)
    switch (data.status) {
        case 'login':

            showToast('Exito', data.message, { timeout: 10000, type: 'success' });
            if(data.redirect==="yes"){
                setTimeout(function() {
                    window.location.href = router +'dashboard';
                }, 2000);
            }
            break;

        case 'error':
            showToast('Error', data.message, { timeout: 10000, type: 'error' });
            break;

        default:
            showToast('Error', data.message, { timeout: 10000, type: 'error' });
            break;
    }
}
export async function setSignup(response) {
    const data = await processResponse(response, 'Signup');
    switch (data.status) {
        case 'signup':
            showToast('Exito', data.message, { timeout: 10000, type: 'success' });
            if(data.redirect==="yes"){
                setTimeout(function() {
                    window.location.href = router +'auth/login';
                }, 2000);
            }
            break;

        case 'error':
            showToast('Error', data.message, { timeout: 10000, type: 'error' });
            break;

        default:
            showToast('Error', data.message, { timeout: 10000, type: 'error' });
            break;
    }
}