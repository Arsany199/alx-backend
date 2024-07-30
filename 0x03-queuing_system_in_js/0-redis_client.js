import redis from 'redis';

const redisclient = redis.createClient();

redisclient.on('connect', () => {
  console.log('Redis client connected to the server');
});

redisclient.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error}`);
});
