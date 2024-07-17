function login() {
    var username = document.querySelector('.input-field[placeholder="Username or Email"]').value;
    var password = document.querySelector('.input-field[placeholder="Password"]').value;

    // Enviar datos al backend
    fetch('/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ username: username, password: password })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert(data.message);  // Mensaje de éxito
            window.location.href = "{{ url_for('home') }}";  // Redirigir a la página de inicio
        } else {
            alert(data.message);  // Mensaje de error
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}


//**********metodo para consumir api ***************/

fetch('https://www.themealdb.com/api/json/v1/1/categories.php')

.then(response => response.json())

.then(data => {

  const tableBody = document.getElementById('tableBody');

  console.log(data);

  data.categories.forEach(categories => {

    const row = `<tr>

            <td>${categories.idCategory}</td>

            <td>${categories.strCategory}</td>

            <td>${categories.strCategoryThumb}</td>

            <td>${categories.strCategoryDescription}</td>

           </tr>`;

    tableBody.innerHTML += row;

  });

})

.catch(error => console.error('Error al consumir la API:', error));


