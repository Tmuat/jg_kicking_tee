// JS for Tiny-Slider Carousel in gallery section - from https://github.com/ganlanyuan/tiny-slider
$(document).ready(function () {
    var slider = tns({
        container: '.gallery-slider',
        loop: true,
        speed: 1000,
        items: 1,
        nav: false,
        mouseDrag: true,
        edgePadding: 20,
        controlsContainer: "#custom-controls",
        responsive: {
            640: {
                items: 1
            },
            700: {
                items: 1,
                edgePadding: 70,
            },
            1000: {
                edgePadding: 140,
            },
            1200: {
                edgePadding: 50,
                items: 2
            },
            1600: {
                edgePadding: 140,
            }
        }
    });
});


// https://www.steckinsights.com/change-active-menu-as-you-scroll-with-jquery/
$(document).ready(function () {
    $(window).scroll(function () {
        var Scroll = $(window).scrollTop() + 1,
            SectionOneOffset = $('#gallery').offset().top,
            SectionTwoOffset = $('#testimonials').offset().top;

        if (Scroll >= SectionOneOffset) {
            $(".menu-item-1").removeClass("active");
            $(".menu-item-2").addClass("active");
        } else {
            $(".menu-item-1").addClass("active");
            $(".menu-item-2").removeClass("active");
        }
        if (Scroll >= SectionTwoOffset) {
            $(".menu-item-1").removeClass("active");
            $(".menu-item-2").removeClass("active");
            $(".menu-item-3").addClass("active");
        } else {
            $(".menu-item-3").removeClass("active");
        }
    });
});
