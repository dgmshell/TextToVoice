class Routers {
    static getUrl(route, method) {
        switch (route) {
            case "auth":
                switch (method) {
                    case "setLogin":
                        return `${router}auth/setLogin`;
                    case "setSignup":
                        return `${router}auth/setSignup`;
                    case "resetPassword":
                        return `${router}auth/resetPassword`;

                    default:
                        throw new Error(`El método '${method}' no es válido para la ruta 'auth'.`);
                }
                break;

            case "users":
<<<<<<< HEAD
                return `${router}users`;
            case "profile":
                return `${router}users/setProfile`;
=======
                switch (method) {
                    case "deleteUserId":
                        return `${router}users/deleteUserId`;

                    default:
                        throw new Error(`El método '${method}' no es válido para la ruta 'auth'.`);
                }
                break;
            case "converter":
                switch (method) {
                    case "setConverter":
                        return `${router}converter/setConverter`;
                        break;
                    case "deleteAudioId":
                        return `${router}converter/deleteAudioId`;
                        break;
                    case "addFavorite":
                        return `${router}converter/addFavorite`;
                        break;
                    default:
                        throw new Error(`El método '${method}' no es válido para la ruta 'auth'.`);
                }
                break;
            case "profile":
                return `${router}users/setProfile`;
            case "roles":
                return `${router}roles/setRoleId`;
>>>>>>> e584ece351510e858fcdb3ce4bcf742b241f31ae
            default:
                throw new Error("Debe especificar una ruta válida.");
        }
    }
}

export { Routers };

