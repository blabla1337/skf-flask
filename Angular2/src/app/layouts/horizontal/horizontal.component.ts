import { Component, OnInit, AfterViewInit } from '@angular/core';
import { UserService } from '../../core/services/user.service';


@Component({
  selector: 'app-horizontal',
  templateUrl: './horizontal.component.html',
  styleUrls: ['./horizontal.component.scss']
})

/**
 * Horizontal-layout component
 */
export class HorizontalComponent implements OnInit, AfterViewInit {
  userId: string;

  constructor(private userService: UserService) { }

  ngOnInit() {
    document.body.setAttribute('data-layout', 'horizontal');
    document.body.setAttribute('data-topbar', 'dark');

    this.userService.getJwtUserId();

    const theme_var = localStorage.getItem("theme");
    if (theme_var === undefined || theme_var === "" || theme_var === null ) {
      localStorage.setItem("theme","light-theme.css");
    }
  }

  ngAfterViewInit() {
  }
}
