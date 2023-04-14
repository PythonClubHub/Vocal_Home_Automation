const btn_press = document.getElementById("btn_press");
const container_data = document.getElementById("container_data");
const fragment = document.createDocumentFragment();

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