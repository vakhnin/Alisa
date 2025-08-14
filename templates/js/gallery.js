const images = document.querySelectorAll('.gallery img');
const viewer = document.createElement('div');
viewer.id = 'viewer';
viewer.innerHTML = '<img><div class="caption"></div>';
document.body.appendChild(viewer);

const viewerImg = viewer.querySelector('img');
const viewerCaption = viewer.querySelector('.caption');

function openImage(img) {
    // Убираем выделение со всех
    images.forEach(i => i.classList.remove('active'));

    // Добавляем выделение текущей
    img.classList.add('active');

    // Меняем изображение в просмотрщике
    viewerImg.src = img.dataset.full;
    viewerCaption.textContent = img.dataset.desc || '';

    // Скроллим к просмотровому блоку
    viewer.scrollIntoView({ behavior: 'smooth' });
}

images.forEach((img) => {
    img.addEventListener('click', () => openImage(img));
});

// Открыть первую картинку при загрузке страницы
if (images.length > 0) {
    openImage(images[0]);
}
