const getOfferButton = document.querySelectorAll('.get-my-offer_button');
const popUpButton = document.getElementById("pop-up_button");
const popUpWindow = document.getElementById("pop-up_window");
const bodyTag = document.getElementsByTagName("body");

// Display pop up window on contact form submit button
getOfferButton.forEach(btn => {
  btn.addEventListener("click", () => {
    const contactAddress = document.querySelectorAll(".contact-form_input-address");
    const contactNumber = document.querySelectorAll(".contact-form_input-number");

    const popUpAddress = document.getElementById("pop-up-form_input-address").value = contactAddress[0].value + contactAddress[1].value;
    const popUpNumber = document.getElementById("pop-up-form_input-number").value = contactNumber[0].value + contactNumber[1].value;

    popUpWindow.style.display = "block";
    document.body.classList.add("blur");

    window.scrollTo({
      top: 0,
      behavior: "smooth"
    });
  })
});

// Disable pop up window on pop up submit button
popUpButton.addEventListener("click", () =>{
  const contactAddress = document.querySelectorAll(".contact-form_input-address");
  const contactNumber = document.querySelectorAll(".contact-form_input-number");
  const popUpAddress = document.getElementById("pop-up-form_input-address").value;
  const popUpNumber = document.getElementById("pop-up-form_input-number").value;

  contactAddress.forEach(val => {val.value = ""})
  contactNumber.forEach(val => {val.value = ""})

  console.log("popUpAddress", popUpAddress)
  console.log("popUpNumber", popUpNumber)

  if (popUpAddress && popUpNumber) {
    popUpWindow.style.display = "none";
    document.body.classList.remove("blur");
  }
});

// Disable pop up window on mouse click
window.addEventListener('mouseup', (event) => {
  if (event.target !== popUpWindow && !popUpWindow.contains(event.target)) {
    popUpWindow.style.display = "none";
    document.body.classList.remove("blur");
  }
})
