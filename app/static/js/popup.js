// Pop Up function

const getOfferButton = document.getElementById("get-my-offer_button")
const popUpButton = document.getElementById("pop-up_button")
const popUpWindow = document.getElementById("pop-up_window")
const bodyTag = document.getElementsByTagName("body")

getOfferButton.addEventListener("click", () => {
  popUpWindow.style.display = "block";
  const contactAddress = document.getElementById("contact-form_input-address").value
  const contactNumber = document.getElementById("contact-form_input-number").value

  const popUpAddress = document.getElementById("pop-up-form_input-address").value = contactAddress
  const popUpNumber = document.getElementById("pop-up-form_input-number").value = contactNumber

  bodyTag.className += " blur"

  console.log("address", contactAddress)
  console.log("number", contactNumber)
  console.log("popAddress", popUpAddress)
  return false;
})

popUpButton.addEventListener("click", () =>
  popUpWindow.style.display = "none"
)


