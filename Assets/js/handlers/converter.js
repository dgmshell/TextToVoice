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
            showToast('Exito', data.message, { timeout: 3000, type: 'success' });
            if(data.redirect==="yes"){
                setTimeout(function() {
                    window.location.href = router +'audios';
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
export async function deleteAudioId(response) {
    const data = await processResponse(response, 'deleteAudioId');

    switch (data.status) {
        case 'success':

            showToast('Exito', data.message, { timeout: 3000, type: 'success' });
            if(data.redirect==="yes"){
                setTimeout(function() {
                    window.location.href = router +'audios';
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

export async function addFavorite(response) {
    const data = await processResponse(response, 'addFavorite');

    switch (data.status) {
        case 'add':
            showToast('Exito', data.message, { timeout: 3000, type: 'success' });
            if(data.redirect==="yes"){
                setTimeout(function() {
                    window.location.href = router +'audios';
                }, 2000);
            }
            break;
        case 'del':

            showToast('Exito', data.message, { timeout: 3000, type: 'success' });
            if(data.redirect==="yes"){
                setTimeout(function() {
                    window.location.href = router +'audios';
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
