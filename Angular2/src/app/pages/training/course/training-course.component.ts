import {Component, OnDestroy, OnInit} from '@angular/core';
import {TrainingService} from '../../../core/services/training.service';
import {ActivatedRoute, Router} from '@angular/router';
import {Subscription} from 'rxjs';
import {Course} from '../../../core/models/course.model';
import {NgxSpinnerService} from 'ngx-spinner';


@Component({
  selector: 'app-training-course',
  templateUrl: './training-course.component.html',
  styleUrls: ['./training-course.component.scss']
})
export class TrainingCourseComponent implements OnInit, OnDestroy {
  public course: Course;
  private subscriptions: Subscription[] = [];

  constructor(private trainingService: TrainingService,
              private activatedRoute: ActivatedRoute,
              private router: Router,
              private spinner: NgxSpinnerService) { }

  ngOnInit(): void {
    this.spinner.show();
    this.subscriptions.push(this.activatedRoute.params.subscribe(params =>
    {
      const courseId = params['id'];
      // TODO IB !!!! send it as param to tree
      this.subscriptions.push(this.trainingService.getCourse(courseId).subscribe(course => {
        this.course = course;
        this.spinner.hide();
      }));
    }));
  }

  ngOnDestroy(): void {
    this.subscriptions.forEach(sub => {
      if(sub) {
        sub.unsubscribe();
      }
    });
  }

  goToTraining() {
    this.router.navigate(["training", "profiles"]);
  }
}
