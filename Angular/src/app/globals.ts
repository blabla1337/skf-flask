
export class AppSettings {
   public static API_ENDPOINT='http://127.0.0.1:8888/api';
   public static AUTH_TOKEN = sessionStorage.getItem("auth_token");
}

sessionStorage.clear()