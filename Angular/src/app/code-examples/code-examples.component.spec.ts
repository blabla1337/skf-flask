import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { CodeExamplesComponent } from './code-examples.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { StartsWithPipe } from '../pipes/starts-with.pipe'
import { RouterTestingModule } from '@angular/router/testing';


describe('CodeExamplesComponent', () => {
  let component: CodeExamplesComponent;
  let fixture: ComponentFixture<CodeExamplesComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CodeExamplesComponent, StartsWithPipe ],
      imports:[FormsModule, HttpModule, RouterTestingModule, NgbModule.forRoot()]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CodeExamplesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create code example component', () => {
    expect(component).toBeTruthy();
  });
});
