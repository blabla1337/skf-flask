import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'stringfilter'
})
export class StringFilterPipe implements PipeTransform {

  transform(items: any[], args: any[]): any {
    if (args) {
      return items.filter(item => item.title.toLowerCase().indexOf(args.toString().toLowerCase()) >= 0);
    }
    if (!args) {
      return items;
    }
  }

}
