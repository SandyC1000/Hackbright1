'use strict';
/** ====== Functions and Event Handlers */

function changeColor() {
  const colorChangeEls = document.querySelectorAll('.color-change');
  for (const el of colorChangeEls) {
      el.classList.add('red');
  }
}

function validateNumber(evt) {
    evt.preventDefault();
    const numberInput = document.querySelector('input[name="number]');
    const userNum = Number(numberInput.value);
    const formFeedback = document.querySelector('#formFeedback');
    if (!userNum || userNum >= 10) {
        formFeedback.innerText = 'Please enter smaller number';
    } else {
        formFeedback.innerText = 'You are ready to go. ';
    }
}
/** =====Event Handlers */
document.querySelector('.color-changer').addEventListener('click', changeColor);
document.querySelector('.number-form').addEventListener('submit',validateNumber);