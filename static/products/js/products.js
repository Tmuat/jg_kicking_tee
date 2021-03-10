$(document).ready(function () {
    $("#thumbnail1").click(function () {
        if ($("#product_image1").hasClass("d-none")) {

            $("#product_image1").removeClass("d-none");
            $("#product_image2").addClass("d-none");
            $("#product_image3").addClass("d-none");
            $("#product_image4").addClass("d-none");

        };
    });
    $("#thumbnail2").click(function () {
        if ($("#product_image2").hasClass("d-none")) {

            $("#product_image2").removeClass("d-none");
            $("#product_image1").addClass("d-none");
            $("#product_image3").addClass("d-none");
            $("#product_image4").addClass("d-none");

        };
    });
    $("#thumbnail3").click(function () {
        if ($("#product_image3").hasClass("d-none")) {

            $("#product_image3").removeClass("d-none");
            $("#product_image1").addClass("d-none");
            $("#product_image2").addClass("d-none");
            $("#product_image4").addClass("d-none");

        };
    });
    $("#thumbnail4").click(function () {
        if ($("#product_image4").hasClass("d-none")) {

            $("#product_image4").removeClass("d-none");
            $("#product_image1").addClass("d-none");
            $("#product_image2").addClass("d-none");
            $("#product_image3").addClass("d-none");

        };
    }); 
});