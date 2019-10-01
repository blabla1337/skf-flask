import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { LabsComponent } from './labs.component';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';
import { RouterTestingModule } from '@angular/router/testing';
import { StringFilterPipe } from '../pipes/string-filter.pipe';


describe('LabsComponent', () => {
  let component: LabsComponent;
  let fixture: ComponentFixture<LabsComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ LabsComponent, StringFilterPipe ],
      imports: [NgbModule.forRoot(), RouterTestingModule,HttpModule, FormsModule]
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
