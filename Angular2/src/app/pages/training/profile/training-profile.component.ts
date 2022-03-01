import {Component, OnDestroy, OnInit} from '@angular/core';
import {ActivatedRoute, Router} from '@angular/router';
import {Subscription} from 'rxjs';
import {CourseInfo} from '../../../core/models/course.model';
import {TrainingService} from '../../../core/services/training.service';

@Component({
  selector: 'app-training-profile',
  templateUrl: './training-profile.component.html',
  styleUrls: ['./training-profile.component.scss']
})
export class TrainingProfileComponent implements OnInit, OnDestroy {
  private profileId: string;
  public courses: CourseInfo[];
  private subscriptions: Subscription[] = [];

  constructor(private trainingService: TrainingService,
              private activatedRoute: ActivatedRoute,
              private router: Router) { }

  ngOnInit(): void {
    this.subscriptions.push(this.activatedRoute.params.subscribe(params =>
    {
      this.profileId = params['id'];
      this.subscriptions.push(this.trainingService.getCourses(this.profileId).subscribe(courses => {
        this.courses = courses;
      }));
    }));
  }

  onSelectCourse(course: CourseInfo) {
    this.router.navigate(["training", "course", course.id]);
  }

  ngOnDestroy(): void {
    this.subscriptions.forEach(sub => {
      if (sub) {
        sub.unsubscribe();
      }
    });
  }
}
