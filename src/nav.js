//FUNCION PARA QUE APAREZCA Y DESAPAREZCA EL NAV PARA CELU, ADEMAS LE DA LA ANIMACIÓN
function myFunction() {
  var x = document.getElementById("myLinks");
  if (x.style.display === "flex") {
    x.style.display = "none";
  } else {
    x.style.display = "flex";
    x.className = "animate__animated animate__fadeIn";
  }
}

$(document).ready(function () {
  irArriba();
}); //Hacia arriba

function irArriba() {
  $(".ir-arriba").click(function () {
    $("body,html").animate({ scrollTop: "0px" }, 1000);
  });
  $(window).scroll(function () {
    if ($(this).scrollTop() > 0) {
      $(".ir-arriba").slideDown(600);
    } else {
      $(".ir-arriba").slideUp(600);
    }
  });
  $(".ir-abajo").click(function () {
    $("body,html").animate({ scrollTop: "1000px" }, 1000);
  });
}

/**
 * Array con las imagenes que se iran mostrando en la web
 */
var imagenes = new Array(
  "https://rammwiki.net/www/w/images/b/b8/RunesLogo1994.png",
  "https://rammwiki.net/www/w/images/9/9e/1994Logo_Fill.png",
  "https://rammwiki.net/www/w/images/0/0d/RammsteinNewspaperLogo.png",
  "https://rammwiki.net/www/w/images/b/b5/1995Logo.png",
  "https://rammwiki.net/www/w/images/a/aa/TrialByFireLogo.png",
  "https://rammwiki.net/www/w/images/d/d4/1994Logo_Outline.png",
  "https://rammwiki.net/www/w/images/3/39/2001Logo.png",
  "https://rammwiki.net/www/w/images/8/8b/5TrackDemoSpineLogo.png",
  "https://rammwiki.net/www/w/images/f/f1/2011logo.png",
  "https://rammwiki.net/www/w/images/8/82/2012logo.png"
);

/**
 * Funcion para cambiar la imagen
 */
function rotarImagenes() {
  // obtenemos un numero aleatorio entre 0 y la cantidad de imagenes que hay
  var index = Math.floor(Math.random() * imagenes.length);

  // cambiamos la imagen
  document.getElementById("imagen").src = imagenes[index];
  document.getElementById("imagen").animate(
    {
      opacity: [0, 0.5, 1],
      offset: [0, 0.5, 1], // Shorthand for [ 0, 0.8, 1 ]
      easing: ["ease-in", "ease-out"],
    },
    2000
  );
}

/**
 * Función que se ejecuta una vez cargada la página
 */
onload = function () {
  // Cargamos una imagen aleatoria
  rotarImagenes();

  // Indicamos que cada 5 segundos cambie la imagen
  setInterval(rotarImagenes, 15000);
};
