import {Component, ElementRef, Input, OnDestroy, OnInit, ViewChild} from '@angular/core';
import {Subscription} from 'rxjs';
import {TrainingNavigationService} from '../../../core/services/training-navigation.service';
import {Lab} from '../../../core/models/course.model';
import {TrainingService} from '../../../core/services/training.service';
import {LabService} from '../../../core/services/lab.service';
import {DomSanitizer, SafeResourceUrl} from '@angular/platform-browser';
import {NgxSpinnerService} from 'ngx-spinner';
import {UserService} from '../../../core/services/user.service';

type CurrentViewType = "None" | "LanguageSelection" | "Lab";

@Component({
  selector: 'app-training-content-lab',
  templateUrl: './training-content-lab.component.html',
  styleUrls: ['./training-content-lab.component.scss']
})
export class TrainingContentLabComponent implements OnInit, OnDestroy {
  private _lab: Lab;
  get lab(): Lab {
    return this._lab;
  }

  @ViewChild("iframe") iframe : ElementRef;

  @Input() set lab(value: Lab) {
    this._lab = value;
    this.initLab();
  }

  public currentView: CurrentViewType;
  public selectedLanguageCode: string;
  private subscriptions: Subscription[] = [];
  public safeLabUrl: SafeResourceUrl;
  public labError: string;

  constructor(private trainingNavigationService: TrainingNavigationService,
              private trainingService: TrainingService,
              private labService: LabService,
              private userService: UserService,
              private spinner: NgxSpinnerService,
              private domSanitizer: DomSanitizer) { }

  ngOnInit(): void {

    this.trainingNavigationService.raiseFullScreenChanged(true);

    this.subscriptions.push(this.trainingNavigationService.nextClicked$.subscribe(() => {
      this.trainingNavigationService.raiseNextContentItem();
    }));

    this.subscriptions.push(this.trainingNavigationService.restartLab$.subscribe(() => {
      this.initLab();
    }));

    this.subscriptions.push(this.trainingNavigationService.fullScreenChanged$.subscribe((isFullScreen) => {
      this.focus_iframe();
    }));

    this.subscriptions.push(this.trainingNavigationService.openWriteUp$.subscribe(() => {
      this.focus_iframe();
    }));

    this.subscriptions.push(this.trainingNavigationService.labHintClicked$.subscribe(() => {
      this.focus_iframe();
    }));
  }

  initLab() {
    if ((!this.lab.images) || this.lab.images.length === 0) {
      this.currentView = "None";
      this.trainingNavigationService.raiseRunningLabChanged(undefined);
    } else if (this.lab.images.length === 1) {
      this.showLab(this.trainingService.getLabImageLanguageCode(this.lab.images[0]));
    } else {
      this.currentView = "LanguageSelection";
      this.trainingNavigationService.raiseRunningLabChanged(undefined);
    }

    this.trainingNavigationService.setNextSlideType("None");
  }

  onLanguageSelected(languageCode: string) {
    this.showLab(languageCode);
  }

  focus_iframe(){
    if (this.iframe) {
      this.iframe.nativeElement.focus();
    }
  }

  showLab(languageCode: string) {
    this.selectedLanguageCode = languageCode;
    this.currentView = "Lab"
    const image = this.lab.images.find(image => image[this.selectedLanguageCode]);
    const imageId = image[this.selectedLanguageCode];
    this.safeLabUrl = undefined;
    this.labError = undefined;
    if (imageId) {
      let userId: string;
      try {
        userId = sessionStorage.getItem("user_id")
      } catch (e) {
        console.log('Could not read current user Id', e);
      }

      this.spinner.show();
      this.subscriptions.push(this.labService.deployLab(imageId, userId)
        .subscribe((deployResult: string) => {
        // console.log("TODO IB deployResult: ", deployResult);

        const resultSplit = deployResult['message'].split("'");
        const urlOrMessage = resultSplit[1];
        setTimeout(() => {
          try {
            new URL(urlOrMessage);
            this.safeLabUrl = this.domSanitizer.bypassSecurityTrustResourceUrl(urlOrMessage);
          } catch (e) {
            this.labError = `${urlOrMessage}. Please Restart Lab to try again.`;
          }
          this.spinner.hide();
        }, 6000);

      }, error => {
          this.spinner.hide();
          console.error('Could not initialise lab', error);
          this.labError = "Could not initialise the Lab. Please Restart Lab to try again.";
        }))
    } else {
      console.error("Lab has no valid address");
    }
    this.trainingNavigationService.raiseRunningLabChanged(this.lab);
  }

  ngOnDestroy(): void {
    this.trainingNavigationService.raiseRunningLabChanged(undefined);
    this.subscriptions.forEach(sub => {
      if (sub) {
        sub.unsubscribe();
      }
    });
  }
}
