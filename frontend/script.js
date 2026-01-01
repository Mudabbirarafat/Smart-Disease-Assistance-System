const API_URL = "http://127.0.0.1:5000";

function predictCrop() {
  const fileInput = document.getElementById("cropImage");
  const result = document.getElementById("cropResult");

  if (fileInput.files.length === 0) {
    alert("Please upload a leaf image");
    return;
  }

  result.style.display = "block";
  result.innerHTML = "<span class='loading'>Predicting disease...</span>";

  const formData = new FormData();
  formData.append("image", fileInput.files[0]);

  fetch(`${API_URL}/predict-crop`, {
    method: "POST",
    body: formData
  })
    .then(res => res.json())
    .then(data => {
      result.innerHTML =
        `🌱 <b>Disease:</b> ${data.disease}<br>
         📊 <b>Confidence:</b> ${data.confidence}%`;
    })
    .catch(() => {
      result.innerHTML = "❌ Error predicting crop disease";
    });
}

function predictMedical() {
  const result = document.getElementById("medicalResult");
  result.style.display = "block";
  result.innerHTML = "<span class='loading'>Analyzing risk...</span>";

  const fields = [
    "Pregnancies","Glucose","BloodPressure","SkinThickness",
    "Insulin","BMI","DiabetesPedigreeFunction","Age"
  ];

  let payload = {};
  for (let f of fields) {
    payload[f] = Number(document.getElementById(f).value);
  }

  fetch(`${API_URL}/medical-chat`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload)
  })
    .then(res => res.json())
    .then(data => {
      result.innerHTML =
        `🩺 <b>Risk:</b> ${data.risk}<br>
         📈 <b>Probability:</b> ${data.probability}%`;
    })
    .catch(() => {
      result.innerHTML = "❌ Error predicting medical risk";
    });
}
