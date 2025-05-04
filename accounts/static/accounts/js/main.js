document.addEventListener("DOMContentLoaded", () => {
  const passwordTogglers = document.querySelectorAll(".password-btn");

  passwordTogglers.forEach((button) => {
    button.addEventListener("click", (e) => {
      const id = button.dataset.id;

      if (!id) return;

      const password = document.getElementById(id);

      if (!password) return;

      button.classList.toggle("show");
      password.type = password.type === "text" ? "password" : "text";
    });
  });
});
