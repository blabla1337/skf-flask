import { Component, OnInit } from '@angular/core';
import { KnowledgebaseService } from '../services/knowledgebase.service'
import { AppSettings } from '../globals';
import * as JWT from 'jwt-decode';
import { Knowledgebase } from '../models/knowledgebase';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';

@Component({
  selector: 'app-knowledgebase',
  templateUrl: './knowledgebase.component.html',
  providers: [KnowledgebaseService]
})

export class KnowledgebaseComponent implements OnInit {

  public knowledgeitems: Knowledgebase[] = [];
  public queryString: string;
  public error: string;
  public errors: string[];
  public return: boolean;
  public title: string;
  public content: string;
  public canEdit: boolean;
  public delete: string;

  constructor(public _knowledgeService: KnowledgebaseService, private modalService: NgbModal) { }

  ngOnInit() {
    this.getKnowledgeItems();

    if (AppSettings.AUTH_TOKEN) {
      const decodedJWT = JWT(AppSettings.AUTH_TOKEN);
      this.canEdit = decodedJWT.privilege.includes('edit');
    }
  }

  getKnowledgeItems() {
    this._knowledgeService.getKnowledgeBase().subscribe(requestData => this.knowledgeitems = requestData,
      err => this.error = 'Error getting knowledge items, contact the administrator!'
    );
  }

  storeKnowledgebaseItem() {
    this.errors = [];
    this.return = true;

    if (!this.title) { this.errors.push('Title was left empty'); this.return = false; }
    if (!this.content) { this.errors.push('Content was left empty'); this.return = false; }
    if (this.return == false) { return; }

    this.errors = [];
    this._knowledgeService.newKnowledgebaseItem(this.title, this.content)
      .subscribe(
        () => this.errors.push('Eror storing a new knowledgebase item!')
      );
    this.getKnowledgeItems();
  }

  deleter(id: number) {
    if (this.delete == 'DELETE') {
      this._knowledgeService.deleteKnowledgebaseItem(id).subscribe(x =>
        // Get the new project list on delete
        this.getKnowledgeItems())
    }
  }

  deleteKbModal(content) {
    this.modalService.open(content, { size: 'lg' }).result
  }

  NewKbModal(content) {
    this.modalService.open(content, { size: 'lg' }).result
  }

}
