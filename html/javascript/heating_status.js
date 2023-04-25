const btn_on = document.getElementById("btn_on");
const btn_off = document.getElementById("btn_off");

let on = 1;
let off = 0;

let heating_status = 0;

// ----- fetch the status of the heating system -----------------------------
const fecth_status = async () => {
    try {
        const res2 = await fetch("http://127.0.0.1:5000/data");
        const data2 = await res2.json();

        console.log(data2);
        console.log(data2[0][1]);
        heating_status = data2[0][2];
        console.log(heating_status);

        if(heating_status == 1){
            console.log("on");
            btn_on.disabled = true;
            btn_on.style.backgroundColor = "#0dd15877";
            status_heating.textContent = 'The heating is ON';
        }

        if(heating_status == 0){
            console.log("off");
            btn_off.disabled = true;
            btn_off.style.backgroundColor = "#fb414480";
            status_heating.textContent = 'The heating is OFF';
        }

        counter.textContent = `${data2[0][1]} ° C `;

        
    } catch (error) {
        console.log(error);
    }
}

fecth_status();


// -------- turn ON the heating system and send the value to the database ------------------
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


// -------- turn OFF the heating system and send the value to the database ------------------
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