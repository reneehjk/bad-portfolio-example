/* Three-state view switch: bad | annotated | fixed.
   Persists via localStorage and ?view= so case studies stay in the same state. */

(function () {
  "use strict";

  var STORAGE_KEY = "portfolio-view";
  var VIEWS = ["bad", "annotated", "fixed"];
  var LABELS = { bad: "Bad", annotated: "Annotated", fixed: "Fixed" };

  function readView() {
    try {
      var q = new URLSearchParams(window.location.search).get("view");
      if (VIEWS.indexOf(q) !== -1) return q;
      var stored = localStorage.getItem(STORAGE_KEY);
      if (VIEWS.indexOf(stored) !== -1) return stored;
      if (sessionStorage.getItem("annotate-mistakes") === "1") return "annotated";
    } catch (e) {}
    return "bad";
  }

  function currentView() {
    return document.documentElement.getAttribute("data-view") || "bad";
  }

  function setView(view, persistUrl) {
    if (VIEWS.indexOf(view) === -1) view = "bad";
    document.documentElement.setAttribute("data-view", view);
    try {
      localStorage.setItem(STORAGE_KEY, view);
    } catch (e) {}
    if (persistUrl !== false) {
      try {
        var url = new URL(window.location.href);
        url.searchParams.set("view", view);
        history.replaceState({}, "", url);
      } catch (e) {}
    }
    syncSwitch(view);
    applyFixedAlts(view === "fixed");
    if (view !== "annotated") hideTip();
    document.dispatchEvent(new CustomEvent("viewchange", { detail: { view: view } }));
  }

  function applyFixedAlts(isFixed) {
    var imgs = document.querySelectorAll("[data-alt-fixed]");
    for (var i = 0; i < imgs.length; i++) {
      var img = imgs[i];
      if (!img.getAttribute("data-alt-bad")) {
        img.setAttribute("data-alt-bad", img.getAttribute("alt") || "");
      }
      img.setAttribute("alt", isFixed ? img.getAttribute("data-alt-fixed") : img.getAttribute("data-alt-bad"));
    }
  }

  var switcher = document.createElement("div");
  switcher.className = "view-switch";
  switcher.setAttribute("role", "group");
  switcher.setAttribute("aria-label", "Portfolio view");
  VIEWS.forEach(function (view) {
    var btn = document.createElement("button");
    btn.type = "button";
    btn.setAttribute("data-view-set", view);
    btn.textContent = LABELS[view];
    btn.addEventListener("click", function () {
      setView(view);
    });
    switcher.appendChild(btn);
  });
  document.body.appendChild(switcher);

  function syncSwitch(view) {
    var buttons = switcher.querySelectorAll("button");
    for (var i = 0; i < buttons.length; i++) {
      var on = buttons[i].getAttribute("data-view-set") === view;
      buttons[i].setAttribute("aria-pressed", on ? "true" : "false");
    }
  }

  var tip = document.createElement("div");
  tip.className = "annotate-tip";
  tip.setAttribute("role", "tooltip");
  document.body.appendChild(tip);

  var current = null;

  function parseLabel(raw) {
    var match = String(raw).match(/^(A11Y|UX|Visual):\s*(.*)$/);
    if (match) return { kind: match[1], text: match[2] };
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

  document.addEventListener(
    "mousemove",
    function (e) {
      if (currentView() !== "annotated") return;
      if (e.target.closest(".view-switch")) {
        hideTip();
        return;
      }
      var el = e.target.closest("[data-mistake]");
      if (!el || el.closest(".view-fixed")) {
        hideTip();
        return;
      }
      showTip(el, e.clientX, e.clientY);
    },
    { passive: true }
  );

  document.addEventListener("mouseleave", hideTip);

  setView(readView(), true);
})();
