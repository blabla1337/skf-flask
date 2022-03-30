import {Component, Input, OnDestroy, OnInit, ViewChild} from '@angular/core';
import {Subscription} from 'rxjs';
import {Course, CourseItem} from '../../../core/models/course.model';
import {ITreeOptions, TreeComponent, TreeNode} from '@circlon/angular-tree-component';
import {TrainingNavigationService} from '../../../core/services/training-navigation.service';
import {TrainingService} from '../../../core/services/training.service';
import {ActivatedRoute} from '@angular/router';
import {KEYS} from '@circlon/angular-tree-component';

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
  private selectedCourseItem: CourseItem = undefined;

  public options: ITreeOptions = {
    actionMapping: {
      keys: {
        [KEYS.LEFT]: null,
        [KEYS.UP]: null,
        [KEYS.RIGHT]: null,
        [KEYS.DOWN]: null,
        [KEYS.SPACE]: null,
        [KEYS.ENTER]: null
      }
    }
  };

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
            this.setNodesFromCourse(this.course, seenCategoryIds);
          }));
        } else {
          this.setNodesFromCourse(this.course, []);
        }
      }));
    }
    this.subscriptions.push(this.trainingNavigationService.nextCourseItem$.subscribe(() => {
      this.setNextCourseItem();
    }));
    this.subscriptions.push(this.trainingNavigationService.markCategoryAsSeen$.subscribe(categoryId => {
      this.markCategoryAsSeen(categoryId)
    }));
  }

  private setNodesFromCourse(course: Course, seenCategoryIds: string[]) {
    const titleNode = {
      id: course.id,
      name: course.name,
      content: course.content ?? [],
      seen: true,
      children: [],
      courseItemType: 'Title',
    }

    const nodes = course.topics.map(t => ({
      id: t.id,
      name: t.name,
      content: t.content ?? [],
      seen: false,
      courseItemType: 'Topic',
      children: t.categories.map(c => ({
        id: c.id,
        name: c.name,
        content: c.content ?? [],
        seen: (seenCategoryIds.find(cid => cid === c.id) !== undefined),
        courseItemType: 'Category',
        children: [],
      }))
    }));
    nodes.forEach(t => t.seen = t.children.every(c => c.seen));

    this.nodes = [titleNode, ...nodes];

    setTimeout(() => {
      if (this.nodes.length > 0) {
        // this.tree.treeModel.expandAll();
        this.tree.treeModel.roots[0].setActiveAndVisible();
      }
    }, 0);
  }

  private markCategoryAsSeen(categoryId: string) {
    const newNodes = this.nodes.map(topic => {
     const categoryIndex = topic.children.findIndex(c => c.id === categoryId);
     if (categoryIndex !== -1) {
       const newCategory = {...topic.children[categoryIndex], seen: true};
       const newChildren = [...topic.children];
       newChildren.splice(categoryIndex, 1, newCategory);
       const newTopic = {
         ...topic,
         children: newChildren
       };
       newTopic.seen = newTopic.children.every(c => c.seen);
       return newTopic;
     } else {
       return {...topic};
     }
    });
    this.nodes = newNodes;
  }

  private setNextCourseItem() {
    const oldFocusedNode = this.tree.treeModel.getFocusedNode();
    oldFocusedNode.expand();
    this.tree.treeModel.focusNextNode();
    const focusedNode = this.tree.treeModel.getFocusedNode();
    if (focusedNode !== oldFocusedNode) {
      focusedNode.setActiveAndVisible();
      focusedNode.scrollIntoView(true);
    }
  }

  onActivateNode(event: any) {
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
