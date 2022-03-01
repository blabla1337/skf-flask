import {Component, OnDestroy, OnInit} from '@angular/core';
import {Profile} from '../../../core/models/course.model';
import {TrainingService} from '../../../core/services/training.service';
import {Subscription} from 'rxjs';
import {TrainingPersistenceService} from '../../../core/services/training.persistence.service';
import {Router} from '@angular/router';

@Component({
  selector: 'app-training-profiles',
  templateUrl: './training-profiles.component.html',
  styleUrls: ['./training-profiles.component.scss']
})
export class TrainingProfilesComponent implements OnInit, OnDestroy {
  profiles: Profile[] = [];
  subscriptions: Subscription[] = [];
  constructor(private trainingService: TrainingService,
              private trainingPersistenceService: TrainingPersistenceService,
              private router: Router) { }

  ngOnInit(): void {
    this.subscriptions.push(this.trainingService.getProfiles().subscribe(profiles => {
      this.profiles = profiles;
    }));
  }

  onSelectProfile(profile: Profile) {
    this.router.navigate(["training", "profile", profile.id]);
  }

  ngOnDestroy(): void {
    this.subscriptions.forEach(sub => {
      if (sub) {
        sub.unsubscribe();
      }
    });
  }
}
