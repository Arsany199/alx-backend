import { createClient, print } from 'redis';

const myclient = createClient();

myclient.hset("HolbertonSchools", "Portland", 50, print);
myclient.hset("HolbertonSchools", "Seattle", 80, print);
myclient.hset("HolbertonSchools", "New York", 20, print);
myclient.hset("HolbertonSchools", "Bogota", 20, print);
myclient.hset("HolbertonSchools", "Cali", 40, print);
myclient.hset("HolbertonSchools", "Paris", 2, print);

myclient.hgetall("HolbertonSchools", function(error, val) {
  console.log(val);
});
