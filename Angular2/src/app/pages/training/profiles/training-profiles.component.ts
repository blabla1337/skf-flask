import { Component, OnInit } from '@angular/core';
import {Profile} from '../../../core/models/course.model';
import {TrainingService} from '../../../core/services/training.service';

@Component({
  selector: 'app-training-profiles',
  templateUrl: './training-profiles.component.html',
  styleUrls: ['./training-profiles.component.scss']
})
export class TrainingProfilesComponent implements OnInit {
  profiles: Profile[] = []

  constructor(private trainingService: TrainingService) { }

  ngOnInit(): void {
    this.trainingService.getProfilesList().subscribe(profiles => {
      this.profiles = profiles;
    } )

  }

}
