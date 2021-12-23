const ALPHABET = 'abcdefghijklmnopqrstuvwxyz';

const WORDS = [
  'strawberry',
  'orange',
  'apple',
  'banana',
  'pineapple',
  'kiwi',
  'peach',
  'pecan',
  'eggplant',
  'durian',
  'peanut',
  'chocolate',
];

const numWrong = 0;

// Loop over the chars in `word` and create divs.xww
//

const createDivsForChars = word => {
  // Replace this with your code
  
for (char of word) {
  console.log(char);
  document.querySelector('#word-container')
  .insertAdjacentHTML('beforeend', `<div class="letter-box">${char}</div>`);
}

};

// Loop over each letter in the alphabet and generate a button
// for each letter
const button = document.querySelector('#letter-buttons');
const generateLetterButtons = () => {
  // Replace this with your code
for (letter of ALPHABET) {
  //console.log(letter) 
  document.querySelector('#letter-buttons')
  .insertAdjacentHTML('beforeend', `<button>${letter}</button>`);
}

};
button.addEventListener('click', generateLetterButtons)
// Set the `disabled` property of `buttonEl` to `true.
//
// `buttonEl` is an `HTMLElement` object.
//

const disableLetterButton = buttonEl => {
  // Replace this with your code
  //const document.getElementsByClassName("buttonEl").disabled = true;
};

// This is a helper function we will use in the future
// It should return `true` if `letter` is in the word
// For now, you should test it out to make sure it works
// catPhoto.getAttribute('src');


const isLetterInWord = letter => {
  // Replace this with your code
  const aLetter = document.querySelectorAll('#word-container')
  console.log(aLetter)
  for (l of aLetter) {
    return letter ===l;
  }
};

// This is like if __name__ == '__main__' in Python
// It will be called when the file is run (because
// we call the function on line 66)
(function startGame() {
  // For now, we'll hardcode the word that the user has to guess
  // You can change this to choose a random word from WORDS once you
  // finish this lab but we hard code it so we know what the word is
  // and can tell if things look correct for this word
  const word = 'hello';

  // call the function that makes an empty line for each letter in the word
  // Replace this line with the function call
  createDivsForChars(word)

  // call the function that makes a button for each letter in the alphabet
  // Replace this line with the function call
  generateLetterButtons()


  // in the next lab, you will be adding functionality to handle when
  // someone clicks on a letter
})();
