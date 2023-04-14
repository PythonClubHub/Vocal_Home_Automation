
let all_humidity = [];
let humidity = [];

const fetchData2 = async () => {
    try {
        const res = await fetch("http://127.0.0.1:5000/");
        const data = await res.json();

        data.forEach(item => {
            all_humidity.push(item[4]);
        });

        humidity = all_humidity.slice(-7);

        console.log(data);
        console.log(all_humidity);
        console.log(humidity);

        const ctx = document.getElementById("myChart2");

        new Chart(ctx, {
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
        
    } catch (error) {
        console.log(error);
    }
}

fetchData2()

