const { Worker } = require('./worker');

function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

const jobs = [{ id: 1 }, { id: 2 }, { id: 3 }];

describe('Worker', () => {
  test('processes jobs in order', async () => {
    const seen = [];
    const worker = new Worker((job) => seen.push(job.id));
    await worker.run(jobs);
    expect(seen).toEqual([1, 2, 3]);
    expect(worker.done).toEqual([1, 2, 3]);
  });

  test('records failed jobs and carries on', async () => {
    const worker = new Worker((job) => {
      if (job.id === 2) throw new Error('bad payload');
    });
    await worker.run(jobs);
    expect(worker.done).toEqual([1, 3]);
    expect(worker.failed).toEqual([{ id: 2, reason: 'bad payload' }]);
  });

  test('works through the queue in the background', async () => {
    const worker = new Worker(() => {});
    worker.start(jobs);
    await sleep(30);
    expect(worker.done).toEqual([1, 2, 3]);
  });
});
