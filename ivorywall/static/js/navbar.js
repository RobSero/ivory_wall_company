const dropdownButton = document.getElementById('dropdown-toggle')
const dropdownMenu = document.getElementById('mobile-dropdown')
const contactPopUp = document.getElementById('message-area')
const contactButton = document.getElementById('message-button')
const contactCloseButton = document.getElementById('message-exit')
dropdownButton.addEventListener('click', toggleDropdown)


function toggleDropdown(){
  if (dropdownMenu.classList.contains('is-active')){
    dropdownMenu.classList.remove('is-active')
  } else {
    dropdownMenu.classList.add('is-active')
  }
}

// Popup message section
contactButton.addEventListener('click', ()=> {
  contactPopUp.style.display = 'block'
  contactPopUp.classList.add('animate__fadeIn')
})

contactCloseButton.addEventListener('click', ()=> {
  contactPopUp.classList.remove('animate__fadeIn')
  contactPopUp.classList.add('animate__fadeOut')
  setTimeout(()=> {
    contactPopUp.style.display = 'none'
  },1000)
})





