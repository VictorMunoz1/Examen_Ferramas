document.addEventListener('DOMContentLoaded', function() {
    const botonFlotante = document.getElementById('boton-flotante');
    const datosOcultos = document.getElementById('datos-ocultos');

    // Ocultar los datos ocultos al cargar la página
    datosOcultos.style.display = 'none';

    botonFlotante.addEventListener('click', function() {
        if (datosOcultos.style.display === 'none') {
            datosOcultos.style.display = 'block';
        } else {
            datosOcultos.style.display = 'none';
        }
    });
});
