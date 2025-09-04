$(document).ready(function () {
    const $gallery = $('.gallery');
    let allItems = $gallery.children().toArray();
    const $viewer = $('#viewer');
    const $viewerImg = $('#viewer img');
    const $viewerCaption = $('#viewer .caption');
    const maxVisible = 7;

    // Функция для добавления описания к миниатюрам
    function addCaptions() {
        $gallery.find('.gallery-item').each(function () {
            const $img = $(this).find('img');
            const desc = $img.data('desc') || 'Описание отсутствует'; // Берём описание из data-desc
            if (!$(this).find('.thumb-caption').length) {
                $(this).append(`<div class="thumb-caption">${desc}</div>`); // Добавляем описание
            }
        });
    }

    function getVisibleSet(centerIndex) {
        const len = allItems.length;
        const half = Math.floor(maxVisible / 2);
        let visible = [];

        for (let i = -half; i <= half; i++) {
            visible.push(allItems[(centerIndex + i + len) % len]);
        }
        return visible;
    }

    function renderGallery(visibleItems) {
        $gallery.empty().append(visibleItems);
        addCaptions(); // Добавляем описания после рендера
    }

    function openImage($img) {
        const index = allItems.indexOf($img.closest('.gallery-item')[0]);
        const visibleSet = getVisibleSet(index);

        $gallery.find('img').removeClass('active');
        $img.addClass('active');

        renderGallery(visibleSet);
        $viewerImg.attr('src', $img.data('full'));
        $viewerCaption.text($img.data('desc') || '');
    }

    $gallery.on('click', 'img', function () {
        openImage($(this));
    });

    // Открываем первую картинку
    if (allItems.length > 0) {
        openImage($(allItems[0]).find('img'));
    }
});
