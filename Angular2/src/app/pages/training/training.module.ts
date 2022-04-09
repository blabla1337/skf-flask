import {NgModule} from '@angular/core';
import {CommonModule} from '@angular/common';
import {TrainingRoutingModule} from './training-routing.module';
import {TrainingProfilesComponent} from './profiles/training-profiles.component';
import {TrainingCourseComponent} from './course/training-course.component';
import {TrainingProfileComponent} from './profile/training-profile.component';
import {TrainingCourseTreeComponent} from './course-tree/training-course-tree.component';
import {TrainingCourseContentComponent} from './course-content/training-course-content.component';
import {TreeModule} from '@circlon/angular-tree-component';
import {NgxSpinnerModule} from 'ngx-spinner';
import {MarkdownModule} from 'ngx-markdown';
import {TrainingContentMarkdownComponent} from './content-markdown/training-content-markdown.component';
import {TrainingContentVideoComponent} from './content-video/training-content-video.component';
import { TrainingCourseButtonsComponent } from './course-buttons/training-course-buttons.component';
import { TrainingContentLabComponent } from './content-lab/training-content-lab.component';
import { TrainingContentLabLanguageComponent } from './content-lab-language/training-content-lab-language.component';
import {NgbPopoverModule} from '@ng-bootstrap/ng-bootstrap';
import { TrainingContentEmptyComponent } from './content-empty/training-content-empty.component';


@NgModule({
  declarations: [
    TrainingProfilesComponent,
    TrainingCourseComponent,
    TrainingProfileComponent,
    TrainingCourseTreeComponent,
    TrainingCourseContentComponent,
    TrainingContentMarkdownComponent,
    TrainingContentVideoComponent,
    TrainingCourseButtonsComponent,
    TrainingContentLabComponent,
    TrainingContentLabLanguageComponent,
    TrainingContentEmptyComponent
  ],
  imports: [
    CommonModule,
    TrainingRoutingModule,
    TreeModule,
    NgxSpinnerModule,
    MarkdownModule.forRoot(),
    NgbPopoverModule
  ]
})
export class TrainingModule {
}
