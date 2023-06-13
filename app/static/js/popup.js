const getOfferButton = document.querySelectorAll('.get-my-offer_button');
const popUpButton = document.getElementById("pop-up_button");
const popUpWindow = document.getElementById("pop-up_window");
const bodyTag = document.getElementsByTagName("body");

getOfferButton.forEach(btn => {
  btn.addEventListener("click", () => {
    popUpWindow.style.display = "block";
    const contactAddress = document.querySelectorAll(".contact-form_input-address");
    const contactNumber = document.querySelectorAll(".contact-form_input-number");

    const popUpAddress = document.getElementById("pop-up-form_input-address").value = contactAddress[0].value + contactAddress[1].value;
    const popUpNumber = document.getElementById("pop-up-form_input-number").value = contactNumber[0].value + contactNumber[1].value;

    console.log("number", contactNumber[0].value);
    document.body.classList.add("blur");
  })
});

// getOfferButton.addEventListener("click", () => {
//   popUpWindow.style.display = "block";
//   const contactAddress = document.getElementById("contact-form_input-address").value
//   const contactNumber = document.getElementById("contact-form_input-number").value

//   const popUpAddress = document.getElementById("pop-up-form_input-address").value = contactAddress
//   const popUpNumber = document.getElementById("pop-up-form_input-number").value = contactNumber

//   document.body.classList.add("blur");


//   console.log("address", contactAddress)
//   console.log("window", popUpWindow)
//   console.log("body", bodyTag)
//   return false;
// })

popUpButton.addEventListener("click", () =>{
  const contactAddress = document.querySelectorAll(".contact-form_input-address");
  const contactNumber = document.querySelectorAll(".contact-form_input-number");

  contactAddress.forEach(val => {val.value = ""})
  contactNumber.forEach(val => {val.value = ""})

  popUpWindow.style.display = "none";
  document.body.classList.remove("blur");
});


