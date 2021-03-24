$(document).ready(function () {
    $( ".table-form" ).click(function() {
        $(this).find("input").focus();
    });

    $('#id_form-0-image').change(function () {
        var file = $('#id_form-0-image')[0].files[0];
        $('#filename0').text(`New Image: ${file.name}`);
        $('#filename0').removeClass('text-transparent');
    });
    $('#id_form-1-image').change(function () {
        var file = $('#id_form-1-image')[0].files[0];
        $('#filename1').text(`New Image: ${file.name}`);
        $('#filename1').removeClass('text-transparent');
    });
    $('#id_form-2-image').change(function () {
        var file = $('#id_form-2-image')[0].files[0];
        $('#filename2').text(`New Image: ${file.name}`);
        $('#filename2').removeClass('text-transparent');
    });
    $('#id_form-3-image').change(function () {
        var file = $('#id_form-3-image')[0].files[0];
        $('#filename3').text(`New Image: ${file.name}`);
        $('#filename3').removeClass('text-transparent');
    });
    $('#id_form-4-image').change(function () {
        var file = $('#id_form-4-image')[0].files[0];
        $('#filename4').text(`New Image: ${file.name}`);
        $('#filename4').removeClass('text-transparent');
    });
    $('#id_form-5-image').change(function () {
        var file = $('#id_form-5-image')[0].files[0];
        $('#filename5').text(`New Image: ${file.name}`);
        $('#filename5').removeClass('text-transparent');
    });
    $('#id_form-6-image').change(function () {
        var file = $('#id_form-6-image')[0].files[0];
        $('#filename6').text(`New Image: ${file.name}`);
        $('#filename6').removeClass('text-transparent');
    });
});