import { Component, OnInit, ViewChild, ElementRef} from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { QuestionsService } from '../services/questions.service';
import { ChecklistService } from '../services/checklist.service';
import { Checklist } from '../models/checklist';
import { Questions } from '../models/questions'


@Component({
  selector: 'app-questionnaire',
  templateUrl: './questionnaire.component.html',
  providers: [QuestionsService, ChecklistService]
})
export class QuestionnaireComponent implements OnInit {
  @ViewChild('sectionNeedToScroll') sectionNeedToScroll: ElementRef

  public questions: Questions[] = [];
  public checklist: Checklist[];
  public correlatedChecklist: Checklist[];
  public delete: string;
  public question_id: number;
  public questionForm: FormGroup;
  public isSubmitted: boolean;
  public isSelected: boolean;
  get formControls() { return this.questionForm.controls; }

  constructor(
    private modalService: NgbModal,
    private questionsService: QuestionsService,
    private checklistService: ChecklistService,
    private router: Router,
    private formBuilder: FormBuilder,
  ) { }

  ngOnInit() {
    this.questionForm = this.formBuilder.group({
      question : ['', Validators.required]
    })

    this.getQuestionList();
    this.getChecklistList();
  };

  getQuestionList() {
    this.questionsService.getQuestions(Number(localStorage.getItem('checklist_type_id'))).subscribe(
      questions => this.questions = questions,
      err => console.log('getting questions failed')
    )
  }
  
  getChecklistList() {
    this.checklistService
      .getChecklistByType(Number(localStorage.getItem('checklist_type_id')))
      .subscribe(
      checklist => {
        this.checklist = checklist;
      },
      () => console.log('Getting the checklist types failed, contact an administrator! '))
  }

  getChecklistListItemsCorrelatedToSelectedQuestion() {
    this.questionsService
      .getChecklistItemsOnquestion_id(Number(localStorage.getItem('question_id')))
      .subscribe(
        correlatedChecklist => {
        this.correlatedChecklist = correlatedChecklist;
      },
      err => console.log('Getting the correlated controls failed, contact an administrator! '))
  }

  selectChecklistItems() {
    this.isSelected = true;
    localStorage.setItem('question_id', this.question_id.toString())
    var patch = this.questions.find(x => x['id'] === Number(this.question_id));
    this.questionForm.patchValue(patch)
    this.getChecklistListItemsCorrelatedToSelectedQuestion()
  }

  storeNewQuestion() {
    this.isSubmitted = true;
    if(this.questionForm.invalid){
      return;
    }
    this.questionsService.newQuestion(Number(localStorage.getItem('checklist_type_id')), this.questionForm.value)
      .subscribe(
        () => this.getQuestionList(),
        () => console.log(('Error whilst adding question'))
      );
  }

  updateQuestion() {
    this.questionsService.updateQuestion(Number(localStorage.getItem('checklist_type_id')), Number(localStorage.getItem('question_id')), this.questionForm.value)
      .subscribe(
        () => {this.getQuestionList()},
        () => console.log('Error whilst updating question')
      );
  }

  correlateQuestionToChecklistITem(checklist_id: string) {
    this.checklistService.updateChecklistItemCorraltion(checklist_id, Number(localStorage.getItem('checklist_type_id')), Number(localStorage.getItem('question_id')))
      .subscribe(
        () => {this.getChecklistListItemsCorrelatedToSelectedQuestion(); this.getChecklistList()},
        () => console.log(('Adding the checklistID to the question did not happen!'))
      );
  }

  removeQuestionFromChecklistITem(checklist_id: string) {
    this.checklistService.updateChecklistItemCorraltion(checklist_id, Number(localStorage.getItem('checklist_type_id')), 0)
      .subscribe(
        () => {this.getChecklistListItemsCorrelatedToSelectedQuestion(); this.getChecklistList()},
        () => console.log(('Adding the checklistID to the question did not happen!'))
      );
  }

  deleteQuestion() {
    if (this.delete == 'DELETE') {
      this.questionsService.deleteQuestion(this.question_id).subscribe(x =>
        // Get the new project list on delete
        this.getQuestionList())
      this.delete = '';
      this.isSelected = false;
    }
  }

  addQuestionModal(add) {
    this.questionForm.patchValue({question:''})
    this.modalService.open(add, { size: 'lg' })
  }

  updateQuestionModal(update) {
    this.modalService.open(update, { size: 'lg' })
  }

  deleteQuestionModal(deletes) {
    this.modalService.open(deletes, { size: 'lg' })
  }

  back() {
    this.router.navigate(['/checklist-manage/', localStorage.getItem('checklist_type_id')]);
  }

  public gotoSection() {
    this.sectionNeedToScroll.nativeElement.scrollIntoView({ behavior: 'smooth', block: 'center' })
}

}
