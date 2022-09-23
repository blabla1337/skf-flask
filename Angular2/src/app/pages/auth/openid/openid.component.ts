import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

import { OAuthService } from 'angular-oauth2-oidc';
import { timer } from 'rxjs';

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

  async ngOnInit(): Promise<void>
  {
    this.oauthService.getAccessToken();
    timer(2000).subscribe(x => { this._router.navigate(['/dashboard']); })
  }
}


