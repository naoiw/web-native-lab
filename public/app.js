// Minimal JavaScript: only for capabilities that require it in this demo.
document.querySelectorAll("[data-open-dialog]").forEach((button) => {
  button.addEventListener("click", () => {
    const dialog = document.getElementById(button.dataset.openDialog);
    if (dialog instanceof HTMLDialogElement) dialog.showModal();
  });
});

const validationForm = document.getElementById("validation-form");
validationForm?.addEventListener("submit", (event) => {
  event.preventDefault(); // Keep the demo on this page; browser validity checking is native.
  document.getElementById("validation-result").textContent = "✓ HTMLの制約チェックを通過しました。";
});