import { Component, OnInit } from '@angular/core';
import { OAuthService } from 'angular-oauth2-oidc';
import { authConfig } from './auth.config';
import { environment } from '../environments/environment';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit {

  public loginProvider = environment.AUTH_METHOD;

  constructor(private oauthService: OAuthService) {
    if(this.loginProvider != "skiploginprovider"){
      this.configure();
    }
  }

  private configure() {
    this.oauthService.configure(authConfig);
    this.oauthService.loadDiscoveryDocumentAndTryLogin();
    this.oauthService.setupAutomaticSilentRefresh();
  }

  ngOnInit() {
    setTimeout(() =>
    {
      if(this.loginProvider != "skiploginprovider"){
        //localStorage.setItem('session', 'expired');
        //localStorage.clear();
        //location.replace('/auth/login');
        //this.oauthService.logOut(); 
      }
    }, 2000);
  }
}
