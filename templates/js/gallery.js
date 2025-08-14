const images = document.querySelectorAll('.gallery img');
const viewer = document.createElement('div');
viewer.id = 'viewer';
viewer.innerHTML = '<img><div class="caption"></div>';
document.body.appendChild(viewer);

const viewerImg = viewer.querySelector('img');
const viewerCaption = viewer.querySelector('.caption');

images.forEach((img) => {
    img.addEventListener('click', () => {
        viewerImg.src = img.dataset.full;
        viewerCaption.textContent = img.dataset.desc || '';
        viewer.scrollIntoView({ behavior: 'smooth' });
    });
});
