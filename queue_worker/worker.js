function randomLatency() {
  return new Promise((resolve) => setTimeout(resolve, Math.random() * 20));
}

class Worker {
  constructor(handler, latency = randomLatency) {
    this.handler = handler;
    this.latency = latency;
    this.done = [];
    this.failed = [];
  }

  async run(jobs) {
    for (const job of jobs) {
      await this.latency();
      try {
        await this.handler(job);
        this.done.push(job.id);
      } catch (error) {
        this.failed.push({ id: job.id, reason: error.message });
      }
    }
  }

  start(jobs) {
    this.running = this.run(jobs);
  }
}

module.exports = { Worker };
