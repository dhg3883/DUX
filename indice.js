window.onload(veificalog())
function menu(params) {
    div=document.getElementById("menu")
    if(params){
    menutag='<nav class="navbar sticky-top navbar-expand-lg fixed-top">'+
        '<div class="container-fluid">'+
          '<a class="navbar-brand" href="#">DUX</a>'+
          '<button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">'+
            '<span class="navbar-toggler-icon"></span>'+
          '</button>'+
          '<div class="collapse navbar-collapse" id="navbarNav">'+
            '<ul class="navbar-nav">'+
              '<li class="nav-item">'+
                '<a class="nav-link activ" aria-current="page" href="#">Inicio</a>'+
              '</li>'+

              '<li class="nav-item">'+
                '<a class="nav-link" href="archivopaginawebproducto" >Guias</a>'+
              '</li>'+
            '<li class="nav-item">'+
            '<button class="btn" onclick="cerrar()">Cerrar Sesion</button>'+
          '</li>'+
            '</ul>'+
          '</div>'+
        '</div>'+
      '</nav>'
    }else{
    menutag='<nav class="navbar sticky-top navbar-expand-lg fixed-top">'+
        '<div class="container-fluid">'+
          '<a class="navbar-brand" href="#">DUX</a>'+
          '<button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">'+
            '<span class="navbar-toggler-icon"></span>'+
          '</button>'+
          '<div class="collapse navbar-collapse" id="navbarNav">'+
            '<ul class="navbar-nav">'+
              '<li class="nav-item">'+
                '<a class="nav-link activ" aria-current="page" href="#">Inicio</a>'+
              '</li>'+

              '<li class="nav-item">'+
                '<a class="nav-link" href="archivopaginawebproducto">Guias</a>'+
              '</li>'+

              '<li class="nav-item">'+
              '<a class="nav-link" href="Login">Iniciar Sesion</a>'+
            '</li>'+
            '</ul>'+
          '</div>'+
        '</div>'+
      '</nav>'}
    div.innerHTML=menutag
}
function veificalog() {
    const storedUserData = localStorage.getItem('clientelogueado')
    if (storedUserData) {
        const userData = JSON.parse(storedUserData)
        console.log(userData);
        document.getElementById("user").innerHTML= userData[0].NOMBRE
        menu(true)
    } else {
    ('User data not found in local storage')
    menu(false)
    }


}
function cerrar() {
    alert("adios")
    const storedUserData = localStorage.getItem('clientelogueado')

    if (storedUserData) {
        const userData = JSON.parse(storedUserData)
        console.log(userData);
        localStorage.removeItem('clientelogueado')
        location.replace("/")}
}