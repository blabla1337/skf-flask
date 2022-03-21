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
  private selectedCourseItem: CourseItem = undefined;

  constructor(private trainingNavigationService: TrainingNavigationService) {
  }

  ngOnInit(): void {
    if (this.course) {
      this.setNodesFromCourse(this.course);
    }
    this.subscriptions.push(this.trainingNavigationService.nextCourseItem$.subscribe(() => {
      console.log('TODO IB !!!! nextCourseItem$ in tree');
      this.setNextCourseItem();
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
        this.tree.treeModel.expandAll();
        this.tree.treeModel.roots[0].setActiveAndVisible();
      }
    }, 0);
  }

  private setNextCourseItem() {
    this.tree.treeModel.focusNextNode();
    const focusedNode = this.tree.treeModel.getFocusedNode();
    focusedNode.setActiveAndVisible();
  }

  onActivate(event: any) {
    const treeNode: TreeNode = event.node;
    this.selectedCourseItem = treeNode.data;
    this.trainingNavigationService.raiseCurrentCourseItemChanged(this.selectedCourseItem);
  }

  ngOnDestroy(): void {
    this.subscriptions.forEach(sub => {
      if (sub) {
        sub.unsubscribe();
      }
    });
  }
}
