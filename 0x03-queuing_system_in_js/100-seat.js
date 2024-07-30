import { createClient } from 'redis';
import { createQueue } from 'kue';
import { promisify } from 'util';
import express from 'express';

const app = express();
const client = createClient();
const queue = createQueue();
const host = 'localhost';
const port = 1245;
let reservationEnabled = true;

function reserveSeat(number) {
  client.set('available_seats', number);
}

async function getCurrentAvailableSeats() {
  const getasy = promisify(client.get).bind(client);
  const availableSeats = await getasy('available_seats');
  return Number(availableSeats);
}

app.get('/available_seats', async (req, res) => {
  const availableSeats = await getCurrentAvailableSeats();
  res.send({ numberOfAvailableSeats: availableSeats });
});

app.get('/reserve_seat', (_req, res) => {
  if (!reservationEnabled) {
    res.send({ status: 'Reservation are blocked' });
    return;
  }
  res.send({ status: 'Reservation in process' });
  const reserveSeatJob = queue.create('reserve_seat').save();
  reserveSeatJob.on('complete', () => {
    console.log(`Seat reservation job ${reserveSeatJob.id} completed`);
  });
  reserveSeatJob.on('failed', (errorMessage) => {
    console.log(`Seat reservation job ${reserveSeatJob.id} failed ${errorMessage}`);
  });
});

app.get('/process', (_req, res) => {
  queue.process('reserve_seat', async (_job, done) => {
    let availableSeats = await getCurrentAvailableSeats();
    if (!availableSeats) {
      done(new Error('Not enough seats available'));
      return;
    }
    availableSeats -= 1;
    reserveSeat(availableSeats);
    if (!availableSeats) reservationEnabled = false;
    done();
  });
  res.send({ status: 'Queue processing' });
});

app.listen(port, host, () => {
  console.log(`Server is live at ${host}:${port}`);
});
