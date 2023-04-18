let temp_day = [];
let humidity_day = [];

const btn_day = document.getElementById("btn_day");
const btn_week = document.getElementById("btn_week");

const week_data = document.getElementById("week_data");
const day_data = document.getElementById("day_data");

btn_day.addEventListener("click", () => {
    console.log("day");

    week_data.style.display = 'none';
    day_data.style.display = 'block';
})

btn_week.addEventListener("click", () => {
    console.log("week");

    week_data.style.display = 'block';
    day_data.style.display = 'none';
})

const fecthDayData = async () => {
    try {

        const res = await fetch("http://127.0.0.1:5000/day_data");
        const data = await res.json()

        console.log(data);

        data.forEach(temp => {
            temp_day.push(temp[1]);
            humidity_day.push(temp[2]);
        });

        console.log(temp_day);

        const ctx = document.getElementById("myChart3");
        const ctxHumidity = document.getElementById("myChart4");

        new Chart(ctxHumidity, {
            type: 'bar',
            data: {
            labels: ['8:00', '10:00', '12:00', '14:00', '16:00', '18:00', '20:00'],
            datasets: [{
                label: 'humidity',
                data: humidity_day,
                borderWidth: 2,
                backgroundColor: 'rgba(245, 0, 0, 0.52)',
                borderColor: 'red'
            }]
            },
            options: {
            responsive: true,
            scales: {
                y: {
                beginAtZero: true
                }
            }
            }
        })

        new Chart(ctx, {
            type: 'bar',
            data: {
            labels: ['8:00', '10:00', '12:00', '14:00', '16:00', '18:00', '20:00'],
            datasets: [{
                label: 'grades',
                data: temp_day,
                borderWidth: 2
            }]
            },
            options: {
            responsive: true,
            scales: {
                y: {
                beginAtZero: true
                }
            }
            }
        })
        
    } catch (error) {
        console.log(error);
    }
}

fecthDayData()