class EmailClient {
  constructor() {
    this.sent = [];
  }

  sendEmail(address, subject, body) {
    this.sent.push({ address, subject, body });
  }
}

class SmsGateway {
  constructor() {
    this.messages = [];
  }

  dispatch({ number, text }) {
    if (text.length > 160) {
      throw new Error('SMS messages are limited to 160 characters');
    }
    this.messages.push({ number, text });
    return true;
  }
}

module.exports = { EmailClient, SmsGateway };
