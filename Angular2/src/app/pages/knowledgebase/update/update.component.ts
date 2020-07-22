import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';

import { KnowledgebaseService } from '../../../core/services/knowledgebase.service';

@Component({
  selector: 'app-update',
  templateUrl: './update.component.html',
  styleUrls: ['./update.component.scss']
})
export class UpdateComponent implements OnInit
{
  id: number;
  private sub: any;
  breadCrumbItems: Array<{}>;
  public knowledgebaseForm: FormGroup;
  public knowledgebaseItem: any;
  public isSubmitted: boolean;

  get formControls() { return this.knowledgebaseForm.controls; }

  constructor(
    private formBuilder: FormBuilder,
    private route: ActivatedRoute,
    private _knowledgebaseService: KnowledgebaseService,
    private router: Router) { }

  ngOnInit(): void
  {
    this.breadCrumbItems = [{ label: 'Knowledgebase' }, { label: 'Update', active: true }];

    this.sub = this.route.params.subscribe(params =>
    {
      this.id = +params['id'];
    });

    this.knowledgebaseForm = this.formBuilder.group({
      title: ['', Validators.required],
      content: ['', Validators.required],
    })

    this.knowledgebaseItem = this._knowledgebaseService
      .getKnowledgeBaseItem(this.id)
      .subscribe(item => this.knowledgebaseForm.patchValue(item))
  }

  updateKnowledgebaseItem()
  {
    this.isSubmitted = true;
    if (this.knowledgebaseForm.invalid) {
      return;
    }
    this._knowledgebaseService.updateKnowledgebaseItem(this.id, this.knowledgebaseForm.value).subscribe()
    this.router.navigate(['/knowledgebase/read'])
  }
}

