import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-training-course-buttons',
  templateUrl: './training-course-buttons.component.html',
  styleUrls: ['./training-course-buttons.component.scss']
})
export class TrainingCourseButtonsComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
  }

  onNext() {
    console.log("Next");
  }
}
