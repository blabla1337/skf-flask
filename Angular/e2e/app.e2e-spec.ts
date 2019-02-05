import { SKFAngularPage } from './app.po';

describe('skf-angular App', () => {
  let page: SKFAngularPage;

  beforeEach(() => {
    page = new SKFAngularPage();
  });

  it('should display message saying app works', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('app works!');
  });
});
