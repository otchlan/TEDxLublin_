document.getElementById('subscribe-button').addEventListener('click', function(e) {
    // Get the input elements
    var nameInput = document.getElementById('id_name');
    var emailInput = document.getElementById('id_email');

    // Check if the inputs are valid
    if (nameInput.checkValidity() && emailInput.checkValidity()) {
        // Inputs are valid, manually trigger the modal
        var modal = new bootstrap.Modal(document.getElementById('confirmationModal'));
        modal.show();
    } else {
        // Inputs are invalid, display validation errors
        if (!nameInput.checkValidity()) {
            nameInput.reportValidity();  // This will show the default validation error message
        }
        if (!emailInput.checkValidity()) {
            emailInput.reportValidity();  // This will show the default validation error message
        }
    }
});

document.addEventListener('DOMContentLoaded', function() {
    if (document.getElementById('messageModal')) {
        // Display the modal
        var modal = new bootstrap.Modal(document.getElementById('messageModal'));
        modal.show();
    }
});