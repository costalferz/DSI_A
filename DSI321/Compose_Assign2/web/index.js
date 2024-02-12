const express = require('express');
const redis = require("redis");
const app = express();
const client = redis.createClient({
    host: 'redis',
    port: 6379
  });

client.on('error', err => {
    console.log('Error ' + err);
});

app.get('/redis', (req, res) => {
    client.incr('hits', (err, count) => {
        res.send(`Hello World! I have been seen ${count} times.\n`);
    });
});

app.get('/', (req, res) => {
    return res.send(`Hello World`);
});

app.listen(5000, () => {
    console.log(`Server is running on port : 5000`)
})

//ทำการ export app ที่เราสร้างขึ้น เพื่อให้สามารถนำไปใช้งานใน project อื่นๆ 
//เปรียบเสมือนเป็น module ตัวนึง
module.exports = app;

