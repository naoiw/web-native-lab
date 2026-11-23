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

// <output> provides result semantics; updating values dynamically needs JavaScript.
const additionForm = document.getElementById("addition-form");
additionForm?.addEventListener("input", () => {
  const a = additionForm.elements.namedItem("a");
  const b = additionForm.elements.namedItem("b");
  const result = additionForm.elements.namedItem("result");
  if (a instanceof HTMLInputElement &&
      b instanceof HTMLInputElement &&
      result instanceof HTMLOutputElement) {
    result.value = String(Number(a.value) + Number(b.value));
  }
});
