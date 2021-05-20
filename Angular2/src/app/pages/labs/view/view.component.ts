import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { environment } from '../../../../environments/environment';

import Swal from 'sweetalert2';

import { NgxSpinnerService } from 'ngx-spinner';
import { LabService } from '../../../core/services/lab.service';

@Component({
  selector: 'app-view',
  templateUrl: './view.component.html',
  styleUrls: ['./view.component.scss']
})
export class LabViewComponent implements OnInit
{

  // bread crumb items
  breadCrumbItems: Array<{}>;

  public isCollapsed: boolean[] = [];
  public labData: any = [];
  public queryString;
  public queryLabel;
  public deployments;
  public labLists: string[];
  public lab: any = [];
  public status: any = [];
  public codeLabsData: any = [];
  public catSelector: number;
  public categoryData = ['php', 'java', 'asp', 'python'];
  public lab_code_answer: any = [];
  public lab_code_status: any = [];
  public lab_code_example: any = [];

  public kubernetes_enabled = environment.KUBERNETES_ENABLED;
  public loggedinUser: string;
  public loggedin = false;

  public codeDataTest: any = [];

  // tslint:disable-next-line: variable-name
  constructor(
    private _labService: LabService,
    private spinner: NgxSpinnerService,
    private router: Router,
  ) { }

  ngOnInit(): void
  {
    this.showStatus();
    this.breadCrumbItems = [{ label: 'Labs' }, { label: 'View', active: true }];
    this._fetchData();
    this.labLists = ['SKF-Labs', 'Juice-Shop', 'Other Labs'];

    // TEST VAR FOR STYLING ONLY CAN BE REMOVED LATER
    this.codeDataTest = '    <?php\r    $cmd = $_GET["cmd"];\r    $result = system($_GET["cmd"]);\r    print $result;\r    ?>';
  }

  /**
   * Labs data fetches
   */
  private _fetchData()
  {
    this.spinner.show();
    this._labService
      .getLabs()
      .subscribe(lab =>
      {
        this.labData = lab;
        this.spinner.hide();
      });
  }

    /**
   * Labs code data fetches
   */
  private _fetchCodeLabs(categoryCodeLang)
  {
    this.spinner.show();
    this._labService
      .getLabs()
      .subscribe(lab =>
      {
        this.labData = lab;
        this.spinner.hide();
      });
    this._labService
    .getCodeLabs(categoryCodeLang)
    .subscribe(data => this.codeLabsData = data);
  }

  showStatus()
  {
    this.status = JSON.parse(localStorage.getItem("labs-deployed"));
  }

  // Get Lab Address
  // tslint:disable-next-line: variable-name
  getLabAddress(image_tag)
  {
    this.spinner.show()
    this._labService.deployLab(image_tag).subscribe(requestData =>
    {
      this.spinner.hide();
      this.lab = requestData;
      var lab_split = this.lab.split("\\");
      this.lab = lab_split[3].substring(1);
      Swal.queue([
        {
          title: 'Lab deployment URL',
          text: this.lab,
          confirmButtonText: 'Close',
          confirmButtonColor: '#8184B2',
          showLoaderOnConfirm: true,
          onClose: () =>
          {
            this.status.push(image_tag)
            localStorage.setItem("labs-deployed", JSON.stringify(this.status));
          },
          preConfirm: () =>
          {
          }
        }
      ]);
    });
  }

  viewLabs()
  {
    this.router.navigate(['/labs/view'])
  }

  stopLabFromRunning(image_tag)
  {
    this.spinner.show()
    this._labService.deleteLab(image_tag).subscribe(requestData =>
    {
      this.deployments = requestData
      this.spinner.hide();
      Swal.queue([
        {
          title: 'Lab deployment Stopped',
          text: "The running lab has been stopped.",
          confirmButtonText: 'Close',
          confirmButtonColor: '#8184B2',
          showLoaderOnConfirm: true,
          onClose: () =>
          {
            this.status.splice(this.status.indexOf(image_tag), 1);
            localStorage.setItem("labs-deployed", JSON.stringify(this.status));
          },
          preConfirm: () =>
          {
          }
        }
      ]);
    })
  }


  loggedIn()
  {
    this.loggedinUser = sessionStorage.getItem('Authorization');
    this.loggedin = true;
    return this.loggedinUser;
  }


  setCategorySelectorLang(categoryCodeLang: String = 'php')
  {
    localStorage.setItem('codeReviewLanguage', categoryCodeLang.toString());
    this._fetchCodeLabs(categoryCodeLang);
  }

  answer_question(code_id: number, solution_id: number)
  {
    this._labService
    .solveCodeReviewChallenge(code_id, solution_id)
    .subscribe(data => console.log(data));
  }

  answer_fail()
  {
    this.lab_code_status = false;
    this.lab_code_answer = "It was a CMD injection combined with a Secret Unicorn \r Sometimes developers while creating code invoke a secret unicorn \r this is the reason they exist in old fory stories but people are not able to spot them.";
    this.lab_code_example = '    <?php\r    $cmd = $_GET["cmd"];\r    $escaped_command = escapeshellcmd($_GET["cmd"]);\r    $result = system($escaped_command);\r    print $result;\r    ?>';
  }
  
  answer_success()
  {
    this.lab_code_status = true;
    this.lab_code_answer = "It was a CMD injection combined with a Secret Unicorn \r Sometimes developers while creating code invoke a secret unicorn \r this is the reason they exist in old fory stories but people are not able to spot them.";
    this.lab_code_example = '    <?php\r    $cmd = $_GET["cmd"];\r    $escaped_command = escapeshellcmd($_GET["cmd"]);\r    $result = system($escaped_command);\r    print $result;\r    ?>'; 
  }

}
