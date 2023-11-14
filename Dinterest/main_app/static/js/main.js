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