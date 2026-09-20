/* Bad-mode interactions, plus corrected behavior when data-view="fixed". */

(function () {
  "use strict";

  function view() {
    return document.documentElement.getAttribute("data-view") || "bad";
  }

  /* ----- carousel ----- */
  var carousel = {
    root: null,
    track: null,
    slides: null,
    index: 0,
    timer: null,
    paused: false,
    pauseBtn: null
  };

  function carouselGo(i) {
    if (!carousel.slides || !carousel.slides.length) return;
    carousel.index = (i + carousel.slides.length) % carousel.slides.length;
    carousel.track.style.transform = "translateX(" + -carousel.index * 100 + "%)";
    var dots = carousel.root.querySelectorAll(".carousel-dot, .carousel-dots button");
    for (var d = 0; d < dots.length; d++) {
      var on = d === carousel.index;
      dots[d].classList.toggle("is-active", on);
      if (dots[d].tagName === "BUTTON") {
        dots[d].setAttribute("aria-current", on ? "true" : "false");
      }
    }
  }

  function stopAutoplay() {
    if (carousel.timer) {
      clearInterval(carousel.timer);
      carousel.timer = null;
    }
  }

  function startAutoplay() {
    stopAutoplay();
    if (carousel.paused) return;
    carousel.timer = setInterval(function () {
      carouselGo(carousel.index + 1);
    }, 4500);
  }

  function syncCarouselToView() {
    if (!carousel.root) return;
    var pause = document.querySelector(".carousel-pause");
    if (view() === "fixed") {
      var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
      carousel.paused = reduce;
      if (pause) {
        pause.textContent = carousel.paused ? "Play" : "Pause";
        pause.setAttribute("aria-pressed", carousel.paused ? "true" : "false");
      }
      if (carousel.paused) stopAutoplay();
      else startAutoplay();
    } else {
      carousel.paused = false;
      startAutoplay();
    }
  }

  function initCarousel() {
    carousel.root = document.querySelector(".carousel");
    if (!carousel.root) return;
    carousel.track = carousel.root.querySelector(".carousel-track");
    carousel.slides = carousel.root.querySelectorAll(".carousel-slide");
    if (!carousel.track || carousel.slides.length < 2) return;

    carousel.root.addEventListener("click", function (e) {
      var dot = e.target.closest("[data-slide]");
      if (dot) {
        carouselGo(parseInt(dot.getAttribute("data-slide"), 10));
      }
      if (e.target.closest(".carousel-pause")) {
        carousel.paused = !carousel.paused;
        var btn = e.target.closest(".carousel-pause");
        btn.textContent = carousel.paused ? "Play" : "Pause";
        btn.setAttribute("aria-pressed", carousel.paused ? "true" : "false");
        if (carousel.paused) stopAutoplay();
        else startAutoplay();
      }
    });

    syncCarouselToView();
  }

  /* ----- dropdown (bad only; fixed uses a real <select>) ----- */
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

  function initFilter() {
    var select = document.getElementById("project-filter");
    if (!select) return;
    select.addEventListener("change", function () {
      var value = select.value;
      var cards = document.querySelectorAll(".work-grid article");
      for (var i = 0; i < cards.length; i++) {
        var cat = cards[i].getAttribute("data-category") || "all";
        cards[i].style.display = value === "all" || value === cat ? "" : "none";
      }
    });
  }

  /* ----- modal ----- */
  var lastFocus = null;

  function focusables(root) {
    return root.querySelectorAll(
      'button:not([disabled]), [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
    );
  }

  function closeModal(modal) {
    modal.classList.remove("is-open");
    modal.setAttribute("aria-hidden", "true");
    if (lastFocus && lastFocus.focus) lastFocus.focus();
  }

  function openModal(modal) {
    lastFocus = document.activeElement;
    modal.classList.add("is-open");
    modal.setAttribute("aria-hidden", "false");
    if (view() === "fixed") {
      var panel = modal.querySelector(".modal-panel");
      var list = focusables(panel);
      if (list.length) list[0].focus();
    }
  }

  function initModal() {
    var modal = document.querySelector(".modal");
    if (!modal) return;
    openModal(modal);

    modal.addEventListener("click", function (e) {
      if (e.target.classList.contains("modal") && view() === "fixed") {
        closeModal(modal);
      }
      if (e.target.closest(".modal-close")) {
        closeModal(modal);
      }
    });

    document.addEventListener("keydown", function (e) {
      if (!modal.classList.contains("is-open")) return;
      if (view() !== "fixed") return;
      if (e.key === "Escape") {
        e.preventDefault();
        closeModal(modal);
        return;
      }
      if (e.key !== "Tab") return;
      var list = focusables(modal.querySelector(".modal-panel"));
      if (!list.length) return;
      var first = list[0];
      var last = list[list.length - 1];
      if (e.shiftKey && document.activeElement === first) {
        e.preventDefault();
        last.focus();
      } else if (!e.shiftKey && document.activeElement === last) {
        e.preventDefault();
        first.focus();
      }
    });
  }

  document.addEventListener("viewchange", function () {
    syncCarouselToView();
  });

  initCarousel();
  initDropdown();
  initFilter();
  initModal();
})();
