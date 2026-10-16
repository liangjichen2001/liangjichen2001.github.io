(() => {
  "use strict";

  const root = document.documentElement;
  const preference = window.matchMedia("(prefers-color-scheme: dark)");
  const toggle = document.querySelector("[data-theme-toggle]");
  let savedTheme;

  try {
    savedTheme = localStorage.getItem("liangji-theme");
  } catch (_) {
    // The site also works when browser storage is disabled.
  }

  const applyTheme = (theme) => {
    root.dataset.theme = theme;
    if (toggle) {
      toggle.setAttribute("aria-label", theme === "dark" ? "切换至浅色主题" : "切换至深色主题");
      toggle.setAttribute("aria-pressed", String(theme === "dark"));
    }
    const color = document.querySelector('meta[name="theme-color"]');
    if (color) color.content = theme === "dark" ? "#141e23" : "#f8fafb";
  };

  applyTheme(savedTheme === "light" || savedTheme === "dark" ? savedTheme : (preference.matches ? "dark" : "light"));

  if (toggle) {
    toggle.hidden = false;
    toggle.addEventListener("click", () => {
      savedTheme = root.dataset.theme === "dark" ? "light" : "dark";
      applyTheme(savedTheme);
      try {
        localStorage.setItem("liangji-theme", savedTheme);
      } catch (_) {
        // Theme selection remains available for this page.
      }
    });
  }

  preference.addEventListener("change", (event) => {
    if (savedTheme !== "light" && savedTheme !== "dark") applyTheme(event.matches ? "dark" : "light");
  });

  document.querySelectorAll("[data-print]").forEach((button) => {
    button.hidden = false;
    button.addEventListener("click", () => window.print());
  });
})();
