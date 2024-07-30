import redis from 'redis';

const redisclient = redis.createClient();

redisclient.on('connect', () => {
  console.log('Redis client connected to the server');
});

redisclient.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error}`);
});

function setNewSchool(schoolName, value) {
  redisclient.set(schoolName, value, redis.print);
}

function displaySchoolValue(schoolName) {
  redisclient.get(schoolName, (error, reply) => {
    console.log(reply);
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
