import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

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
  private id: number;
  public sprintData: any = [];
  public codeData: any = [];
  public complianceForm: FormGroup;
  public routerId;

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
    this.breadCrumbItems = [{ label: 'Feature' }, { label: 'Summary', active: true }];
    this.getSprintItems();
    this.complianceForm = this.formBuilder.group({
      evidence: ['', Validators.required],
      resolved: ['', Validators.required],
    });

    this.routerId = localStorage.getItem('routerId');
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
    this.modalService.open(content, { size: 'sm', centered: true });
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

  onSubmit()
  {
    this.router.navigate(['/projects/summary']);
  }
}
