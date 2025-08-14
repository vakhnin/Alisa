$(document).ready(function () {
    const $images = $('.gallery img');
    const $viewer = $('#viewer');
    const $viewerImg = $('#viewer img');
    const $viewerCaption = $('#viewer .caption');

    function openImage($img) {
        // Снимаем выделение со всех миниатюр
        $images.removeClass('active');

        // Выделяем текущую
        $img.addClass('active');

        // Задаём картинку и подпись
        $viewerImg.attr('src', $img.data('full'));
        $viewerCaption.text($img.data('desc') || '');
    }

    // Обработчик клика по миниатюрам
    $images.on('click', function () {
        openImage($(this));
    });

    // Открываем первую картинку при загрузке
    if ($images.length > 0) {
        openImage($images.first());
    }
});
