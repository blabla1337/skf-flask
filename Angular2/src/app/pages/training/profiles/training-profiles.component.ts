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
  profiles: Profile[] = []
  apiSubscriptions: Subscription[] = []
  constructor(private trainingService: TrainingService,
              private trainingPersistenceService: TrainingPersistenceService,
              private router: Router) { }

  ngOnInit(): void {
    this.apiSubscriptions.push(this.trainingService.getProfiles().subscribe(profiles => {
      this.profiles = profiles;
    }));
  }

  onSelectProfile(profile: Profile) {
    this.trainingPersistenceService.setSelectedProfile(profile);
    // TODO IB !!!! the profileId should be in URL
    this.router.navigateByUrl("/training/learning");
  }

  ngOnDestroy(): void {
    this.apiSubscriptions.forEach(sub => {
      if (sub) {
        sub.unsubscribe();
      }
    });
  }
}
