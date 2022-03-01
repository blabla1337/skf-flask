import {Component, OnDestroy, OnInit} from '@angular/core';
import {ActivatedRoute} from '@angular/router';
import {Subscription} from 'rxjs';

@Component({
  selector: 'app-training-profile',
  templateUrl: './training-profile.component.html',
  styleUrls: ['./training-profile.component.scss']
})
export class TrainingProfileComponent implements OnInit, OnDestroy {
  private profileId: string;
  subscriptions: Subscription[] = [];

  constructor(private activatedRoute: ActivatedRoute) { }

  ngOnInit(): void {
    this.subscriptions.push(this.activatedRoute.params.subscribe(params =>
    {
      this.profileId = params['id'];
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
