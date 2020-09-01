// import { TestBed, async, ComponentFixture } from '@angular/core/testing';
// import { BrowserModule, By } from '@angular/platform-browser';
// import { FormsModule, ReactiveFormsModule } from '@angular/forms';
// import { DebugElement } from '@angular/core';

// import { LoginComponent } from '../../pages/auth/login/login.component';

// describe('AppComponent', () => {
//     let comp: LoginComponent;
//     let fixture: ComponentFixture<LoginComponent>;
//     let de: DebugElement;
//     let el: HTMLElement;

//     beforeEach(async(() => {
//       TestBed.configureTestingModule({
//         imports: [
//             LoginComponent
//         ],
//         declarations: [
//           BrowserModule,
//           FormsModule,
//           ReactiveFormsModule
//         ],
//       }).compileComponents().then(() => {
//           fixture = TestBed.createComponent(LoginComponent);
//           comp = fixture.componentInstance;

//           de = fixture.debugElement.query(By.css('form'));
//       });
//     }));

//     it('should call the onLogin method', async(() => {
//         fixture.detectChanges();
//         spyOn(comp, 'onLogin');
//         el = fixture.debugElement.query(By.css('button'))
//     }));

// });
