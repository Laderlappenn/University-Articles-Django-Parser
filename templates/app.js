const crModal = document.querySelector(".cr__outer");
const crOpen = document.querySelector(".cr-btn");

crOpen.addEventListener("click", () => {
    crModal.style.opacity = 1;
    crModal.style.visibility = 'visible';
    crModal.style.pointerEvents = 'all';
});

crModal.addEventListener('click', (e) => {
    if(e.target === crModal) {
        crModal.style.opacity = 0;
        crModal.style.visibility = 'hidden';
        crModal.style.pointerEvents = 'none';
    }
})