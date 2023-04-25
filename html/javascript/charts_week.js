let all_humidity = [];
let humidity = [];

let all_temperatues = [];
let temperatures = [];

const fetchData2 = async () => {
    try {
        const res = await fetch("http://127.0.0.1:5000/");
        const data = await res.json();

        data.forEach(item => {
            all_humidity.push(item[3]);
        });

        humidity = all_humidity.slice(-7);

        data.forEach(item => {
            all_temperatues.push(item[2]);
        });

        temperatures = all_temperatues.slice(-7);

        // console.log(data);
        // console.log(all_humidity);
        console.log(`humidity_week_data ${humidity}`);
        console.log(humidity);

        const chart_week_humidity = document.getElementById("myChart2");
        const chart_week_temperature = document.getElementById("myChart");

        new Chart(chart_week_humidity, {
            type: 'bar',
            data: {
            labels: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
            datasets: [{
                label: 'RH %',
                data: humidity,
                borderWidth: 2,
                borderColor: 'red',
                backgroundColor: 'rgba(245, 0, 0, 0.52)'
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
        });

        new Chart(chart_week_temperature, {
            type: 'bar',
            data: {
            labels: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
            datasets: [{
                label: 'grades',
                data: temperatures,
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
        });
        
    } catch (error) {
        console.log(error);
    }
}

fetchData2()
