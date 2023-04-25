
const temp_text = document.getElementById("temp_text");
const humidity_text = document.getElementById("humidity_text");

const fetch_setTemperature = async () => {
    try {

        const res = await fetch("http://127.0.0.1:5000/temperature");
        const data = await res.json();

        console.log(data);
        let lastElement = data[data.length - 1];
        console.log(`last = ${lastElement}`);

        temp_text.textContent = `${lastElement[2]} ° C `;
        humidity_text.textContent = `${lastElement[3]} %`;
        
    } catch (error) {
        console.log(error);
    }
}

fetch_setTemperature()
