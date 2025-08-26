const box = document.querySelectorAll(".box")
const b0 = document.getElementById("b0")
const b1 = document.getElementById("b1")
const b2 = document.getElementById("b2")
const b3 = document.getElementById("b3")
const b4 = document.getElementById("b4")
const b5 = document.getElementById("b5")
const b6 = document.getElementById("b6")

userChoice = document.getElementsByClassName("userChoice")
compChoice = document.getElementsByClassName("compChoice")

scoreShow = document.getElementsByClassName("score")

let thisChoice;

b0.addEventListener('click', () => {
    thisChoice = b0.innerText
})
b1.addEventListener('click', () => {
    thisChoice = b1.innerText
})
b2.addEventListener('click', () => {
    thisChoice = b2.innerText
})
b3.addEventListener('click', () => {
    thisChoice = b3.innerText
})
b4.addEventListener('click', () => {
    thisChoice = b4.innerText
})
b5.addEventListener('click', () => {
    thisChoice = b5.innerText
})
b6.addEventListener('click', () => {
    thisChoice = b6.innerText
})

function main(choice){

}