'use strict';

// PART 1: SHOW A FORTUNE

function showFortune(evt) {
  // TODO: get the fortune and show it in the #fortune-text div
  fetch('/fortune')
    .then(response => response.text())
    .then(responseData => {
      console.log('***inside /fortune');
      document.querySelector('#fortune-text').innerHTML = responseData;
    });
}

document.querySelector('#get-fortune-button').addEventListener('click', showFortune);

// PART 2: SHOW WEATHER

function showWeather(evt) {
  evt.preventDefault();

  const url = '/weather.json';
  const zipcode = document.querySelector('#zipcode-field').value;

  // TODO: request weather with that URL and show the forecast in #weather-info
  const button = document.querySelector('#zipcode-field');

  button.addEventListener('click', () => {
    // const queryString = new URLSearchParams({zipcode: 94110}).toString();
    // const url = `/weather.json?${queryString}`;
    const url = '/weather.json?94110';

    fetch(url)
      .then(response => response.json())
      .then(status => {
        console.log('weather-info');
        document.querySelector('#weather-info').innerHTML = status;
      });
  });
}

document.querySelector('#weather-form').addEventListener('submit', showWeather);

// PART 3: ORDER MELONS

function orderMelons(evt) {
  evt.preventDefault();

  // TODO: show the result message after your form
  // TODO: if the result code is ERROR, make it show up in red (see our CSS!)
}
document.querySelector('#order-form').addEventListener('submit', orderMelons);
