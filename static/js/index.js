const alertClose = document.querySelector(".alert__close")
const alertDiv = document.querySelector(".alert")
const passwordFields = document.querySelectorAll("input[type=password]")
const eyeBtn = document.querySelector(".show_pass")



alertClose.addEventListener("click", () => {
  alertDiv.classList.add("hide")
})


eyeBtn.addEventListener("click", () => {
  passwordFields.forEach(element => {
    if (element.type == "password") {
      element.type = "text"
    } else {
      element.type = "password"
    }
  })
})