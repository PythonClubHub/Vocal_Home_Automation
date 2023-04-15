const btn_on = document.getElementById("btn_on");
const btn_off = document.getElementById("btn_off");

let on = 1;
let off = 0;

btn_on.addEventListener("click", async () => {
    console.log('on');

    const options = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },

        body: JSON.stringify({ on })
    }

    try {
        const res = await fetch("http://127.0.0.1:5000/turn_on", options);
        const data = await res.json();

        console.log(data);
        
    } catch (error) {
        console.log(error);
    }
})

btn_off.addEventListener("click", async () => {
    console.log('off');

    const options = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },

        body: JSON.stringify({ off })
    }

    try {
        const res = await fetch("http://127.0.0.1:5000/turn_off", options);
        const data = await res.json();

        console.log(data);
        
    } catch (error) {
        console.log(error);
    }
})