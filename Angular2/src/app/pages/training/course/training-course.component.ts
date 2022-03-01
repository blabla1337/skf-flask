import {Component, OnDestroy, OnInit} from '@angular/core';
import {TrainingService} from '../../../core/services/training.service';
import {ActivatedRoute, Router} from '@angular/router';
import {Subscription} from 'rxjs';
import {CourseInfo} from '../../../core/models/course.model';


@Component({
  selector: 'app-training-course',
  templateUrl: './training-course.component.html',
  styleUrls: ['./training-course.component.scss']
})
export class TrainingCourseComponent implements OnInit, OnDestroy {
  public course: CourseInfo;
  private subscriptions: Subscription[] = [];

  constructor(private trainingService: TrainingService,
              private activatedRoute: ActivatedRoute,
              private router: Router) { }

  ngOnInit(): void {
    this.subscriptions.push(this.activatedRoute.params.subscribe(params =>
    {
      const courseId = params['id'];
      this.subscriptions.push(this.trainingService.getCourseInfo(courseId).subscribe(course => {
        this.course = course;
      }));
    }));
  }

  ngOnDestroy(): void {
    this.subscriptions.forEach(sub => {
      if (sub) {
        sub.unsubscribe();
      }
    });
  }
}
