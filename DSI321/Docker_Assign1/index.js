const express = require('express')
const app = express()


const PORT = process.env.PORT || 5000

currentDate = new Date();
startDate = new Date(currentDate.getFullYear(), 0, 1);
var days = Math.floor((currentDate - startDate) /
    (24 * 60 * 60 * 1000));
     
var weekNumber = Math.ceil(days / 7);

let date = {
    "day": currentDate.getDate(),
    "month": currentDate.getMonth()+1,
    "weekday": weekNumber,
    "year": currentDate.getFullYear()
  }
app.get('/', (req, res) => res.send('Hello World!'))
app.get('/date', (req, res) => res.json(date))

app.listen(PORT, () => {
    console.log(`Server is running on port : ${PORT}`)
})

//ทำการ export app ที่เราสร้างขึ้น เพื่อให้สามารถนำไปใช้งานใน project อื่นๆ 
//เปรียบเสมือนเป็น module ตัวนึง
module.exports = app