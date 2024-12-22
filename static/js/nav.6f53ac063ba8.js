const dropdown = document.getElementById('dropdown');
const trigger = document.getElementById('trigger');

trigger.addEventListener('click', () => {
    // Toggle the 'active' class on the dropdown
    dropdown.classList.toggle('active');
});