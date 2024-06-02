const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

console.log("hello!!!")
for (let button of deleteButtons) {
  button.addEventListener("click", (e) => {
      console.log(e)
    let bookingId = e.target.getAttribute("booking_id");
    deleteConfirm.href = `delete-booking/${bookingId}`;
    deleteModal.show();
  });
}