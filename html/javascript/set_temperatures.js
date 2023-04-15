
const set = document.getElementById("set");
const ok_btn = document.getElementById("ok_btn");

const temperatura = document.getElementById("temperatura");


let temperature = 0


ok_btn.addEventListener("click", () => {
    temperature = parseInt(temperatura.value);
    console.log(temperature);
})

set.addEventListener("click", async (e) => {
    console.log("set clicked!");

    counter.innerHTML = temperature;

    const options = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },

        body: JSON.stringify({ temperature })
    }

    try {
        const res = await fetch("http://127.0.0.1:5000/update_temperature", options);
        const data = await res.json();

        console.log(data);
        
    } catch (error) {
        console.log(error);
    }
})
