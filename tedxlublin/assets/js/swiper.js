  var swiper = new Swiper('.swiper', {
    slidesPerView: 1,
    spaceBetween: 25,
    pagination: {
      el: '.swiper-pagination',
      clickable: true,
    },
    breakpoints: {
      1200: {
        slidesPerView: 4,
      },
      992: {
        slidesPerView: 3,
      },
      576: {
        slidesPerView: 2,
      },
    },
  });