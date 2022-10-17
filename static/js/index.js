const alertClose = document.querySelector(".alert__close")
const alertDiv = document.querySelector(".alert")
const passwordFields = document.querySelectorAll("input[type=password]")
const eyeBtn = document.querySelector(".show_pass")



if (alertDiv) {
  alertClose.addEventListener("click", () => {
    alertDiv.classList.add("hide")
  })
}


if (passwordFields) {
  eyeBtn.addEventListener("click", () => {
    passwordFields.forEach(element => {
      if (element.type == "password") {
        element.type = "text"
      } else {
        element.type = "password"
      }
    })
  })
}