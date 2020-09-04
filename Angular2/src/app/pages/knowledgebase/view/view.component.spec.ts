import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { RouterTestingModule } from '@angular/router/testing';
import { HttpClientTestingModule } from '@angular/common/http/testing';
import { NgbNavModule } from "@ng-bootstrap/ng-bootstrap";
import { ViewKnowledebaseComponent } from './view.component';


describe('ViewKnowledebaseComponent', () =>
{
  let component: ViewKnowledebaseComponent;
  let fixture: ComponentFixture<ViewKnowledebaseComponent>;

  beforeEach(async(() =>
  {
    TestBed.configureTestingModule({
      imports: [RouterTestingModule, HttpClientTestingModule, NgbNavModule],
      declarations: [ViewKnowledebaseComponent]
    })
      .compileComponents();
  }));

  beforeEach(() =>
  {
    fixture = TestBed.createComponent(ViewKnowledebaseComponent);
    component = fixture.componentInstance;
    component.ngOnInit();
    fixture.detectChanges();
  });

  it('should create', () =>
  {
    expect(component).toBeTruthy();
  });
});
