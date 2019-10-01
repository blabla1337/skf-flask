import {Injectable, Pipe, PipeTransform} from '@angular/core';

@Pipe({
    name: 'StartsWithPipe',
    pure: false
})
@Injectable()
export class StartsWithPipe implements PipeTransform {
    transform(items: any[], args: any[]): any {
        if (args) {
          return items.filter(item => item.title.toLowerCase().startsWith(args.toString().toLowerCase()));
        }
        if (!args) {
          return items;
        }
    }
}
