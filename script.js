function fetchNames(prefix) {
  fetch(`http://localhost:8080/students?q=${prefix}`)
    .then((resp) => resp.json())
    .then(addNames);
}

function addNames(names) {
  const ul = document.getElementById('name-list');
  while (ul.firstChild) {
      ul.removeChild(ul.firstChild);
  }
  for (let name of names) {
    const li = document.createElement('li');
    li.textContent = name;
    ul.appendChild(li);
  }
}

function setListener() {
  const inputEl = document.getElementById('dropdown-input');
  inputEl.addEventListener('input', () => {
    fetchNames(inputEl.value);
  });
}

window.onload = setListener;
