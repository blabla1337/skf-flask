import { Component, OnInit } from '@angular/core';
import { KnowledgebaseService } from '../services/knowledgebase.service'
import { FormBuilder, FormGroup, Validators } from  '@angular/forms';
import { Knowledgebase } from '../models/knowledgebase';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { CategoryService } from '../services/category.service';
import { Category } from '../models/category';

@Component({
  selector: 'app-knowledgebase',
  templateUrl: './knowledgebase.component.html',
  providers: [KnowledgebaseService, CategoryService]
})

export class KnowledgebaseComponent implements OnInit {
  knowledgebaseForm: FormGroup;
  public isSubmitted: boolean;
  public delete: string;
  public knowledgeitems: Knowledgebase[] = [];
  public queryString: string;
  public categories: Category[];
  public category_id: number;

  get formControls() { return this.knowledgebaseForm.controls; }

  constructor(public _knowledgeService: KnowledgebaseService, private categoryService: CategoryService, private modalService: NgbModal, private formBuilder: FormBuilder) { }

  ngOnInit() {
    this.knowledgebaseForm = this.formBuilder.group({
      title: ['', Validators.required],
      content: ['', Validators.required]
    })
    this.categoryList();
  }

  categoryList() {
    this.categoryService
      .getCategories()
      .subscribe(
      categories => {
        this.categories = categories;
        if (this.categories) {
          console.log('There are no projects to show!')
        }
      },
      err => console.log('Getting the projects failed, contact an administrator! '));
  }

  storeKnowledgebaseItem() {
    this.isSubmitted = true;
    if(this.knowledgebaseForm.invalid){
      return;
    }
    this._knowledgeService.newKnowledgebaseItem(this.category_id, this.knowledgebaseForm.value)
      .subscribe(
        () => this.getKnowledgeItems(this.category_id)
      );
    
  }

  deleteKnowledgebaseItem(id: number) {
    if (this.delete == 'DELETE') {
      this._knowledgeService.deleteKnowledgebaseItem(id).subscribe(x =>
        this.getKnowledgeItems(this.category_id))
    }
  }

  getKnowledgeItems(category_id: number) {
    this._knowledgeService.getKnowledgeBase(category_id).subscribe(requestData => this.knowledgeitems = requestData,
      () => console.log('Error getting knowledge items, contact the administrator!')
    );
  }

  selectChecklistsFromCategory(){
    localStorage.setItem("category_id", this.category_id.toString());
    this.getKnowledgeItems(this.category_id);
  }

  deleteKbModal(content) {
    this.modalService.open(content, { size: 'lg' }).result
  }

  NewKbModal(content) {
    this.modalService.open(content, { size: 'lg' }).result
  }

}
