(function () {
  "use strict";

  var form = document.querySelector(".contact-form");
  if (!form) return;

  form.addEventListener("submit", function (e) {
    e.preventDefault();
    var note = document.querySelector(".form-note");
    if (note) {
      note.classList.add("is-visible");
      note.textContent = "Thanks for reaching out. I'll get back to you soon.";
    }
  });
})();
