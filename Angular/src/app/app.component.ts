import { Component, OnInit } from '@angular/core';
import { HeaderComponent } from './header/header.component';
import { FooterComponent } from './footer/footer.component';
import { KnowledgebaseService } from './services/knowledgebase.service'
import { OidcSecurityService } from 'angular-auth-oidc-client';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  providers: [HeaderComponent, FooterComponent, KnowledgebaseService],
})

export class AppComponent implements OnInit
{
  constructor(public oidcSecurityService: OidcSecurityService) { }

  ngOnInit()
  {

    this.oidcSecurityService.checkAuth().subscribe(isAuthenticated =>
    {
      if (isAuthenticated == true) {
        sessionStorage.setItem("auth_token", "Bearer " + this.oidcSecurityService.getIdToken());
        //location.replace("dashboard");
        this.oidcSecurityService.userData$.subscribe(resp => sessionStorage.setItem("user", resp['preferred_username']))
      }
    });
    setTimeout(() =>
    {
      localStorage.setItem('session', 'expired');
      location.replace('login');
    }, 6600000);
    // 6600000 == total time API gives
  }
}
