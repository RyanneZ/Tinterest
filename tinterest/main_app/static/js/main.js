console.log("hello");

const categoryBtns = document.getElementsByClassName('category-btns');
const button = document.getElementsByClassName('category-button');

// for (i = 0; i<button.length; i++){
//   button[i].addEventListener('click', function(){
//     this.classList.toggle('active')
//   })
// }


const createdBtn = document.getElementById('created-btn');
const savedBtn = document.getElementById('saved-btn');
createdBtn.addEventListener('click', function(){
  if (createdBtn.classList.contains('active')) {
    createdBtn.classList.remove('active');
    console.log(1);
    savedBtn.classList.add('active');

  } else  {
    createdBtn.classList.add('active');
    console.log(2);

    savedBtn.classList.remove('active');
  }
})
console.log("hello");

savedBtn.addEventListener('click', function(){
  if (savedBtn.classList.contains('active')) {
    savedBtn.classList.remove('active');
    console.log(3);

    createdBtn.classList.add('active');
  } else {
    savedBtn.classList.add('active');
    console.log(4);

    createdBtn.classList.remove('active');
  }
})