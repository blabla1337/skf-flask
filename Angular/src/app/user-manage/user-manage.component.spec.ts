import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { UserManageComponent } from './user-manage.component';
import { HttpModule } from '@angular/http';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { RouterTestingModule } from '@angular/router/testing';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

describe('UserManageComponent', () => {
  let component: UserManageComponent;
  let fixture: ComponentFixture<UserManageComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ UserManageComponent ],
      imports:[NgbModule.forRoot(), RouterTestingModule, FormsModule, HttpModule]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(UserManageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create list of al the users', () => {
    expect(component).toBeTruthy();
  });
});
