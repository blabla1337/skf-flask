import {async, ComponentFixture, TestBed} from '@angular/core/testing';
import {ProjectSummaryComponent} from './project-summary.component';
import {HttpModule} from '@angular/http';
import {NgbModule} from '@ng-bootstrap/ng-bootstrap';
import {RouterTestingModule} from '@angular/router/testing';
import {FormsModule, ReactiveFormsModule} from '@angular/forms';


describe('ProjectSummaryComponent', () => {
  let component: ProjectSummaryComponent;
  let fixture: ComponentFixture<ProjectSummaryComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ProjectSummaryComponent],
      imports: [NgbModule.forRoot(), FormsModule, HttpModule, RouterTestingModule]
    })
      .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ProjectSummaryComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create a summary of all sprints and pre development', () => {
    expect(component).toBeTruthy();
  });

  it('should call fetchComment', () => {
    spyOn(component, 'fetchComment');
    component.sprintResult = [
      {
        "status": 1,
        "sprintID": 1,
        "projectID": 1,
        "checklistID": 1057,
        "kb_item_title": "Version management",
        "kb_items_content": " Description:\n\nWhenever a programmer decides to use third party software,\nhe should keep an eye implementing a proper version management methodology for this software.\nWhen hackers discover vulnerabilities they often publish these exploits online in order\nto push the developers of this software to fix their issues. As a result,\nwhen your software is not upgraded to the latest available version,\nscript kiddies could easily compromise your application by following the\nexploit tutorials online, thus compromising your application.\n\n Solution:\n\nOne option is not to use components that you did not write.\nBut that is not very realistic.\n\nMost component projects do not create vulnerability patches for old versions.\nInstead, most simply fix the problem in the next version. So upgrading to these new\nversions is critical.\nSoftware projects should have a process in place to:\n\nIdentify all components and the versions you are using, including all dependencies.\n(e.g., the versions plugin).\n\nMonitor the security of these components in public databases,\nproject mailing lists, and security mailing lists, and keep them up to date.\n\nEstablish security policies governing components use, such as requiring certain software\ndevelopment practices, passing security tests, and acceptable licenses.\n\nWhere appropriate, consider adding security wrappers around components to disable unused\nfunctionality and/ or secure weak or vulnerable aspects of the component.\n\nThis also goes for all other components that should be up to date with proper security\nconfiguration(s) and version(s) such as server OS etc.\n\nThis should include removal of unneeded configurations and folders such as sample\napplications, platform documentation, and default or example users.\n",
        "checklist_items_checklistID": "20.1",
        "checklist_items_content": "Custom checklist item example, lorum ipsum",
        "cwe": null
      }
    ];
    fixture.detectChanges();
    let btnEle = fixture.debugElement.nativeElement.querySelector('.content-panel > div');
    btnEle.click();
    expect(component.fetchComment).toHaveBeenCalled();
  });
});
