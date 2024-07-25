fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
  .then(response => response.json())
  .then(data => {
    const helloValue = document.querySelector('#hello');
    helloValue.textContent = data.hello;
  })
  .catch(error => console.error('Error:', error));