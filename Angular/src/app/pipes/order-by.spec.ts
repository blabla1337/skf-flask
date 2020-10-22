import { OrderBy } from './order-by.pipe';

describe('LPadPipe', () => { // <----------------
  let pipe: OrderBy;

  beforeEach(() => {
    pipe = new OrderBy();
  });

  it('transforms "1" to "0001"', () => {
    const value: any = '1';
    const args: string[] = ['0000'];

    expect(pipe.transform(args, value)).toEqual(args)
  });
});
