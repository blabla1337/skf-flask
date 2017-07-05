import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { KnowledgebaseComponent } from './knowledgebase.component';

describe('KnowledgebaseComponent', () => {
  let component: KnowledgebaseComponent;
  let fixture: ComponentFixture<KnowledgebaseComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ KnowledgebaseComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(KnowledgebaseComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
