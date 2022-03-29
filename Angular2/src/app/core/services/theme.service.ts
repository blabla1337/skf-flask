import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';

@Injectable()
export class ThemeService {
    themeStyle: string;
    public theme: BehaviorSubject<string> = new BehaviorSubject('');
    constructor() {}

    editTheme(newTheme) {
        localStorage.removeItem('theme');
        localStorage.setItem('theme', newTheme);
        this.themeStyle = localStorage.getItem('theme');
        this.theme.next(this.themeStyle);
    }
}
