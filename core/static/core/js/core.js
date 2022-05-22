// const btn = document.getElementById("btn-form");
// btn.addEventListener('click', function (e) {
//     e.preventDefault()
//     console.log("form submitted");
// });
const print=console.log

const seletCity = document.querySelectorAll("#select-btn");
for (let button of seletCity) {
    button.addEventListener('click', function (e) {
        e.preventDefault()
        console.log(this.textContent);
        const a = document.getElementById('select-city');
        a.textContent=this.textContent
        

        
    });
}
