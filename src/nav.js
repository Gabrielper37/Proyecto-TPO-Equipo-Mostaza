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