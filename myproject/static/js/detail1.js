document.addEventListener("DOMContentLoaded",function(){
    window.onload = function(){
        const scrollList=document.querySelector('.ull');
        const items = Array.from(scrollList.children);
        items.reverse().forEach(item => scrollList.appendChild(item));
    };
    });
