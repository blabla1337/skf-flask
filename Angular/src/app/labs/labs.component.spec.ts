import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { LabsComponent } from './labs.component';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { RouterTestingModule } from '@angular/router/testing';


describe('LabsComponent', () => {
  let component: LabsComponent;
  let fixture: ComponentFixture<LabsComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ LabsComponent ],
      imports: [NgbModule.forRoot(), RouterTestingModule]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(LabsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create the labs page', () => {
    expect(component).toBeTruthy();
  });
});
