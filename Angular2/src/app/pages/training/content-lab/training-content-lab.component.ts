import {Component, Input, OnDestroy, OnInit} from '@angular/core';
import {Subscription} from 'rxjs';
import {TrainingNavigationService} from '../../../core/services/training-navigation.service';
import {Lab} from '../../../core/models/course.model';
import {TrainingService} from '../../../core/services/training.service';
import {DomSanitizer, SafeResourceUrl} from '@angular/platform-browser';

type CurrentViewType = "None" | "LanguageSelection" | "Lab";

@Component({
  selector: 'app-training-content-lab',
  templateUrl: './training-content-lab.component.html',
  styleUrls: ['./training-content-lab.component.scss']
})
export class TrainingContentLabComponent implements OnInit, OnDestroy {
  @Input() lab: Lab;
  public currentView: CurrentViewType;
  public selectedLanguageCode: string;
  private subscriptions: Subscription[] = [];
  public safeLabUrl: SafeResourceUrl;

  constructor(private trainingNavigationService: TrainingNavigationService,
              private trainingService: TrainingService,
              private domSanitizer: DomSanitizer) { }

  ngOnInit(): void {
    if ((!this.lab.images) || this.lab.images.length === 0) {
      this.currentView = "None";
    } else if (this.lab.images.length === 1) {
      this.showLab(this.trainingService.getLabImageLanguageCode(this.lab.images[0]));
    } else {
      this.currentView = "LanguageSelection";
    }

    this.trainingNavigationService.setNextSlideType("None");

    this.subscriptions.push(this.trainingNavigationService.nextClicked$.subscribe(() => {
      console.log('TODO IB !!!! nextClicked$ in lab');
      this.trainingNavigationService.raiseNextContentItem();
    }));
  }

  onLanguageSelected(languageCode: string) {
    this.showLab(languageCode);
  }

  showLab(languageCode: string) {
    this.selectedLanguageCode = languageCode;
    this.currentView = "Lab"
    const image = this.lab.images.find(image => image[this.selectedLanguageCode]);
    const labAddress = image[this.selectedLanguageCode];
    if (labAddress) {
      this.subscriptions.push(this.trainingService.getLabUrl(labAddress).subscribe(labUrl => {
        this.safeLabUrl = this.domSanitizer.bypassSecurityTrustResourceUrl(labUrl);
      }))
    } else {
      console.error("Lab has no valid address");
    }
  }

  ngOnDestroy(): void {
    this.subscriptions.forEach(sub => {
      if (sub) {
        sub.unsubscribe();
      }
    });
  }
}
