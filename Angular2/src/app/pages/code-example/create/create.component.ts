import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-create',
  templateUrl: './create.component.html',
  styleUrls: ['./create.component.scss']
})
export class CodeCreateComponent implements OnInit {

   // bread crumb items
   breadCrumbItems: Array<{}>;

   constructor() { }
 
   ngOnInit(): void {
     this.breadCrumbItems = [{ label: 'Code Examples' }, { label: 'Create', active: true }];
   }

}
