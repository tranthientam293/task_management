document.addEventListener("DOMContentLoaded",() => {
  const dropdown = document.getElementById("dropdown");

  const dropdownItems = document.querySelectorAll(".dropdown-item");

  dropdown.addEventListener("click", () => {
    dropdown.classList.toggle("active");
  })

  dropdownItems.forEach(item => {
    item.addEventListener("click", (e) => {
      e.stopPropagation();
      dropdown.classList.remove("active");
    })
  })

  document.addEventListener("click", (e) => {
    if (!e.target.closest("#dropdown")){
      console.log("run")
      dropdown.classList.remove("active");
    }
  })
})
