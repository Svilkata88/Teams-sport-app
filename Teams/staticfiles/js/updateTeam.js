const modal = document.getElementById('customModal');
const closeBtn = document.getElementById('closeBtn');
const confirmBtn = document.getElementById('confirmBtn');
const cancelBtn = document.getElementById('cancelBtn');
const deleteForm = document.getElementById('deleteForm');

function showModal() {
    modal.style.display = 'flex';  // Show the modal
}

function closeModal() {
    modal.style.display = 'none';  // Hide the modal
}

closeBtn.addEventListener('click', closeModal);

cancelBtn.addEventListener('click', closeModal);

confirmBtn.addEventListener('click', function () {
    deleteForm.submit();  // Submit the form to delete the team
    closeModal();  // Close the modal
});

document.getElementById('deleteTeamBtn').addEventListener('click', function (e) {
    e.preventDefault();  // Prevent the form from submitting
    showModal();  // Show the confirmation
});