//for small screen menu
function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
}

function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
}

// for image changing
function carousel() {
    if (!document.getElementById("carousel")) {
        return;
    }
    const carouselImages = document.getElementById("carousel").attributes.data_images.value.split(",");
    const carouseDisplayImage = document.getElementById("carousel-display-image");

    let currentImageIndex = 0;

    carouseDisplayImage.src = carouselImages[currentImageIndex];

    setInterval(() => {
        carouseDisplayImage.src = carouselImages[currentImageIndex];
        currentImageIndex = (currentImageIndex + 1) % carouselImages.length;
    }
        , 3000);

    const leftArrow = document.getElementById("carousel-button-prev");
    const rightArrow = document.getElementById("carousel-button-next");

    leftArrow.addEventListener("click", () => {
        currentImageIndex = (currentImageIndex - 1 + carouselImages.length) % carouselImages.length;
        carouseDisplayImage.src = carouselImages[currentImageIndex];
    });

    rightArrow.addEventListener("click", () => {
        currentImageIndex = (currentImageIndex + 1) % carouselImages.length;
        carouseDisplayImage.src = carouselImages[currentImageIndex];
    });

}

document.addEventListener("DOMContentLoaded", () => {
    carousel();
});
