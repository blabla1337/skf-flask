import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';

@Injectable()
export class ThemeService {
    themeStyle: string;
    public theme: BehaviorSubject<string> = new BehaviorSubject('');
    constructor() {}

    editTheme(newTheme) {
        sessionStorage.removeItem('theme');
        sessionStorage.setItem('theme', newTheme);
        this.themeStyle = sessionStorage.getItem('theme');
        this.theme.next(this.themeStyle);
    }
}
