window.addEventListener("scroll",function()
{
    var header = document.querySelector("header");
    header.classList.toggle("sticky",window.scrollY > 0);
})

////////////// POP UPS ////////////////////

var modal
var span = document.getElementsByClassName("close")[0];

function openPOPUP( num ){
	console.log("popup" + num.toString());
	modal = document.getElementsByClassName("popup" + num.toString())[0];
	console.log(modal)
	modal.style.display = "block";
}

function closePOPUP( num ){
	console.log("popup" + num.toString());
	modal = document.getElementsByClassName("popup" + num.toString())[0];
	console.log(modal)
	modal.style.display = "none";
}

// When the user clicks on the button, open the modal
// btn.onclick = function() {
//   modal.style.display = "block";
// }

// // When the user clicks on <span> (x), close the modal
// span.onclick = function() {
//   modal.style.display = "none";
// }

// // When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
	modal = document.getElementById("myModal");
  	if (event.target == modal) {
    modal.style.display = "none";
  }
}



