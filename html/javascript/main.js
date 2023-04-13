
let number = 10;

let btn_increase = document.getElementById("increase");
let btn_decrease = document.getElementById("decrease");

let counter = document.getElementById("counter");

// database
let db;
const request = indexedDB.open('data.db', 1)

request.onerror = (event) => {
    console.log('Database error: ' + event.target.errorCode);
}


request.onsuccess = (event) => {
    db = event.target.result;
}

btn_increase.addEventListener("click", () => {
    console.log("increase clicked!");
    number++;
    counter.innerHTML = number;

})

btn_decrease.addEventListener("click", () => {
    console.log("decrease clicked!");
    number--;
    counter.innerHTML = number;
})