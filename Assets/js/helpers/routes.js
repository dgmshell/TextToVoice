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
                return `${router}users`;
            case "profile":
                return `${router}users/setProfile`;
            default:
                throw new Error("Debe especificar una ruta válida.");
        }
    }
}

export { Routers };

