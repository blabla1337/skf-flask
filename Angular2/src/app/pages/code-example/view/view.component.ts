import { Component, OnInit } from '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { NgxSpinnerService  } from 'ngx-spinner';
import { AppSettings } from '../../../global';

import { CodeExamplesService } from '../../../core/services/code-examples.service';
import { ChecklistCategoryService } from '../../../core/services/checklist_category.service';

@Component({
  selector: 'app-view',
  templateUrl: './view.component.html',
  styleUrls: ['./view.component.scss']
})
export class ViewCodeComponent implements OnInit 
{

  // bread crumb items
  breadCrumbItems: Array<{}>;

  // Collapse value
  public isCollapsed: boolean[] = [];
  public codeData: any = [];
  public categoryData: any = [];
  public codeExample: any = [];
  public codeExampleForm: FormGroup;
  public queryString;
  public catSelector: number;
  public delete: string;
  public loggedinUser: string;
  public loggedin = false;
  public priv: string;

  get formControls() { return this.codeExampleForm.controls; }

  constructor(
    private modalService: NgbModal,
    private _codeExamplesService: CodeExamplesService,
    private _checklistCategoryService: ChecklistCategoryService,
    private spinner: NgxSpinnerService,
  ) { }

  ngOnInit()
  {
    if(AppSettings.USER_PRIV != null){
      this.priv = AppSettings.USER_PRIV;
    }else{
      this.priv = "";
    }
    this.breadCrumbItems = [{ label: 'Code Examples' }, { label: 'View', active: true }];
    this._fetchData();
    this.catSelector = Number(localStorage.getItem("categorySelector"));
  }

  /**
   * Knowledgebase data fetches
   */
  private _fetchData()
  {
    this.spinner.show();
    this._codeExamplesService
      .getCode(Number(localStorage.getItem('categorySelector')))
      .subscribe(data => {
        this.codeData = data;
        this.spinner.hide();
      });

    this._checklistCategoryService
      .getChecklistCategoryCollection()
      .subscribe(data => this.categoryData = data);
  }

  showCode(value: number) {
    this.spinner.show();
    this._codeExamplesService
      .getCodeExample(Number(value)).subscribe(test => 
        {
          this.codeExample = test
          this.spinner.hide();
        });
  }

  loggedIn()
  {
    this.loggedinUser = sessionStorage.getItem('Authorization');
    this.loggedin = true;
    return this.loggedinUser;
  }

  /**
   * Open delete modal
   * @param deleteDataModal center modal data
   */
  deleteModal(deleteDataModal: any)
  {
    this.modalService.open(deleteDataModal, { centered: true, size: 'lg' });
  }

  setCategorySelectorId(categoryId: Number)
  {
    localStorage.setItem('categorySelector', categoryId.toString());
    this._fetchData();
  }

  deleteCodeExample(code_id: number)
  {
    if (this.delete == 'DELETE') {
      this._codeExamplesService.deleteCodeExample(code_id).subscribe(x => this._fetchData())
    }
  }
}
