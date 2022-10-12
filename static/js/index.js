const alertClose = document.querySelector(".alert__close")
const alertDiv = document.querySelector(".alert")

alertClose.addEventListener("click", () => {
  alertDiv.classList.add("hide")
})