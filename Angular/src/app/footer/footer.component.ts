import { Component, OnInit } from '@angular/core';


@Component({
  selector: 'app-footer',
  templateUrl: './footer.component.html'
})
export class FooterComponent {
    public isLoggedin : boolean = false;
    
    constructor(){}
 
    ngOnInit(){
      if(sessionStorage.getItem("auth_token")!= null){
        this.isLoggedin = true;
      }
    }
}
