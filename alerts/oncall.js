function alertOnCall(engineer, incident, emailClient, smsGateway) {
  const headline = `[${incident.severity}] ${incident.title}`;
  if (engineer.prefers === 'sms') {
    smsGateway.dispatch({ number: engineer.phone, text: headline });
  } else {
    emailClient.sendEmail(engineer.email, headline, incident.details);
  }
}

module.exports = { alertOnCall };
