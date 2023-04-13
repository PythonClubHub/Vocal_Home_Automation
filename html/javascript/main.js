
let number = 10;

let btn_increase = document.getElementById("increase");
let btn_decrease = document.getElementById("decrease");

let counter = document.getElementById("counter");

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