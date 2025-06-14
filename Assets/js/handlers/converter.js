async function processResponse(response, handlerName) {
    try {
        return await response;
    } catch (error) {
        console.error(`Error processing ${handlerName}:`, error.message);
        throw error;
    }
}

export async function setConverter(response) {
    const data = await processResponse(response, 'setConverter');
    console.log(data.status)
    switch (data.status) {
        case 'success':
            document.getElementById("audioId").value=data.audioId
            document.getElementById("saveAudio").disabled =false
            document.getElementById("converterAudio").disabled =true
            showToast('Exito', data.message, { timeout: 10000, type: 'success' });
            if(data.status==="yes"){
                setTimeout(function() {
                    window.location.href = router +'dashboard';
                }, 5000);
            }
            break;
        case 'successSave':
            showToast('Exito', data.message, { timeout: 10000, type: 'success' });
            break;
        case 'error':
            showToast('Error', data.message, { timeout: 10000, type: 'error' });
            break;

        default:
            showToast('Error', data.message, { timeout: 10000, type: 'error' });
            break;
    }
}
