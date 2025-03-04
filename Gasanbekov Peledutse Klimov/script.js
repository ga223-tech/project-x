// Функция для показа модального окна с биографией
function showBio(id) {
    const modal = document.getElementById(id);
    modal.style.display = "block";
    setTimeout(() => {
        modal.querySelector('.bio-modal-content').style.transform = "translateY(0)";
        modal.querySelector('.bio-modal-content').style.opacity = "1";
    }, 100); // Плавность анимации
}

// Функция для закрытия модального окна
function closeBio(id) {
    const modal = document.getElementById(id);
    modal.querySelector('.bio-modal-content').style.transform = "translateY(20px)";
    modal.querySelector('.bio-modal-content').style.opacity = "0";
    setTimeout(() => {
        modal.style.display = "none";
    }, 1); // Задержка для анимации
}
