class Channel {
  constructor(options = {}) {
    this.options = options;
  }

  beforeSend(message) {
    return message;
  }

  afterSend(receipt) {
    return receipt;
  }

  deliver() {
    throw new Error('Subclasses must implement deliver()');
  }

  send(message) {
    return this.afterSend(this.deliver(this.beforeSend(message)));
  }
}

class EmailChannel extends Channel {
  constructor(outbox, options = {}) {
    super(options);
    this.outbox = outbox;
  }

  deliver(message) {
    this.outbox.push({ to: message.recipient.email, body: message.text });
    return { channel: 'email', to: message.recipient.email };
  }
}

class Notifier {
  constructor(channels, { formatter = (text) => text } = {}) {
    this.channels = channels;
    this.formatter = formatter;
  }

  notify(recipient, text, metadata = {}) {
    if (!recipient.email) {
      throw new Error('Recipient has no email address');
    }
    const formatted = this.formatter(text, metadata);
    return this.channels.map((channel) => channel.send({ recipient, text: formatted }));
  }
}

module.exports = { Channel, EmailChannel, Notifier };
