import { ComponentFixture, TestBed, waitForAsync } from '@angular/core/testing';
import { OpenidComponent } from './openid.component';
import { RouterTestingModule } from '@angular/router/testing';


describe('OpenidComponent', () =>
{
  let component: OpenidComponent;
  let fixture: ComponentFixture<OpenidComponent>;

  beforeEach(waitForAsync(() =>
  {
    TestBed.configureTestingModule({
      imports: [RouterTestingModule],
      declarations: [OpenidComponent]
    })
      .compileComponents();
  }));

  beforeEach(() =>
  {
    fixture = TestBed.createComponent(OpenidComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () =>
  {
    expect(component).toBeTruthy();
  });
});
