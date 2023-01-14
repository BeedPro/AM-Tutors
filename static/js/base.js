// function myFunction() {
//     var x = document.getElementById("myTopnav");
//     if (x.className === "topnav") {
//       x.className += " responsive";
//     } else {
//       x.className = "topnav";
//     }
//   }

// Get the navbar element
let navbar = document.querySelector('.navbar');

// Get the current scroll position
let prevScrollpos = window.pageYOffset;

// Listen for the scroll event
window.onscroll = function() {
    let currentScrollPos = window.pageYOffset;
    if (prevScrollpos > currentScrollPos) {
        navbar.classList.remove("navbar-hidden");
    } else {
        navbar.classList.add("navbar-hidden");
    }
    prevScrollpos = currentScrollPos;
}