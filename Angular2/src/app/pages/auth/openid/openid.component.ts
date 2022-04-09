import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

import { OAuthService } from 'angular-oauth2-oidc';

@Component({
  selector: 'app-openid',
  templateUrl: './openid.component.html',
  styleUrls: ['./openid.component.scss']
})
export class OpenidComponent implements OnInit
{

  year: number = new Date().getFullYear();

  constructor(
    private _router: Router,
    private oauthService: OAuthService,
    ) { }

  ngOnInit(): void
  {
    this.oauthService.refreshToken();
    window.location.assign("/dashboard");
  }
}
