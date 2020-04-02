import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
    name: 'labelFilter',
    pure: false
})
export class LabelFilterPipe implements PipeTransform
{

    transform(items: any[], args: any[]): any
    {
        if (args && args.length > 0) {
            return items.filter(item => args.indexOf(item.label) >= 0);
        }
        else {
            return items;
        }
    }

}
