import { ComponentFixture, TestBed } from '@angular/core/testing';
import {TrainingProfilesComponent} from './training-profiles.component';


describe('TrainingProfilesComponent', () => {
  let component: TrainingProfilesComponent;
  let fixture: ComponentFixture<TrainingProfilesComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ TrainingProfilesComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(TrainingProfilesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
