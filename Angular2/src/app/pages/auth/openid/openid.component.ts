import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-openid',
  templateUrl: './openid.component.html',
  styleUrls: ['./openid.component.scss']
})
export class OpenidComponent implements OnInit
{

  year: number = new Date().getFullYear();

  constructor(private router: Router) { }

  ngOnInit(): void
  {
  }

  onRegister()
  {
    this.router.navigate(['/auth/register']);
  }

}
