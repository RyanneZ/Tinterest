console.log("hello");

const createdTrigger = document.getElementById("created-post-trigger");
const savedTrigger = document.getElementById("saved-post-trigger");

createdTrigger.addEventListener('click', function(){
  console.log("active")
    document.getElementById("saved-posts").style.display = "none";
    document.getElementById("created-posts").style.display = "block";
})
savedTrigger.addEventListener('click', function(){
  console.log("active again")
 
    document.getElementById("created-posts").style.display = "none";
    document.getElementById("saved-posts").style.display = "block"; 
})

// const categoryBtns = document.getElementsByClassName('category-btns');
// const button = document.getElementsByClassName('category-button');


// const createdBtn = document.getElementById('created-btn');
// const savedBtn = document.getElementById('saved-btn');
// createdBtn.addEventListener('click', function(){
//   if (createdBtn.classList.contains('active')) {
//     createdBtn.classList.remove('active');
//     console.log(1);
//     savedBtn.classList.add('active');

//   } else  {
//     createdBtn.classList.add('active');
//     console.log(2);

//     savedBtn.classList.remove('active');
//   }
// })
// console.log("hello");

// savedBtn.addEventListener('click', function(){
//   if (savedBtn.classList.contains('active')) {
//     savedBtn.classList.remove('active');
//     console.log(3);

//     createdBtn.classList.add('active');
//   } else {
//     savedBtn.classList.add('active');
//     console.log(4);

//     createdBtn.classList.remove('active');
//   }
// })
