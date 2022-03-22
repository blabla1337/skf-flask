import {Component, Input, OnDestroy, OnInit, ViewChild} from '@angular/core';
import {Subscription} from 'rxjs';
import {Course, CourseItem} from '../../../core/models/course.model';
import {TreeComponent, TreeNode} from '@circlon/angular-tree-component';
import {TrainingNavigationService} from '../../../core/services/training-navigation.service';
import {TrainingService} from '../../../core/services/training.service';
import {ActivatedRoute} from '@angular/router';

@Component({
  selector: 'app-training-course-tree',
  templateUrl: './training-course-tree.component.html',
  styleUrls: ['./training-course-tree.component.scss']
})
export class TrainingCourseTreeComponent implements OnInit, OnDestroy {
  @ViewChild(TreeComponent) private tree: TreeComponent;
  @Input() public course: Course;
  @Input() public userId: string;
  private subscriptions: Subscription[] = [];
  public nodes = [];
  public options = {};
  private selectedCourseItem: CourseItem = undefined;

  constructor(private trainingNavigationService: TrainingNavigationService,
              private activatedRoute: ActivatedRoute,
              private trainingService: TrainingService) {
  }

  ngOnInit(): void {
    if (this.course) {
      this.subscriptions.push(this.activatedRoute.params.subscribe(params => {
        const courseId = params['cid'];
        if (this.userId !== undefined && this.userId !== "") {
          this.subscriptions.push(this.trainingService.getCourseProgress(this.userId, courseId).subscribe(seenCategoryIds => {
            console.log('TODO IB !!!! seenCategoryIds', seenCategoryIds);
            this.setNodesFromCourse(this.course, seenCategoryIds);
          }));
        } else {
          this.setNodesFromCourse(this.course, []);
        }
      }));
    }
    this.subscriptions.push(this.trainingNavigationService.nextCourseItem$.subscribe(() => {
      console.log('TODO IB !!!! nextCourseItem$ in tree');
      this.setNextCourseItem();
    }));
  }

  private setNodesFromCourse(course: Course, seenCategoryIds: string[]) {
    const nodes = course.topics.map(t => ({
      id: t.id,
      name: t.name,
      content: t.content,
      seen: false,
      courseItemType: 'Topic',
      children: t.categories.map(c => ({
        id: c.id,
        name: c.name,
        content: c.content,
        seen: (seenCategoryIds.find(cid => cid === c.id) !== undefined),
        courseItemType: 'Category',
        children: [],
      }))
    }));
    nodes.forEach(t => t.seen = t.children.every(c => c.seen));

    this.nodes = nodes;

    console.log('TODO IB !!!! this.nodes', this.nodes);

    setTimeout(() => {
      if (this.nodes.length > 0) {
        this.tree.treeModel.expandAll();
        this.tree.treeModel.roots[0].setActiveAndVisible();
      }
    }, 0);
  }

  private setNextCourseItem() {
    const oldFocusedNode = this.tree.treeModel.getFocusedNode();
    this.tree.treeModel.focusNextNode();
    const focusedNode = this.tree.treeModel.getFocusedNode();
    if (focusedNode !== oldFocusedNode) {
      focusedNode.setActiveAndVisible();
    }
  }

  onActivateNode(event: any) {
    const treeNode: TreeNode = event.node;
    console.log('TODO IB !!!! onActivateNode treeNode', treeNode);
    console.log('TODO IB !!!! this.nodes', this.nodes);
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
