function setupCampaignCategoryLimit() {
  const checkboxes = document.querySelectorAll('input[type="checkbox"][data-category]');
  checkboxes.forEach(currentBox => {
    currentBox.addEventListener("change", () => {
      const category = currentBox.dataset.category;
      checkboxes.forEach(other => {
        if (other !== currentBox && other.dataset.category === category) {
          other.disabled = currentBox.checked;
        }
      });
    });
  });
}

setupCampaignCategoryLimit();

const form = document.getElementById("campaign-form");
const resultBox = document.getElementById("discount-result");

form.addEventListener("submit", async function (event) {
  event.preventDefault();

  const selected = [];
  document.querySelectorAll('input[type="checkbox"]:checked').forEach(cb => {
    selected.push(cb.value);
  });

  if (selected.length === 0) {
    alert("Please select at least one campaign.");
    return;
  }

  try {
    const response = await fetch("http://localhost:8000/apply-discounts", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ campaign_ids: selected })
    });

    if (response.ok) {
      const data = await response.json();
      resultBox.innerHTML = `<h3>Final Price: ฿${data.final_price}</h3>`;
    } else {
      const error = await response.json();
      resultBox.innerHTML = `<h3 style="color:red;">${error.detail}</h3>`;
    }
  } catch (err) {
    resultBox.innerHTML = `<h3 style="color:red;">Request failed</h3>`;
  }
});
