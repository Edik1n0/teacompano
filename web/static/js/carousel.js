var myCarousel = document.querySelector('#carouselExampleAutoplaying')
var carousel = new bootstrap.Carousel(myCarousel, {
  interval: 3000, // tiempo en milisegundos entre cada transición
  wrap: true // si se debe volver al primer elemento después del último
})