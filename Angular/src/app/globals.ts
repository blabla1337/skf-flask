
export class AppSettings {
   public static AUTH_TOKEN = sessionStorage.getItem("auth_token");
}

sessionStorage.clear()