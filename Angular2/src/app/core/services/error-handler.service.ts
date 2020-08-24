import { Injectable } from '@angular/core';
import { HttpErrorResponse } from '@angular/common/http';
import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class ErrorHandlerService {

  public errorMessage = '';

  constructor(private router: Router) { }

  public handleError = (error: HttpErrorResponse) => {
    if (error.status === 500){
      this.handle500Error(error);
    }
    else if (error.status === 404){
      this.handle404Error(error);
    }
    else{
      this.handleOtherError(error);
    }
  }

  private handle500Error = (error: HttpErrorResponse) => {
    this.createErrorMessage(error);
    this.router.navigate(['/page-500']);
  }

  private handle404Error = (error: HttpErrorResponse) => {
    this.createErrorMessage(error);
    this.router.navigate(['/page-404']);
  }

  private handleOtherError = (error: HttpErrorResponse) => {
    this.createErrorMessage(error);
    // TODO: Can be added later;
  }

  private createErrorMessage = (error: HttpErrorResponse) => {
    this.errorMessage = error.error ? error.error : error.statusText;
  }
}
