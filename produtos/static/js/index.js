
//nav mobile
const navButton = document.querySelector('.menu-button'); 
const navXButton = document.querySelector('.menu-X-button'); 
const navMobile = document.querySelector('.items-mobile'); 

navButton.addEventListener('click', () => {

    navMobile.classList.toggle('nav-change'); 

    setTimeout(() => {

        navButton.style.display = 'none'; 
        navXButton.style.display = 'block'; 

    }, 400)

})

navXButton.addEventListener('click', () => {

    navMobile.classList.toggle('nav-change'); 

    setTimeout(() => {

        navButton.style.display = 'block'; 
        navXButton.style.display = 'none'; 

    }, 400)

}); 

//opening time
const opening = document.querySelector('.opening'); 
const data = new Date(); 
const hour = data.getHours(); 
const day = data.getDay(); 

if ((hour >= 19 && day >= 1 && day < 7) || day === 7) {
    opening.innerHTML = 'Fechado (segunda a sábado 10:00 às 19:00)'; 
    opening.classList.toggle('closed'); 
} else if (hour >= 10 && hour < 19 && day >= 1 && day < 7) {
    opening.innerHTML = 'Aberto (segunda a sábado 10:00 às 19:00)'; 
    opening.classList.toggle('open');   
}