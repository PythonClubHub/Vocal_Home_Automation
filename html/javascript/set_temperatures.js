
// here we set the temperatures with the input and the buttons OK and SET

const ok_btn = document.getElementById("ok_btn"); // OK button
const btn_set = document.getElementById("btn_set"); // SET button
const input_temp = document.getElementById("input_temperatura"); // INPUT for to set the temperature

let temperature = 0  // this variable will store the value of the input

input_temp.addEventListener("change", () => {
    btn_set.style.backgroundColor = "#0274d8ba";
    btn_set.disabled = true;
})

// the event CLICK of the OK button
ok_btn.addEventListener("click", () => {
    temperature = parseInt(input_temp.value);
    console.log(temperature);
    btn_set.style.backgroundColor = "#0275d8";
    btn_set.disabled = false;
})


// the event CLICK of the SET button
btn_set.addEventListener("click", async (e) => {
    console.log("btn_set clicked!");

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
