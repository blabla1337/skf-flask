import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';

import { KnowledgebaseService } from '../../../core/services/knowledgebase.service';

@Component({
  selector: 'app-hard-link',
  templateUrl: './hard-link.component.html',
  styleUrls: ['./hard-link.component.scss']
})
export class HardLinkKBComponent implements OnInit
{
  public id: number;
  private sub: any;
  public breadCrumbItems: Array<{}>;
  public knowledgebaseItem: any = [];

  // Form Submission
  public submit: boolean;
  public formsubmit: boolean;

  constructor(
    private route: ActivatedRoute,
    private _knowledgebaseService: KnowledgebaseService,
    private router: Router) { }

  ngOnInit(): void
  {
    this.breadCrumbItems = [{ label: 'Knowledgebase' }, { label: 'hard-link', active: true }];

    this.sub = this.route.params.subscribe(params =>
    {
      this.id = +params['id'];
    });

    this._knowledgebaseService
      .getKnowledgeBaseItem(this.id)
      .subscribe(item => this.knowledgebaseItem = item)
  }
}

