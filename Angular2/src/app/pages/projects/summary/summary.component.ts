import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { AppSettings } from '../../../global';

import { SprintService } from '../../../core/services/sprint.service';
import { CodeExamplesService } from '../../../core/services/code-examples.service';

@Component({
  selector: 'app-summary',
  templateUrl: './summary.component.html',
  styleUrls: ['./summary.component.scss']
})
export class SummaryComponent implements OnInit
{

  // bread crumb items
  breadCrumbItems: Array<{}>;

  // Collapse value
  public isCollapsed: boolean[] = [];
  private sub: any = [];
  public id: number;
  public sprintData: any = [];
  public codeData: any = [];
  public complianceForm: FormGroup;
  public routerId;
  public delete: string;
  public priv: string;

  // Form Submission
  public submit: boolean;
  public formsubmit: boolean;

  get formControls() { 
    return this.complianceForm.controls; 
  }

  constructor(
    private formBuilder: FormBuilder,
    private modalService: NgbModal,
    private route: ActivatedRoute,
    private _sprintService: SprintService,
    private _codeExampleService: CodeExamplesService,
    private router: Router
  ) { }


  ngOnInit(): void
  {
    this.priv = AppSettings.USER_PRIV;
    this.breadCrumbItems = [{ label: 'Feature' }, { label: 'Summary', active: true }];
    this.getSprintItems();
    this.complianceForm = this.formBuilder.group({
      evidence: ['', Validators.required],
      resolved: ['', Validators.required],
    });

    this.routerId = localStorage.getItem('routerId');
  }


  exportCsv(sprint_id)
  {
    this.route.params.subscribe(params =>
    {
      this._sprintService.exportCsv(sprint_id).subscribe(
        (resp) =>
        {
          const base64fix = resp['message'].replace('b\'', '');
          const base64 = base64fix.substring(0, base64fix.lastIndexOf('\''));

          const a = document.createElement('a');
          document.body.appendChild(a);

          const byteCharacters = atob(base64);
          const byteArrays = [];

          for (let offset = 0; offset < byteCharacters.length; offset += 512) {
            const slice = byteCharacters.slice(offset, offset + 512);

            const byteNumbers = new Array(slice.length);
            for (let i = 0; i < slice.length; i++) {
              byteNumbers[i] = slice.charCodeAt(i);
            }

            const byteArray = new Uint8Array(byteNumbers);

            byteArrays.push(byteArray);
          }

          const blob = new Blob(byteArrays, { type: 'text/html' });
          const url = window.URL.createObjectURL(blob);
          a.href = url;
          a.download = 'export.csv';
          a.click();
          window.URL.revokeObjectURL(url);
        },
        err => console.log('Error getting sprint stats')
      );
    });
  }

  getSprintItems()
  {
    this.sub = this.route.params.subscribe(params =>
    {
      this.id = +params['id'];
    });
    this._sprintService.getSprintChecklistResults(this.id).subscribe(sprint => this.sprintData = sprint)
  }


  getCodeExamples(checklist_kb_id: number)
  {
    this._codeExampleService.getChecklistKbCodeItems(checklist_kb_id).subscribe(code => this.codeData = code)
  }
  

  newCompliance(item: number){
    this.submit = true;
    if (this.complianceForm.invalid) {
      return;
    }
    this._sprintService
      .updateCompliance(item, this.complianceForm.value)
      .subscribe(() => {
      this.getSprintItems();
    });
  }


  /**
   * Open modal
   * @param content modal content
   */
  summaryModal(content: any)
  {
    this.modalService.open(content, { centered: true, size: 'lg' });
  }

  get form()
  {
    return this.complianceForm.controls;
  }

  /**
   * Validation form submit method
   */
  validSubmit()
  {
    this.submit = true;
  }

  /**
   * Open delete modal
   * @param deleteDataModal center modal data
   */
  deleteModal(deleteDataModal: any)
  {
    this.modalService.open(deleteDataModal, { centered: true, size: 'lg' });
  }

  deleteControl(control_id: number)
  {
    if (this.delete == 'DELETE') {
      this._sprintService.deleteControlsFromSprint(control_id).subscribe(x => this.getSprintItems());
    }
  }

  onSubmit()
  {
    this.router.navigate(['/projects/summary']);
  }
}
