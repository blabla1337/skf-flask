import {Component, OnDestroy, OnInit} from '@angular/core';
import {ActivatedRoute, Router} from '@angular/router';
import {Subscription} from 'rxjs';
import {CourseInfo, Profile} from '../../../core/models/course.model';
import {TrainingService} from '../../../core/services/training.service';
import {NgxSpinnerService} from 'ngx-spinner';

@Component({
  selector: 'app-training-profile',
  templateUrl: './training-profile.component.html',
  styleUrls: ['./training-profile.component.scss']
})
export class TrainingProfileComponent implements OnInit, OnDestroy {
  public profile: Profile;
  private subscriptions: Subscription[] = [];

  constructor(private trainingService: TrainingService,
              private activatedRoute: ActivatedRoute,
              private router: Router,
              private spinner: NgxSpinnerService) {
  }

  ngOnInit(): void {
    this.spinner.show();
    this.subscriptions.push(this.activatedRoute.params.subscribe(params => {
      const profileId = params['id'];
      this.subscriptions.push(this.trainingService.getProfileInfo(profileId).subscribe(profile => {
        this.profile = profile;
        this.spinner.hide();
      }));
    }));
  }

  onSelectCourse(course: CourseInfo) {
    this.router.navigate(['training', 'profile', this.profile.id, 'course', course.id]);
  }

  ngOnDestroy(): void {
    this.subscriptions.forEach(sub => {
      if (sub) {
        sub.unsubscribe();
      }
    });
  }

  goToTraining() {
    this.router.navigate(['training', 'profiles']);
  }
}
