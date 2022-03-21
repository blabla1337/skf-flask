import {Component, Input, OnDestroy, OnInit, ViewChild} from '@angular/core';
import {Subscription} from 'rxjs';
import {Course, CourseItem} from '../../../core/models/course.model';
import {TreeComponent, TreeNode} from '@circlon/angular-tree-component';
import {TrainingNavigationService} from '../../../core/services/training-navigation.service';

@Component({
  selector: 'app-training-course-tree',
  templateUrl: './training-course-tree.component.html',
  styleUrls: ['./training-course-tree.component.scss']
})
export class TrainingCourseTreeComponent implements OnInit, OnDestroy {
  @ViewChild(TreeComponent) private tree: TreeComponent;
  private subscriptions: Subscription[] = [];
  public nodes = [];
  public options = {};
  @Input() public course: Course;

  constructor(private trainingNavigationService: TrainingNavigationService) {
  }

  ngOnInit(): void {
    if (this.course) {
      this.setNodesFromCourse(this.course);
    }
    this.subscriptions.push(this.trainingNavigationService.nextCourseItem$.subscribe(() => {
      console.log('TODO IB !!!! nextCourseItem$ in tree');
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
        children: []
      }))
    }));

    setTimeout(() => {
      if (this.nodes.length > 0) {
        this.tree.treeModel.roots.map(x => x.expand());
        this.tree.treeModel.roots[0].setActiveAndVisible();
      }
    }, 0);
  }

  onActivate(event: any) {
    const treeNode: TreeNode = event.node;
    const courseItem: CourseItem = treeNode.data;
    this.trainingNavigationService.raiseCurrentCourseItemChanged(courseItem);
  }

  ngOnDestroy(): void {
    this.subscriptions.forEach(sub => {
      if (sub) {
        sub.unsubscribe();
      }
    });
  }
}
