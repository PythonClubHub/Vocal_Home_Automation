 
let temp_data = [];
let humidity_data = [];

let temp_data_day = [];
let humidity_data_day = [];

let average_temp = 0;
let average_humidity = 0;

let average_temp_week = 0;
let average_humidity_week = 0;


const avg_temp = document.getElementById("avg_temp");
const avg_humidity = document.getElementById("avg_humidity");
const avg_temp_week = document.getElementById("avg_temp_week");
const avg_humidity_week = document.getElementById("avg_humidity_week");

// fetch the temperatures for the all day and make a average
 const fecthDate = async () => {
    try {

        const res = await fetch("http://127.0.0.1:5000/day_data");
        const data = await res.json();

        console.log(data);

        data.forEach(item => {
            temp_data_day.push(item[1]);
        });

        data.forEach(item => {
            humidity_data_day.push(item[2]);
        });

        // temp_data_day = temp_data_day.slice(-7);
        // humidity_data_day = humidity_data_day.slice(-7);

        console.log(temp_data_day);
        console.log(humidity_data_day);

        let i = 0;
        let j = 0;

        temp_data_day.forEach(temp => {
            average_temp = average_temp + temp;
            i++;
        });

        humidity_data_day.forEach(humidity => {
            average_humidity = average_humidity + humidity;
            j++;
        });

        average_temp = average_temp / i;
        average_temp = average_temp.toFixed(1);
        // console.log(average_temp);

        average_humidity = average_humidity / j;
        average_humidity = average_humidity.toFixed(1);
        // console.log(average_humidity);

        avg_temp.textContent = `${average_temp} ° C `;
        avg_humidity.textContent = `${average_humidity} %`
        
    } catch (error) {
        console.log(error);
    }
 }

 const fetchWeek = async () => {
    try {
        
        const res = await fetch("http://127.0.0.1:5000/week_data");
        const data = await res.json();

        data.forEach(item => {
            temp_data.push(item[0]);
        });

        data.forEach(item => {
            humidity_data.push(item[1]);
        });

        temp_data = temp_data.slice(-7);
        humidity_data = humidity_data.slice(-7);

        // console.log(temp_data);
        // console.log(humidity_data);

        temp_data.forEach(temp => {
            average_temp_week = average_temp_week + temp
        });

        // console.log(average_temp_week);

        humidity_data.forEach(humidity => {
            average_humidity_week = average_humidity_week + humidity
        });

        // console.log(average_humidity_week);

        average_temp_week = average_temp_week / 7;
        average_temp_week = average_temp_week.toFixed(1);
        // console.log(average_temp_week);

        average_humidity_week = average_humidity_week / 7;
        average_humidity_week = average_humidity_week.toFixed(1);
        // console.log(average_humidity_week);

        avg_temp_week.textContent = `${average_temp_week} ° C `;
        avg_humidity_week.textContent = `${average_humidity_week} %`

        // console.log(`Week = ${data}`);
        // console.log(data);
        
    } catch (error) {
        console.log(error);
    }
 }

 fecthDate();
 fetchWeek();