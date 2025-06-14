function showToast(title, text, options) {
    options = options || {};
    options.title = title;
    options.text = text;

    createToast(options);
}
function createToast(options) {
    var container = document.getElementById('cooltoast-container');
    if (!container) {
        container = document.createElement('div');
        container.id = 'cooltoast-container';
        document.body.appendChild(container);
    }

    var toast = document.createElement('div');
    toast.className = 'cooltoast-toast';

    // Añadir clase de estilo según el tipo de tostada
    if (options.type) {
        toast.classList.add('cooltoast-' + options.type);
    }

    toast.innerHTML = '<h4 class="cooltoast-title">' + options.title + '</h4><p class="cooltoast-text">' + options.text + '</p>';
    container.appendChild(toast);

    if (options.timeout) {
        setTimeout(function () {
            if (container.contains(toast)) {
                toast.classList.add('cooltoast-fadeOut');  // Agrega la clase de la animación de desaparición
                // También puedes agregar un evento de escucha para la animación y luego quitar el elemento
                toast.addEventListener('animationend', function() {
                    if (container.contains(toast)) {
                        container.removeChild(toast);
                    }
                });
            }
        }, options.timeout);
    }


    toast.addEventListener('click', function () {
        if (container.contains(toast)) {
            container.removeChild(toast);
        }
    });
}

// Ejemplo de uso
// showToast('Some title', 'Some text', { timeout: 3000, type: 'success' });
