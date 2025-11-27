const root = document.documentElement;
const saved = localStorage.getItem("theme");

// Elements
const sun = document.getElementById("icon-sun");
const moon = document.getElementById("icon-moon");
const button = document.getElementById("theme-toggle");

// Apply saved theme
if (saved === "light") {
    root.classList.add("light");
    sun.classList.remove("hidden");
    moon.classList.add("hidden");
} else {
    root.classList.remove("light");
    sun.classList.add("hidden");
    moon.classList.remove("hidden");
}

// On click toggle
button.addEventListener("click", () => {
    const isLight = root.classList.toggle("light");

    if (isLight) {
        localStorage.setItem("theme", "light");
        sun.classList.remove("hidden");
        moon.classList.add("hidden");
    } else {
        localStorage.setItem("theme", "dark");
        sun.classList.add("hidden");
        moon.classList.remove("hidden");
    }
});
