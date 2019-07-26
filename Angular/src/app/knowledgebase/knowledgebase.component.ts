import { Component, OnInit } from '@angular/core';
import { KnowledgebaseService } from '../services/knowledgebase.service'
import { FormBuilder, FormGroup, Validators } from  '@angular/forms';
import { Knowledgebase } from '../models/knowledgebase';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';

@Component({
  selector: 'app-knowledgebase',
  templateUrl: './knowledgebase.component.html',
  providers: [KnowledgebaseService]
})

export class KnowledgebaseComponent implements OnInit {
  knowledgebaseForm: FormGroup;
  public isSubmitted: boolean;
  public delete: string;
  public knowledgeitems: Knowledgebase[] = [];
  public queryString: string;

  get formControls() { return this.knowledgebaseForm.controls; }

  constructor(public _knowledgeService: KnowledgebaseService, private modalService: NgbModal, private formBuilder: FormBuilder) { }

  ngOnInit() {
    this.knowledgebaseForm = this.formBuilder.group({
      title: ['', Validators.required],
      content: ['', Validators.required]
    })
    this.getKnowledgeItems();
  }

  storeKnowledgebaseItem() {
    this.isSubmitted = true;
    if(this.knowledgebaseForm.invalid){
      return;
    }
    this._knowledgeService.newKnowledgebaseItem(this.knowledgebaseForm.value)
      .subscribe(
        () => console.log('Eror storing a new knowledgebase item!')
      );
    this.getKnowledgeItems();
  }

  deleteKnowledgebaseItem(id: number) {
    if (this.delete == 'DELETE') {
      this._knowledgeService.deleteKnowledgebaseItem(id).subscribe(x =>
        this.getKnowledgeItems())
    }
  }

  getKnowledgeItems() {
    this._knowledgeService.getKnowledgeBase().subscribe(requestData => this.knowledgeitems = requestData,
      () => console.log('Error getting knowledge items, contact the administrator!')
    );
  }

  deleteKbModal(content) {
    this.modalService.open(content, { size: 'lg' }).result
  }

  NewKbModal(content) {
    this.modalService.open(content, { size: 'lg' }).result
  }

}
