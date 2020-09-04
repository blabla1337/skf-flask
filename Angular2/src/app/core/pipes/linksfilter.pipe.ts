import { Pipe, PipeTransform } from '@angular/core';
import { ConstantPool } from '@angular/compiler';

@Pipe({
    name: 'linksfilter'
})
export class LinksFilterPipe implements PipeTransform
{
    public i: string = null;
    public links: any;

    transform(items: any[]): any {
        if(typeof(items)!=="undefined") {
            for(this.i in items){
                this.links = items[this.i].add_resources.split(",");
                items[this.i].add_resources = this.links.join("\n\r");
            }
            return items;
        }
    }
}

