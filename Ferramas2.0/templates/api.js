//**********metodo para consumir api ***************/

fetch('http://127.0.0.1:5000/tools')

.then(response => response.json())

.then(data => {

  const tableBody = document.getElementById('tableBody');

  console.log(data);

  data.forEach(categories => {

    const row = `<tr>

            <td>${categories.ID}</td>

            <td>${categories.Nombre}</td>

            <td>${categories.Precio}</td>

            <td>${categories.Stock}</td>

           </tr>`;

    tableBody.innerHTML += row;

  });

})

.catch(error => console.error('Error al consumir la API:', error));