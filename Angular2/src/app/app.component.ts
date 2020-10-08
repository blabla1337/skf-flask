import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit {
  ngOnInit() {
    setTimeout(() =>
    {
      localStorage.setItem('session', 'expired');
      sessionStorage.setItem('Authorization', '');
      location.replace('/auth/login');
    }, 7100000);
  }
}
