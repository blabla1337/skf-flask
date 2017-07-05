import { TestBed, inject } from '@angular/core/testing';
import { GuardService } from './guard.service';
import { RouterTestingModule } from '@angular/router/testing';

describe('GuardService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [GuardService],
      imports:[RouterTestingModule]
    });
  });
  it('should create the service for the route guard', inject([GuardService], (service: GuardService) => {
    expect(service).toBeTruthy();
  }));

  it('should check the service to return false', inject([GuardService], (service: GuardService) => {
    service.canActivate()
    expect(service.returner).toBeDefined();
  }));
});
