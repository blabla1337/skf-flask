import {Component, OnDestroy, OnInit, ViewChild} from '@angular/core';
import {Subscription} from 'rxjs';
import {TrainingService} from '../../../core/services/training.service';
import {Course} from '../../../core/models/course.model';
import {TreeComponent} from '@circlon/angular-tree-component';

@Component({
  selector: 'app-training-course-tree',
  templateUrl: './training-course-tree.component.html',
  styleUrls: ['./training-course-tree.component.scss']
})
export class TrainingCourseTreeComponent implements OnInit, OnDestroy {
  @ViewChild(TreeComponent) private tree: TreeComponent;

  private subscriptions: Subscription[] = [];
  private course: Course;
  public nodes = [];
  public options = {};

  constructor(private trainingService: TrainingService) { }

  ngOnInit(): void {
    this.subscriptions.push(this.trainingService.getCourse("").subscribe(course => {
      this.course = course;
      this.nodes = course.topics.map(t => ({
        id: t.id,
        name: t.name,
        isExpanded: true,
        content: t.content,
        children: t.categories.map(c => ({
          id: c.id,
          name: c.name,
          content: c.content,
          children:[]
        }))
      }))
    }));

    setTimeout(() => {
      this.tree.treeModel.focusNextNode();
    }, 0)
  }

  ngOnDestroy(): void {
    this.subscriptions.forEach(sub => {
      if(sub) {
        sub.unsubscribe();
      }
    });
  }
}
