window.onload(veificalog())
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