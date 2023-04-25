
const counter = document.getElementById("counter");
const temp_text = document.getElementById("temp_text");
const humidity_text = document.getElementById("humidity_text");

const status_heating = document.getElementById("status_heating");

const fecth_setTemperature = async () => {
    try {

        const res = await fetch("http://127.0.0.1:5000/temperature");
        const data = await res.json();

        console.log(data);
        let lastElement = data[data.length - 1];
        console.log(`last = ${lastElement}`);

        temp_text.textContent = `${lastElement[2]} ° C `;
        humidity_text.textContent = `${lastElement[3]} %`;

        // here we have 2 condicionals to control the status of the heating system
        // if we comment this 2 IFs, we can control the heating system with the Turn On and Turn Off buttons
        if(lastElement[2] > 20){
            console.log('off');
            heating_status = 0

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
        }

        if(lastElement[2] <= 20){
            console.log('on');
            heating_status = 1  

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
        }

        // ---------------------------------------------------------
  
    } catch (error) {
        console.log(error);
    }
}

fecth_setTemperature()