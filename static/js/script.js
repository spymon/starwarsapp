let alertList = document.querySelectorAll('.alert')
alertList.forEach(function (alert) {
    const bsAlert = new bootstrap.Alert(alert)

    setTimeout(() => {
        bsAlert.close();
    }, "5000")
})
