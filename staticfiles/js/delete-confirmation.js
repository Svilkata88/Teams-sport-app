const modal = document.getElementById('customModal');
const closeBtn = document.getElementById('closeBtn');
const confirmBtn = document.getElementById('confirmBtn');
const cancelBtn = document.getElementById('cancelBtn');
const deleteForm = document.getElementById('deleteForm');

function showModal() {
    modal.style.display = 'flex';
    console.log('showed')
}

function closeModal() {
    modal.style.display = 'none';
}

closeBtn.addEventListener('click', closeModal);

cancelBtn.addEventListener('click', closeModal);

confirmBtn.addEventListener('click', function () {
    deleteForm.submit();
    closeModal();
});

document.getElementById('deleteTeamBtn').addEventListener('click', function (e) {
    e.preventDefault();
    showModal();
});