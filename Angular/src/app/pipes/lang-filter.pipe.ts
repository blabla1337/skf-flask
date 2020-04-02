import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'langFilter',
  pure: false
})
export class LangFilterPipe implements PipeTransform {

  transform(items: any[], args: any[]): any {
    if (args && args.length > 0) {
      return items.filter(item => args.indexOf(item.code_lang) >= 0);
    }
    else {
      return items;
    }
  }

}
