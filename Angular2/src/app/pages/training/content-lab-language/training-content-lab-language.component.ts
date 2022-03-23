import {Component, EventEmitter, Input, OnInit, Output} from '@angular/core';
import {Lab, LanguageInfo} from '../../../core/models/course.model';
import {TrainingService} from '../../../core/services/training.service';

@Component({
  selector: 'app-training-content-lab-language',
  templateUrl: './training-content-lab-language.component.html',
  styleUrls: ['./training-content-lab-language.component.scss']
})
export class TrainingContentLabLanguageComponent implements OnInit {
  @Input() lab: Lab;
  @Output() languageSelected = new EventEmitter<string>();
  public languages: LanguageInfo[] = [];

  constructor(private trainingService: TrainingService) { }

  ngOnInit(): void {
    this.languages = this.trainingService.getLanguages()
      .filter(language => this.lab.images.find(image => image[language.code] !== undefined));
  }

  onLanguageSelected(languageCode: string) {
    this.languageSelected.emit(languageCode);
  }
}
