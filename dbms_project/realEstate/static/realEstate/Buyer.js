{/* <div class="input-group">
  <div class="form-outline">
    <input id="search-input" type="search" id="form1" class="form-control" />
    <label class="form-label" for="form1">Search</label>
  </div>
  <button id="search-button" type="button" class="btn btn-primary">
    <i class="fas fa-search"></i>
  </button>
</div> */}



// const formSignIn = document.querySelector('.form-signin');

// // <----------------------------------------------->
// /* <!-----~----SIGN IN POP UP!-----~~~~~------------>
// <!-----------------------------------------------> */
// const signinBtn = document.querySelector('.clickable-btn-sign-in').addEventListener('click', function(e){
//   let displayShow = document.querySelector('.displayShow');
//   let signinWrapper = document.querySelector('.sign-wrapper');
//   let signinDiv = document.querySelector('.sign-in-div');
  
//   // console.log('clicked');
//   signinDiv.classList.remove("sign-wrapper");
//   signinDiv.classList.add("displayShow");

//   e.preventDefault();
// });



// // ------remove--------

// window.addEventListener('click', function(event){
//   let displayShow = document.querySelector('.displayShow');
//   let signinWrapper = document.querySelector('.sign-wrapper');
//   let signinDiv = document.querySelector('.sign-in-div');

//   if(event.target === displayShow){
//     signinDiv.classList.remove("displayShow");
//     signinDiv.classList.add("sign-wrapper");
    
//   }
// });

//////////////////////// SLIDER //////////////////////////

// var slider = document.getElementById("myRange");
// var output = document.getElementById("demo");
// output.innerHTML = slider.value;

// slider.oninput = function() {
//   output.innerHTML = this.value;
// }


/////////////////////// POP-UPS ///////////////////////////

// var modal1 = document.getElementById("myModal");
// var modal = document.getElementsByClassName("popup1")[0];

// Get the button that opens the modal
// var btn1 = document.getElementById("myBtn");
// var btn = document.getElementsByClassName("card1")[0];
// Get the <span> element that closes the modal
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

///////////////////////////// SLIDER //////////////////////////

function getVals()
{
  // Get slider values
	var parent = this.parentNode;
	var slides = parent.getElementsByTagName("input");
	var slide1 = parseFloat(slides[0].value);
	var slide2 = parseFloat(slides[1].value);
	// Neither slider will clip the other, so make sure we determine which is larger
	
	if( slide1 > slide2 )
	{ 
		var tmp = slide2; slide2 = slide1; slide1 = tmp; 
	}

	var displayElement = parent.getElementsByClassName("rangeValues")[0];
	displayElement.innerHTML = "$ " + slide1 + "k - $" + slide2 + "k";
}

window.onload = function()
{
  // Initialize Sliders
  	var sliderSections = document.getElementsByClassName("range-slider");
		for( var x = 0; x < sliderSections.length; x++ )
		{
			var sliders = sliderSections[x].getElementsByTagName("input");
			for( var y = 0; y < sliders.length; y++ )
			{
				if( sliders[y].type ==="range" )
				{
					sliders[y].oninput = getVals;
					// Manually trigger event first time to display values
					sliders[y].oninput();
				}
			}
		}
	}
// navbar js

window.addEventListener("scroll",function()
{
	var header = document.querySelector("header");
	header.classList.toggle("sticky",window.scrollY > 0);
})

// scroll down js

function scrollWin() {
	setTimeout(() => { window.scrollBy(0, 500); }, 4000);
  }