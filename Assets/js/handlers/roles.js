async function processResponse(response, handlerName) {
    try {
        return await response;
    } catch (error) {
        console.error(`Error processing ${handlerName}:`, error.message);
        throw error;
    }
}

export async function setRoleId(response) {
    const data = await processResponse(response, 'RoleId');
    console.log(data.status)
    switch (data.status) {
        case 'update':

            showToast('Exito', data.message, { timeout: 10000, type: 'success' });
            if(data.redirect==="yes"){
                setTimeout(function() {
                    window.location.href = router +'users';
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
