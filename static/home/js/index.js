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
