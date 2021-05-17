var modalDelete = document.getElementById('modalDelete');
modalDelete.addEventListener('show.bs.modal', function (event) {
    var modalTrigger = event.relatedTarget

    var modalForm = modalDelete.querySelector('form')
    var modalModelName = modalDelete.querySelector('.model-name')
    var modalObjectDescription = modalDelete.querySelector('.object-description')

    modalForm.action = modalTrigger.getAttribute('data-bs-url');
    modalModelName.textContent = modalTrigger.getAttribute('data-bs-model');
    modalObjectDescription.textContent = modalTrigger.getAttribute('data-bs-object');
})
