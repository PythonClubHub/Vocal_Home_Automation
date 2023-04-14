
let all_temperatues = [];
let temperatures = [];
const test = [10,12,9,4,12,20,15];

const fetchData = async () => {
    try {
        const res = await fetch("http://127.0.0.1:5000/");
        const data = await res.json();

        data.forEach(item => {
            all_temperatues.push(item[3]);
        });

        temperatures = all_temperatues.slice(-7);

        console.log(data);
        console.log(all_temperatues);
        console.log(temperatures);

        const ctx = document.getElementById("myChart");

        new Chart(ctx, {
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

fetchData()

