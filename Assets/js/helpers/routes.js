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

            case "users":
                switch (method) {
                    case "deleteUserId":
                        return `${router}users/deleteUserId`;

                    default:
                        throw new Error(`El método '${method}' no es válido para la ruta 'users'.`);
                }

            case "converter":
                switch (method) {
                    case "setConverter":
                        return `${router}converter/setConverter`;
                    case "deleteAudioId":
                        return `${router}converter/deleteAudioId`;
                    case "addFavorite":
                        return `${router}converter/addFavorite`;
                    default:
                        throw new Error(`El método '${method}' no es válido para la ruta 'converter'.`);
                }

            case "profile":
                return `${router}users/setProfile`;

            case "roles":
                return `${router}roles/setRoleId`;

            default:
                throw new Error("Debe especificar una ruta válida.");
        }
    }
}

export { Routers };
