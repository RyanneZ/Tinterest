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
    savedBtn.classList.add('active');
  } else if (!(createdBtn.classList.contains('active'))) {
    createdBtn.classList.add('active');
    savedBtn.classList.remove('active');
  }
})

savedBtn.addEventListener('click', function(){
  if (savedBtn.classList.contains('active')) {
    savedBtn.classList.remove('active');
    createdBtn.classList.add('active');
  } else if (!(savedBtn.classList.contains('active'))) {
    savedBtn.classList.add('active');
    createdBtn.classList.remove('active');
  }
})