
export class AppSettings {
   public static AUTH_TOKEN = sessionStorage.getItem("auth_token");
   public static USER = sessionStorage.getItem("user");
}

sessionStorage.clear()