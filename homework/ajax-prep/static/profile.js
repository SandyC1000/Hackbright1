function submitProfile(evt) {
  evt.preventDefault();

  const data = {
    name: document.querySelector('#name-field').value,
    // fill in the rest
    age:  document.querySelector('#age-field').value,
    occupation: document.querySelector('#occupation-field').value,
  };

  // make request to server to get the data
  // add the data the server returns to the document
  // (you can add it to the end of the div with ID "profiles")
  fetch('/api/profile', {
    method: 'POST',
    body: JSON.stringify(data),
    headers: {
      'Content-Type': 'application/json',
    },
  })
    .then(response => response.json())
    .then(jsonData => {
      document
        .querySelector('#profiles')
        .insertAdjacentHTML(
          'beforeend',
          `<li>${jsonData.fullname} the ${jsonData.occupation} is ${jsonData.age}</li>`
        );
      });
}

document.querySelector('#profile-form').addEventListener('submit', submitProfile);
