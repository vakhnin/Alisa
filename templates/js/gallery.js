const images = document.querySelectorAll('.gallery img');
const viewer = document.querySelector('#viewer');
const viewerImg = viewer.querySelector('img');
const viewerCaption = viewer.querySelector('.caption');

function openImage(img) {
    images.forEach(i => i.classList.remove('active'));
    img.classList.add('active');

    viewerImg.src = img.dataset.full;
    viewerCaption.textContent = img.dataset.desc || '';

    viewer.scrollIntoView({ behavior: 'smooth' });
}

images.forEach((img) => {
    img.addEventListener('click', () => openImage(img));
});

if (images.length > 0) {
    openImage(images[0]);
}
