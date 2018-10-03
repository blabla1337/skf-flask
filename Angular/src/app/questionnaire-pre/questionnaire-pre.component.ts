import { Component, OnInit } from '@angular/core';
import { NgbModal, ModalDismissReasons } from '@ng-bootstrap/ng-bootstrap';
import { AppSettings } from '../globals';
import * as JWT from 'jwt-decode';


@Component({
  selector: 'app-questionnaire-pre',
  templateUrl: './questionnaire-pre.component.html',
  providers: []
})
export class QuestionnairePreComponent implements OnInit {

  closeResult: string;
  public canDelete: boolean;

  constructor(
    private modalService: NgbModal,
  ) { }

  ngOnInit() {
    if (AppSettings.AUTH_TOKEN) {
      let decodedJWT = JWT(AppSettings.AUTH_TOKEN);
      this.canDelete = decodedJWT.privilege.includes("delete");
    }
  };

  addQuestion(add) {
    this.modalService.open(add, { size: 'lg' })
  }

  updateQuestion(update) {
    this.modalService.open(update, { size: 'lg' })
  }

  deleteQuestion(deletes) {
    this.modalService.open(deletes, { size: 'lg' })
  }
}
