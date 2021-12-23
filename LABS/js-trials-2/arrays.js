'use strict';

// 1. printIndices
function printIndices(items) {
  for (let i = 0; i < items.length; i += 1) {
    console.log(`${items[i]} ${i}`);
  }
}

// for (const index in items) <-- How to get index
// for (const item of items) <-- How to get value

// 2. everyOtherItem
function everyOtherItem(items) {
  const result = [];
  for (const i in items) {
    if (i % 2 == 0) {
      result.push(items[i]);
    } 
  }
  console.log(result);   
}


// 3. smallestNItems
function smallestNItems(items, n) {
  const sorted_items = items.sort((a, b) => a - b);
  const sorted_n_items = sorted_items.slice(0, n);
  console.log(sorted_n_items.reverse());
}
