import {AfterViewInit, Component, OnDestroy, OnInit, ViewChild} from '@angular/core';
import {Subscription} from 'rxjs';
import {TrainingService} from '../../../core/services/training.service';
import {Course, CourseItem} from '../../../core/models/course.model';
import {TreeComponent, TreeNode} from '@circlon/angular-tree-component';
import {TrainingPersistenceService} from '../../../core/services/training.persistence.service';

@Component({
  selector: 'app-training-course-tree',
  templateUrl: './training-course-tree.component.html',
  styleUrls: ['./training-course-tree.component.scss']
})
export class TrainingCourseTreeComponent implements OnInit, AfterViewInit, OnDestroy {
  @ViewChild(TreeComponent) private tree: TreeComponent;
  private subscriptions: Subscription[] = [];
  public nodes = [];
  public options = {};

  constructor(private trainingService: TrainingService,
              private trainingPersistenceService: TrainingPersistenceService) {

  }

  ngOnInit(): void {
    this.subscriptions.push(this.trainingService.getCourse("").subscribe(course => {
      this.setNodesFromCourse(course);
    }));
  }

  private setNodesFromCourse(course: Course) {
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
    }));
  }

  ngAfterViewInit() {
    if (this.nodes.length > 0) {
      this.tree.treeModel.roots[0].setActiveAndVisible();
    }
  }

  onActivate(event: any) {
    const treeNode: TreeNode = event.node;
    const courseItem: CourseItem = treeNode.data;
    this.trainingPersistenceService.setSelectedCourseItem(courseItem);
  }

  ngOnDestroy(): void {
    this.subscriptions.forEach(sub => {
      if(sub) {
        sub.unsubscribe();
      }
    });
  }
}
