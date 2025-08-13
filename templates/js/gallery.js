const images = document.querySelectorAll('.gallery img');
let currentIndex = -1;

function openOverlay(index) {
    currentIndex = index;
    const img = images[index];
    const overlay = document.createElement('div');
    overlay.className = 'overlay';
    overlay.innerHTML = `
        <img src="${img.dataset.full}" alt="">
        <div class="caption">${img.dataset.desc || ''}</div>
    `;
    overlay.addEventListener('click', e => {
        if (e.target === overlay) closeOverlay();
    });
    document.body.appendChild(overlay);

    document.addEventListener('keydown', keyHandler);
}

function closeOverlay() {
    document.querySelector('.overlay')?.remove();
    document.removeEventListener('keydown', keyHandler);
}

function keyHandler(e) {
    if (e.key === 'Escape') closeOverlay();
    else if (e.key === 'ArrowRight') navigate(1);
    else if (e.key === 'ArrowLeft') navigate(-1);
}

function navigate(dir) {
    let newIndex = currentIndex + dir;
    if (newIndex < 0) newIndex = images.length - 1;
    if (newIndex >= images.length) newIndex = 0;
    closeOverlay();
    openOverlay(newIndex);
}

images.forEach((img, idx) => {
    img.addEventListener('click', () => openOverlay(idx));
});
