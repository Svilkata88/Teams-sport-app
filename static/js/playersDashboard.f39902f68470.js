

window.onload = () => {
    const searchInput = document.getElementById('id_username');

    if (searchInput) {
        // Clear the input
        searchInput.value = '';

        // Remove query parameters from the URL
        const url = new URL(window.location);
        url.search = ''; // Clear query string
        window.history.replaceState({}, document.title, url.pathname);
    }
};