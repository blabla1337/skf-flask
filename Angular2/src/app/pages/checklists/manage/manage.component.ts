import { Component, OnInit } from '@angular/core';
import { DndDropEvent } from 'ngx-drag-drop';

import { manageData } from './data';
import { Manage } from './manage.model';

@Component({
  selector: 'app-manage',
  templateUrl: './manage.component.html',
  styleUrls: ['./manage.component.scss']
})
export class CheckManageComponent implements OnInit {

  checkTotal: Manage[];
  checkItems: Manage[];

  // bread crumb items
  breadCrumbItems: Array<{}>;

  constructor() { }

  ngOnInit() {
    this.breadCrumbItems = [{ label: 'Checklists' }, { label: 'Manage', active: true }];


    this._fetchData();
  }

  /**
   * on dragging
   * @param item item dragged
   * @param list list from item dragged
   */
  onDragged(item: any, list: any[]) {
    const index = list.indexOf(item);
    list.splice(index, 1);
  }

  /**
   * On drop event
   */
  onDrop(event: DndDropEvent, filteredList?: any[], targetStatus?: string) {
    if (filteredList && event.dropEffect === 'move') {
      let index = event.index;

      if (typeof index === 'undefined') {
        index = filteredList.length;
      }

      filteredList.splice(index, 0, event.data);
    }
  }

  private _fetchData() {
    this.checkTotal = manageData.filter(t => t.status === 'Completed');
    this.checkItems = manageData.filter(t => t.status === 'Pending');
  }

}
