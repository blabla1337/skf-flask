import { Component, OnDestroy, OnInit } from '@angular/core';
import { Profile } from '../../../core/models/course.model';
import { TrainingService } from '../../../core/services/training.service';
import { Subscription } from 'rxjs';
import { Router } from '@angular/router';
import { NgxSpinnerService } from 'ngx-spinner';

@Component({
  selector: 'app-training-profiles',
  templateUrl: './training-profiles.component.html',
  styleUrls: ['./training-profiles.component.scss'],

export class TrainingProfilesComponent implements OnInit, OnDestroy {
    public profiles: Profile[] = [];
    private subscriptions: Subscription[] = [];

  constructor(
    private trainingService: TrainingService,
    private router: Router,
    private spinner: NgxSpinnerService
  ) {}

  ngOnInit(): void {
    this.spinner.show();
    this.subscriptions.push(
      this.trainingService.getProfiles().subscribe((profiles) => {
        this.profiles = profiles;
        this.spinner.hide();
      })
    );
  }

  onSelectProfile(profile: Profile) {
        this.router.navigate(['training', 'profile', profile.id]);
    }

  ngOnDestroy(): void {
    this.subscriptions.forEach((sub) => {
      if (sub) {
        sub.unsubscribe();
      }
    });
  }

