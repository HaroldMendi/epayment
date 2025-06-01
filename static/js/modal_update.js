function openUpdateModal(id) {
    $.ajax({
        url: `/profile-update/${id}/`,
        success: function(data) {
            $('#modalContent').html(data);
            var myModal = new bootstrap.Modal(document.getElementById('updateModal'));
            myModal.show();
        }
    });
}

function submitUpdateForm(event, form) {
    event.preventDefault();
    $.ajax({
        url: form.action,
        method: 'POST',
        data: $(form).serialize(),
        success: function(data) {
            if (data.success) {
                location.reload();
            } else {
                $('#modalContent').html(data);
            }
        }
    });
}