document.addEventListener("DOMContentLoaded", function() {
    var currentIndex = 0;
    var images = document.querySelectorAll("#images img");
    var prevButton = document.getElementById("prev");
    var nextButton = document.getElementById("next");
    var interval = 3000; // Interval de timp în milisecunde

    function showImage(index) {
        images.forEach((img, i) => {
            img.style.display = i === index ? 'block' : 'none';
        });
        currentIndex = index;
    }

    prevButton.addEventListener("click", function() {
        var newIndex = currentIndex - 1;
        if (newIndex < 0) newIndex = images.length - 1;
        showImage(newIndex);
    });

    nextButton.addEventListener("click", function() {
        var newIndex = currentIndex + 1;
        if (newIndex >= images.length) newIndex = 0;
        showImage(newIndex);
    });

    function autoSlide() {
        var newIndex = (currentIndex + 1) % images.length;
        showImage(newIndex);
    }

    var slideInterval = setInterval(autoSlide, interval);

    // Opriți sliderul automat la hover
    document.getElementById("imageSlider").addEventListener("mouseover", function() {
        clearInterval(slideInterval);
    });

    document.getElementById("imageSlider").addEventListener("mouseout", function() {
        slideInterval = setInterval(autoSlide, interval);
    });
});
