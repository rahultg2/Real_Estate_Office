window.addEventListener("scroll",function()
{
    var header = document.querySelector("header");
    header.classList.toggle("sticky",window.scrollY > 0);
})

var modal = document.getElementById("myModal");
var btn = document.getElementById("myBtn");
var span = document.getElementsByClassName("close")[0];
btn.onclick = function() 
{
    modal.style.display = "block";
}
span.onclick = function() 
{
    modal.style.display = "none";
}
window.onclick = function(event) 
{
    if (event.target == modal) 
    {
        modal.style.display = "none";
    }
}



$('#myModal').on('shown.bs.modal', function () {
  $('#myInput').trigger('focus')
})

// update stauts js

// function changeStatus( num ){
// 	console.log("popup" + num.toString());
// 	modal = document.getElementsByClassName("popup" + num.toString())[0];
// 	console.log(modal)
// 	modal.style.display = "block";
// }