import { TestBed, inject } from '@angular/core/testing';
import { GuardService } from './guard.service';
import { RouterTestingModule } from '@angular/router/testing';
import { Router } from "@angular/router";
import { AppSettings } from '../globals';

describe('GuardService', () => {
  AppSettings.AUTH_TOKEN = null;
  let router = {
    navigate: jasmine.createSpy('navigate')
  }

  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [GuardService, { provide: Router, useValue: router }],
      imports: [RouterTestingModule],

    });
  });
  it('should create the service for the route guard', inject([GuardService], (service: GuardService) => {
    expect(service).toBeTruthy();
  }));

  it('should check the service to return false', inject([GuardService], (service: GuardService) => {
    service.canActivate()
    expect(router.navigate).toHaveBeenCalledWith(['/login']);
    expect(service.returner).toBeFalsy();
  }));
});
