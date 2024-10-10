document.addEventListener("DOMContentLoaded",function(){


let togglebtn = document.querySelector(".toggle-menu");
let tlinks = document.querySelector(".link");

togglebtn.onclick = function(e){
    e.stopPropagation();
    this.classList.toggle("menu-active");
    tlinks.classList.toggle("open");
};


document.addEventListener("click", (e)=> {
    if(e.target !== togglebtn && e.target !== tlinks){
        if(tlinks.classList.contains("open")){
            togglebtn.classList.toggle("menu-active");
            tlinks.classList.toggle("open");
        }
    }
});

tlinks.onclick = function (e){
    e.stopPropagation();
}
});
