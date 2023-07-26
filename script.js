const polygons = document.querySelectorAll('.cls-1');

function animatePolygons() {
  polygons.forEach((polygon, index) => {
    polygon.style.animationDelay = `${index * 0.5}s`;
  });
}

animatePolygons();