import { browser, element, by } from 'protractor';

export class SKFAngularPage {
  navigateTo() {
    return browser.get('/login');
  }

  getParagraphText() {
    return element(by.css('app-root h1')).getText();
  }
}
