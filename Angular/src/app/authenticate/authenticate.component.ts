import { Component, OnInit, DoCheck } from "@angular/core";
import { FormBuilder, FormGroup, Validators } from "@angular/forms";
import { AuthenticateService } from "../services/authenticate.service";
import { OidcClientNotification, OidcSecurityService, PublicConfiguration } from 'angular-auth-oidc-client';
import { Observable } from 'rxjs';
import { environment } from '../../environments/environment';

@Component({
  selector: "app-authenticate",
  templateUrl: "./authenticate.component.html",
  providers: [AuthenticateService]
})
export class AuthenticateComponent implements OnInit
{
  configuration: PublicConfiguration;
  userDataChanged$: Observable<OidcClientNotification<any>>;
  userData$: Observable<any>;
  isAuthenticated$: Observable<boolean>;

  public error: string[] = [];
  public expired = false;
  public error
  loginForm: FormGroup;
  public loginMethod = environment.AUTH_METHOD;

  get formControls()
  {
    return this.loginForm.controls;
  }

  constructor(
    public _authenticateService: AuthenticateService,
    private formBuilder: FormBuilder,
    public oidcSecurityService: OidcSecurityService
  ) { }

  ngDoCheck()
  {
    if (sessionStorage.getItem('auth_token')) {
      location.replace("dashboard");
    }
  }

  ngOnInit()
  {

    if (this.loginMethod == "skipprovider") {
      this.skipLogin();
    }

    this.configuration = this.oidcSecurityService.configuration;
    this.userData$ = this.oidcSecurityService.userData$;
    this.isAuthenticated$ = this.oidcSecurityService.isAuthenticated$;

    if (localStorage.getItem("session") == "expired") {
      this.expired = true;
    }
    localStorage.clear();
    this.loginForm = this.formBuilder.group({
      username: ["", Validators.required],
      password: ["", Validators.required]
    });
  }

  onLogin()
  {
    this.error = [];
    this._authenticateService.authenticate(this.loginForm.value).subscribe(
      response =>
      {
        if (response["Authorization token"]) {
          sessionStorage.setItem("auth_token", response["Authorization token"]);
          sessionStorage.setItem("user", response["username"]);
          location.replace("dashboard");
        }
      },
      () => this.error.push("Wrong username/password combination!")
    );
  }

  skipLogin()
  {
    sessionStorage.setItem("skip_login", "true");
    location.replace("dashboard");
  }

  openIDLogin()
  {
    this.oidcSecurityService.authorize();
  }

  openIDLogout()
  {
    this.oidcSecurityService.logoff();
  }
}
