/* ============================================================
   Shared "broken by design" behavior for the satirical portfolio.
   Every function is an intentional anti-pattern for the talk.
   ============================================================ */

(function () {
  "use strict";

  /* BAD: auto-playing background audio with no pause control.
     The <audio autoplay> element in the DOM also has no controls attribute. */
  function startUnstoppableAudio() {
    var audio = document.getElementById("bg-audio");
    if (!audio) return;
    audio.loop = true;
    audio.volume = 0.35;
    var tryPlay = function () {
      audio.play().catch(function () {
        /* Autoplay may be blocked until a click; then it never stops. */
      });
    };
    tryPlay();
    document.addEventListener("click", tryPlay, { once: true });
  }

  /* BAD: fake "background video" captured from a flashing canvas.
     No pause UI. No prefers-reduced-motion check. */
  function startUnstoppableVideo() {
    var canvas = document.getElementById("bg-canvas");
    var video = document.getElementById("bg-video");
    if (!canvas || !video) return;
    var ctx = canvas.getContext("2d");
    var t = 0;
    function draw() {
      t += 1;
      /* Color cycle ~2Hz — annoying and labeled as flashing, kept under 3 flashes/sec. */
      var hue = (t * 8) % 360;
      ctx.fillStyle = "hsl(" + hue + ", 100%, 50%)";
      ctx.fillRect(0, 0, canvas.width, canvas.height);
      ctx.fillStyle = "#000";
      ctx.font = "20px Comic Sans MS, cursive";
      ctx.fillText("WATCH ME", 20, 40 + Math.sin(t / 6) * 20);
      requestAnimationFrame(draw);
    }
    draw();
    if (canvas.captureStream) {
      video.srcObject = canvas.captureStream(24);
      video.muted = true;
      video.play().catch(function () {});
    }
  }

  /* BAD: custom dropdown is a div, not a <select> or real menu.
     Ignores keyboard entirely (no arrow keys, no Escape, no typeahead).
     Items are not in the tab order. */
  function initBrokenDropdown() {
    var trigger = document.getElementById("dropdown-trigger");
    var menu = document.getElementById("dropdown-menu");
    if (!trigger || !menu) return;
    trigger.addEventListener("click", function () {
      menu.style.display = menu.style.display === "block" ? "none" : "block";
    });
    /* Intentionally no keydown handler. Intentionally no focus management. */
    var items = menu.querySelectorAll(".dropdown-item");
    for (var i = 0; i < items.length; i++) {
      items[i].addEventListener("click", function (e) {
        trigger.textContent = e.target.textContent;
        menu.style.display = "none";
      });
    }
  }

  /* BAD: modal ignores keyboard. Cannot close with Escape.
     Close target is a tiny unlabeled div. Focus is not moved into the modal,
     and the page behind remains interactive (or, on some pages, the overlay
     swallows clicks but not Tab). */
  function initBrokenModal() {
    var modal = document.getElementById("popup");
    var closer = document.getElementById("popup-x");
    if (!modal) return;
    modal.style.display = "block";
    if (closer) {
      closer.addEventListener("click", function () {
        modal.style.display = "none";
      });
    }
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") {
        /* BAD: swallow Escape so the modal cannot be dismissed from the keyboard. */
        e.preventDefault();
        e.stopPropagation();
      }
    });
  }

  /* BAD: "click the red one" — color is the only indicator. */
  function initColorOnly() {
    var nodes = document.querySelectorAll("[data-color-target]");
    for (var i = 0; i < nodes.length; i++) {
      nodes[i].addEventListener("click", function (e) {
        var href = e.currentTarget.getAttribute("data-href");
        if (href) {
          window.location.href = href;
        } else {
          alert("wrong one");
        }
      });
    }
  }

  startUnstoppableAudio();
  startUnstoppableVideo();
  initBrokenDropdown();
  initBrokenModal();
  initColorOnly();
})();
