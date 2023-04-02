const form = document.querySelector("#search-form");

form.addEventListener("submit", (event) => {
    event.preventDefault();
    const query = form.querySelector("input[name='q']").value;
    const searchUrl = `https://www.google.com/search?q=${query}`;
    window.location.href = searchUrl;
});
