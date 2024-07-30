import redis from 'redis';
import { promisify } from 'util';

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

async function displaySchoolValue(schoolName) {
  const getasy = promisify(redisclient.get).bind(redisclient);
  const val = await getasy(schoolName)
    console.log(val);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
