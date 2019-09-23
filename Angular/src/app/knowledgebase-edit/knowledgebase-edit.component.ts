import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { ChecklistService } from '../services/checklist.service'
import { KnowledgebaseService } from '../services/knowledgebase.service'
import { QuestionsService } from '../services/questions.service'
import { FormBuilder, FormGroup, Validators } from  '@angular/forms';
import { Knowledgebase } from '../models/knowledgebase';
import { Observable } from 'rxjs';
import { tap } from 'rxjs/operators';


@Component({
  selector: 'app-knowledgebase-edit',
  templateUrl: './knowledgebase-edit.component.html',
  providers: [ChecklistService, QuestionsService]
})
export class KnowledgebaseEditComponent implements OnInit {

  constructor(private knowledgeService: KnowledgebaseService,private route: ActivatedRoute,private router: Router ,private formBuilder: FormBuilder) { }

  knowledgebaseForm: FormGroup;
  public title: string;
  public canEdit: string;
  public IdFromUrl: number;
  public isSubmitted: boolean;
  knowledgebaseItem: Observable<Knowledgebase>;
  knowledgebaseItemArray: Knowledgebase[];

  get formControls() { return this.knowledgebaseForm.controls; }

  ngOnInit() {
    this.knowledgebaseForm = this.formBuilder.group({
      title: ['', Validators.required],
      content: ['', Validators.required],
    })

    this.route.params.subscribe(params => {
      this.IdFromUrl = params['id'];
    });

    this.knowledgebaseItem = this.knowledgeService.getKnowledgebaseItem(this.IdFromUrl).pipe(
      tap(knowledgebaseItem => this.knowledgebaseForm.patchValue(knowledgebaseItem))
    );
  }

  updateKnowledgebaseItem() {
    this.isSubmitted = true;
    if(this.knowledgebaseForm.invalid){
      return;
    }
    this.knowledgeService.updateKnowledgebaseItem(Number(this.IdFromUrl), this.knowledgebaseForm.value)
      .subscribe(
        () => console.log('updating knowledebase item'),
        () => console.log('error updating knowledebase item')
      );

      this.knowledgeService.getKnowledgeBase().subscribe(requestData => this.knowledgebaseItemArray = requestData,
        () => console.log('Error getting knowledge items, contact the administrator!')
      );
    
      this.router.navigate(['/knowledgebase']);
  }

  back() {
    this.router.navigate(['/knowledgebase']);
  }
}
