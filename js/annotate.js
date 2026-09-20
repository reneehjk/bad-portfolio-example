/* Hover annotations for presentation. pointer-events stay on the page;
   the tooltip ignores clicks so links/buttons underneath still work. */

(function () {
  "use strict";

  var STORAGE_KEY = "annotate-mistakes";

  var toggle = document.createElement("button");
  toggle.type = "button";
  toggle.className = "annotate-toggle";
  toggle.textContent = "Show mistakes";
  toggle.setAttribute("aria-pressed", "false");
  toggle.setAttribute("aria-label", "Show mistakes");
  document.body.appendChild(toggle);

  var tip = document.createElement("div");
  tip.className = "annotate-tip";
  tip.setAttribute("role", "tooltip");
  document.body.appendChild(tip);

  var current = null;

  function isOn() {
    return document.body.classList.contains("annotate-on");
  }

  function setOn(on) {
    document.body.classList.toggle("annotate-on", on);
    toggle.setAttribute("aria-pressed", on ? "true" : "false");
    toggle.textContent = on ? "Hide mistakes" : "Show mistakes";
    try {
      sessionStorage.setItem(STORAGE_KEY, on ? "1" : "0");
    } catch (e) {}
    if (!on) hideTip();
  }

  function parseLabel(raw) {
    var match = String(raw).match(/^(A11Y|UX|Visual):\s*(.*)$/);
    if (match) {
      return { kind: match[1], text: match[2] };
    }
    return { kind: "", text: raw };
  }

  function hideTip() {
    if (current) current.classList.remove("is-annotate-hover");
    current = null;
    tip.classList.remove("is-visible");
    tip.innerHTML = "";
  }

  function placeTip(clientX, clientY) {
    var pad = 12;
    tip.style.left = "0px";
    tip.style.top = "0px";
    var w = tip.offsetWidth;
    var h = tip.offsetHeight;
    var x = clientX + 14;
    var y = clientY + 18;
    if (x + w > window.innerWidth - pad) x = clientX - w - 12;
    if (y + h > window.innerHeight - pad) y = clientY - h - 12;
    if (x < pad) x = pad;
    if (y < pad) y = pad;
    tip.style.left = x + "px";
    tip.style.top = y + "px";
  }

  function showTip(el, clientX, clientY) {
    if (current !== el) {
      if (current) current.classList.remove("is-annotate-hover");
      current = el;
      el.classList.add("is-annotate-hover");
      var parsed = parseLabel(el.getAttribute("data-mistake"));
      tip.innerHTML = "";
      if (parsed.kind) {
        var kind = document.createElement("span");
        kind.className = "annotate-kind";
        kind.textContent = parsed.kind;
        tip.appendChild(kind);
      }
      tip.appendChild(document.createTextNode(parsed.text));
      tip.classList.add("is-visible");
    }
    placeTip(clientX, clientY);
  }

  toggle.addEventListener("click", function () {
    setOn(!isOn());
  });

  document.addEventListener(
    "mousemove",
    function (e) {
      if (!isOn()) return;
      if (e.target.closest(".annotate-toggle")) {
        hideTip();
        return;
      }
      var el = e.target.closest("[data-mistake]");
      if (!el) {
        hideTip();
        return;
      }
      showTip(el, e.clientX, e.clientY);
    },
    { passive: true }
  );

  document.addEventListener("mouseleave", hideTip);

  try {
    if (sessionStorage.getItem(STORAGE_KEY) === "1") setOn(true);
  } catch (e) {}
})();
