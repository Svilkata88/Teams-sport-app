filterButton = document.getElementById('filterBtn')
filterButtonsContainer = document.getElementById('filter-c')


filterButton.addEventListener('click', () => {
    filterButtonsContainer.classList.toggle('hidden');
});

