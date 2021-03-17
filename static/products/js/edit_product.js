$(document).ready(function () {
    $('.new-image').closest('.inline-formset').nextAll('.inline-formset').find('.new-image').removeClass('new-image').addClass('new-image2');
    $('.new-image2').closest('.inline-formset').nextAll('.inline-formset').find('.new-image2').removeClass('new-image2').addClass('new-image3');
    $('.new-image3').closest('.inline-formset').nextAll('.inline-formset').find('.new-image3').removeClass('new-image2').addClass('new-image4');

    $('.new-image').closest('.inline-formset').nextAll('.inline-formset').find('.filename').removeClass('filename').addClass('filename2');
    $('.new-image2').closest('.inline-formset').nextAll('.inline-formset').find('.filename2').removeClass('filename2').addClass('filename3');
    $('.new-image3').closest('.inline-formset').nextAll('.inline-formset').find('.filename3').removeClass('filename2').addClass('filename4');

    $('.new-image').change(function () {
        var file = $('.new-image')[0].files[0];
        $('.filename').text(`New Image: ${file.name}`);
    });
    $('.new-image2').change(function () {
        var file = $('.new-image2')[0].files[0];
        $('.filename2').text(`New Image: ${file.name}`);
    });
    $('.new-image3').change(function () {
        var file = $('.new-image3')[0].files[0];
        $('.filename3').text(`New Image: ${file.name}`);
    });
    $('.new-image4').change(function () {
        var file = $('.new-image4')[0].files[0];
        $('.filename4').text(`New Image: ${file.name}`);
    });
});