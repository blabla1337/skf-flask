import { OrderBy } from "./order-by.pipe";

describe('LPadPipe', () => { // <----------------
  let pipe: OrderBy;

  beforeEach(() => {
    pipe = new OrderBy();
  });

  it('transforms "1" to "0001"', () => {
    let value: any = "1";
    let args: string[] = ['0000'];

    expect(pipe.transform(args, value)).toEqual(args)
  });
});