const { EmailClient, SmsGateway } = require('./channels');
const { alertOnCall } = require('./oncall');

const incident = { severity: 'P1', title: 'Checkout is down', details: 'Error rate 100% since 02:14' };

function setUp() {
  return { email: new EmailClient(), sms: new SmsGateway() };
}

describe('alertOnCall', () => {
  test('texts engineers who prefer SMS', () => {
    const { email, sms } = setUp();
    alertOnCall({ prefers: 'sms', phone: '07700900123' }, incident, email, sms);
    expect(sms.messages).toEqual([{ number: '07700900123', text: '[P1] Checkout is down' }]);
    expect(email.sent).toEqual([]);
  });

  test('emails everyone else', () => {
    const { email, sms } = setUp();
    alertOnCall({ prefers: 'email', email: 'ada@example.com' }, incident, email, sms);
    expect(email.sent).toEqual([
      { address: 'ada@example.com', subject: '[P1] Checkout is down', body: 'Error rate 100% since 02:14' },
    ]);
    expect(sms.messages).toEqual([]);
  });
});

describe('SmsGateway', () => {
  test('accepts a message of 160 characters', () => {
    const sms = new SmsGateway();
    sms.dispatch({ number: '07700900123', text: 'x'.repeat(160) });
    expect(sms.messages).toHaveLength(1);
  });

  test('rejects longer messages', () => {
    expect(() => new SmsGateway().dispatch({ number: '07700900123', text: 'x'.repeat(161) })).toThrow();
  });
});
