import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'stringfilter'
})
export class StringFilterPipe implements PipeTransform {

  transform(items: any[], args: any[]): any {
    if (args) {
      if (items[0].name) {
        return items.filter(item => item.name.toLowerCase().indexOf(args.toString().toLowerCase()) >= 0);
      }
      if (items[0].title) {
        return items.filter(item => item.title.toLowerCase().indexOf(args.toString().toLowerCase()) >= 0);
      }
      if (items[0].description) {
        return items.filter(item => item.description.toLowerCase().indexOf(args.toString().toLowerCase()) >= 0);
      }     
      if (items[0].checklist_items_content) {
        return items.filter(item => item.checklist_items_content.toLowerCase().indexOf(args.toString().toLowerCase()) >= 0);
      }       
      if (items[0].email) {
        return items.filter(item => item.email.toLowerCase().indexOf(args.toString().toLowerCase()) >= 0);
      }      
    }
    if (!args) {
      return items;
    }
  }

}
