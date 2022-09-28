// Alerts
let alertList = document.querySelectorAll('.alert')
alertList.forEach(function (alert) {
    const bsAlert = new bootstrap.Alert(alert)

    setTimeout(() => {
        bsAlert.close();
    }, "5000")
})

// Modals
const myModal = document.getElementById('deleteProfileModal')
const myInput = document.getElementById('deleteAccountPassword')
const deleteAccountForm = document.getElementById('deleteAccountForm')
const deleteAccountButton = document.getElementById('deleteAccountButton')



myModal.addEventListener('shown.bs.modal', function () {
  myInput.focus()
})

deleteAccountButton.addEventListener('click', () => deleteAccountForm.submit())