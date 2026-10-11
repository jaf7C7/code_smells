const { EmailChannel, Notifier } = require('./notifier');

const ada = { name: 'Ada', email: 'ada@example.com' };

function setUp() {
  const outbox = [];
  const notifier = new Notifier([new EmailChannel(outbox)]);
  return { outbox, notifier };
}

describe('Notifier', () => {
  test('emails the recipient', () => {
    const { outbox, notifier } = setUp();
    notifier.notify(ada, 'Your order has shipped');
    expect(outbox).toEqual([{ to: 'ada@example.com', body: 'Your order has shipped' }]);
  });

  test('returns a receipt for each delivery', () => {
    const { notifier } = setUp();
    expect(notifier.notify(ada, 'Hello')).toEqual([{ channel: 'email', to: 'ada@example.com' }]);
  });

  test('refuses recipients without an email address', () => {
    const { outbox, notifier } = setUp();
    expect(() => notifier.notify({ name: 'Alan' }, 'Hello')).toThrow('Recipient has no email address');
    expect(outbox).toEqual([]);
  });
});
