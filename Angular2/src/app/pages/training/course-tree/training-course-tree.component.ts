import {Component, OnDestroy, OnInit, ViewChild} from '@angular/core';
import {Subscription} from 'rxjs';
import {TrainingService} from '../../../core/services/training.service';
import {Course, CourseItem} from '../../../core/models/course.model';
import {TreeComponent, TreeNode} from '@circlon/angular-tree-component';
import {TrainingPersistenceService} from '../../../core/services/training.persistence.service';
import {ActivatedRoute} from '@angular/router';

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

  constructor(private trainingService: TrainingService,
              private activatedRoute: ActivatedRoute,
              private trainingPersistenceService: TrainingPersistenceService) {

  }

  ngOnInit(): void {
    this.subscriptions.push(this.activatedRoute.params.subscribe(params => {
      const courseId = params['id'];
      this.subscriptions.push(this.trainingService.getCourse(courseId).subscribe(course => {
        if (course) {
          this.setNodesFromCourse(course);
        }
      }));
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
