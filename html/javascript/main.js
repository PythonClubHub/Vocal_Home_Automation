const btn_press = document.getElementById("btn_press");
const container_data = document.getElementById("container_data");
const fragment = document.createDocumentFragment();

const counter = document.getElementById("counter");
const temp_text = document.getElementById("temp_text");
const status_heating = document.getElementById("status_heating");

const fecth_setTemperature = async () => {
    try {

        const res = await fetch("http://127.0.0.1:5000/");
        const data = await res.json();

        console.log(data);
        let lastElement = data[data.length - 1];
        console.log(lastElement);

        temp_text.textContent = `${lastElement[3]} ° C `;

        const res2 = await fetch("http://127.0.0.1:5000/data");
        const data2 = await res2.json();

        console.log(data2);
        console.log(data2[0][1]);
        let status = data2[0][2];
        console.log(status);

        if(status == 1){
            status_heating.textContent = 'The heating is ON';
        }

        if(status == 0){
            status_heating.textContent = 'The heating is OFF';
        }

        counter.textContent = `${data2[0][1]} ° C `;
        
    } catch (error) {
        console.log(error);
    }
}

fecth_setTemperature()

btn_press.addEventListener('click', async () => {
    
    try {
        const res = await fetch('http://127.0.0.1:5000/');
        const data = await res.json()
        console.log(data);

        data.forEach(item => {
            const p = document.createElement('p');
            p.textContent = `In ${item[1]} at ${item[2]} was ${item[3]} grades and ${item[4]} humidity`;
            fragment.appendChild(p);
        });

        container_data.appendChild(fragment)
        
    } catch (error) {
        console.log(error);
    }

})