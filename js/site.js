/* Realistic-but-flawed interactions for the presentation.
   Search for BAD: to jump to each talking point. */

(function () {
  "use strict";

  /* BAD: carousel autoplays with no pause, stop, or reduced-motion handling */
  function initCarousel() {
    var root = document.querySelector(".carousel");
    if (!root) return;
    var track = root.querySelector(".carousel-track");
    var slides = root.querySelectorAll(".carousel-slide");
    var dots = root.querySelectorAll(".carousel-dot");
    if (!track || slides.length < 2) return;
    var index = 0;

    function go(i) {
      index = (i + slides.length) % slides.length;
      track.style.transform = "translateX(" + -index * 100 + "%)";
      for (var d = 0; d < dots.length; d++) {
        dots[d].classList.toggle("is-active", d === index);
      }
    }

    for (var d = 0; d < dots.length; d++) {
      (function (n) {
        dots[n].addEventListener("click", function () {
          go(n);
        });
      })(d);
    }

    setInterval(function () {
      go(index + 1);
    }, 4500);
  }

  /* BAD: custom dropdown is not a <select> or button+menu.
     Trigger is a div. Hidden options stay in the tab order (tabindex="0"),
     so Tab walks through them even while the menu is closed. */
  function initDropdown() {
    var dropdown = document.querySelector(".dropdown");
    if (!dropdown) return;
    var trigger = dropdown.querySelector(".dropdown-trigger");
    var items = dropdown.querySelectorAll(".dropdown-item");
    trigger.addEventListener("click", function () {
      dropdown.classList.toggle("is-open");
    });
    for (var i = 0; i < items.length; i++) {
      items[i].addEventListener("click", function (e) {
        trigger.textContent = e.currentTarget.textContent;
        dropdown.classList.remove("is-open");
      });
    }
  }

  /* BAD: modal does not move focus inward, close control is not a button
     (skipped when tabbing), and focus is free to leave onto the page behind.
     Escape is not handled. Not a hard trap — just a broken tab order. */
  function initModal() {
    var modal = document.querySelector(".modal");
    if (!modal) return;
    var closer = modal.querySelector(".modal-close");
    modal.classList.add("is-open");
    if (closer) {
      closer.addEventListener("click", function () {
        modal.classList.remove("is-open");
      });
    }
  }

  initCarousel();
  initDropdown();
  initModal();
})();
