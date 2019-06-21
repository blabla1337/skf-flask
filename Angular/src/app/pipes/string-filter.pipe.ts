import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'stringFilter',
  pure: false
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
