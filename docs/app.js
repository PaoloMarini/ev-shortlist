const state = {
  vehicles: [],
  criteria: [],
  changeLog: [],
  photoCollections: {}
};

const statusOrder = {
  shortlist: 1,
  watchlist: 2,
  research: 3,
  benchmark: 4,
  rejected: 5
};

async function loadJson(path) {
  const response = await fetch(path);
  if (!response.ok) throw new Error(`Failed to load ${path}`);
  return response.json();
}

function scoreVehicle(vehicle) {
  const weighted = state.criteria.reduce((total, criterion) => {
    const score = vehicle.scores?.[criterion.id];
    if (typeof score !== "number") return total;
    return total + score * criterion.weight;
  }, 0);

  const possible = state.criteria.reduce((total, criterion) => {
    const score = vehicle.scores?.[criterion.id];
    if (typeof score !== "number") return total;
    return total + criterion.weight;
  }, 0);

  if (!possible) return null;
  return Math.round((weighted / possible) * 10) / 10;
}

function unknownCount(vehicle) {
  return state.criteria.filter((criterion) => typeof vehicle.scores?.[criterion.id] !== "number").length;
}

function formatFactValue(key, value) {
  if (value === null || value === undefined || value === "") return "TBD";
  if (key === "priceGbp") return `£${Number(value).toLocaleString("en-GB")}`;
  if (key === "rangeMiles") return `${value} miles`;
  if (key === "zeroTo62Sec") return `${value}s 0–62`;
  if (key === "maxPowerHp") return `${value} hp`;
  if (key === "charge10To80Min") return `${value} min 10–80%`;
  if (key === "maxDcKw") return `${value} kW DC`;
  return value;
}

function factLabel(key) {
  return {
    priceGbp: "Price",
    rangeMiles: "Range",
    zeroTo62Sec: "Acceleration",
    maxPowerHp: "Power",
    charge10To80Min: "Charging",
    maxDcKw: "Peak DC",
    audio: "Audio",
    dashboard: "Dashboard",
    phoneIntegration: "Phone",
    security: "Security"
  }[key] || key;
}

function flagItems(vehicle) {
  const flags = vehicle.flags || {};
  const items = [];

  if (flags.featureSubscription && flags.featureSubscription !== false && flags.featureSubscription !== "no") {
    items.push({ label: "Feature subscriptions?", severity: "warn" });
  }
  if (flags.tabletDashboard && flags.tabletDashboard !== false) {
    items.push({ label: "Dashboard risk", severity: "warn" });
  }
  if (flags.touchOnlyBasicControls && flags.touchOnlyBasicControls !== false) {
    items.push({ label: "Touch controls?", severity: "warn" });
  }
  if (flags.unreliablePhoneIntegration && flags.unreliablePhoneIntegration !== false) {
    items.push({ label: "Phone integration?", severity: "warn" });
  }
  if (flags.theftSecurityConcern && flags.theftSecurityConcern !== false) {
    items.push({ label: "Security check", severity: "bad" });
  }
  if (flags.weakUkSupport && flags.weakUkSupport !== false) {
    items.push({ label: "UK support?", severity: "warn" });
  }
  if (flags.expensive) {
    items.push({ label: "Cost risk", severity: "warn" });
  }

  return items;
}

function renderCriteria() {
  const container = document.getElementById("criteria");
  container.innerHTML = "";

  state.criteria.forEach((criterion) => {
    const div = document.createElement("div");
    div.className = "criterion";
    div.innerHTML = `
      <strong>${criterion.label}<span class="weight">${criterion.weight}%</span></strong>
      <p class="muted">${criterion.description}</p>
    `;
    container.appendChild(div);
  });
}

function renderPhotos(vehicle, container) {
  const collection = state.photoCollections[vehicle.id];
  const photos = collection?.photos || [];

  if (!photos.length) {
    const pending = document.createElement("p");
    pending.className = "photo-pending";
    pending.textContent = collection?.status
      ? `Official photo carousel pending: ${collection.status}.`
      : "Official photo carousel pending.";
    container.appendChild(pending);
    return;
  }

  const wrapper = document.createElement("div");
  wrapper.className = "photo-carousel";

  const track = document.createElement("div");
  track.className = "photo-track";

  photos.forEach((photo, index) => {
    const figure = document.createElement("figure");
    figure.className = "photo-slide";
    figure.innerHTML = `
      <img src="${photo.url}" alt="${vehicle.make} ${vehicle.model}: ${photo.caption || `official photo ${index + 1}`}" loading="lazy" />
      <figcaption>${index + 1}/${photos.length} · ${photo.caption || "Official manufacturer image"}</figcaption>
    `;
    track.appendChild(figure);
  });

  const source = document.createElement("p");
  source.className = "photo-source";
  source.textContent = `${photos.length} manufacturer-hosted images · ${collection.status || "official"}`;

  wrapper.append(track, source);
  container.appendChild(wrapper);
}

function renderVehicles() {
  const container = document.getElementById("vehicle-grid");
  const template = document.getElementById("vehicle-card-template");
  const statusFilter = document.getElementById("status-filter").value;
  const sortMode = document.getElementById("sort-mode").value;
  const showUnknowns = document.getElementById("show-unknowns").checked;

  let vehicles = [...state.vehicles];

  if (statusFilter !== "all") {
    vehicles = vehicles.filter((vehicle) => vehicle.status === statusFilter);
  }

  if (!showUnknowns) {
    vehicles = vehicles.filter((vehicle) => unknownCount(vehicle) < state.criteria.length - 2);
  }

  vehicles.sort((a, b) => {
    if (sortMode === "score") {
      return (scoreVehicle(b) ?? -1) - (scoreVehicle(a) ?? -1);
    }
    if (sortMode === "status") {
      return (statusOrder[a.status] ?? 99) - (statusOrder[b.status] ?? 99);
    }
    if (sortMode === "confidence") {
      return String(a.evidenceConfidence).localeCompare(String(b.evidenceConfidence));
    }
    return `${a.make} ${a.model}`.localeCompare(`${b.make} ${b.model}`);
  });

  container.innerHTML = "";

  vehicles.forEach((vehicle) => {
    const score = scoreVehicle(vehicle);
    const node = template.content.cloneNode(true);
    node.querySelector(".status").textContent = vehicle.status;
    node.querySelector("h3").textContent = `${vehicle.make} ${vehicle.model}`;
    node.querySelector(".meta").textContent = `${vehicle.bodyType || "Unknown body"} · ${vehicle.origin || "origin TBD"} · ${vehicle.availabilityUk || "availability TBD"}`;
    node.querySelector(".score").textContent = score === null ? "—" : score.toFixed(1);

    renderPhotos(vehicle, node.querySelector(".photo-section"));

    const factList = node.querySelector(".fact-list");
    const facts = vehicle.facts || {};
    ["priceGbp", "rangeMiles", "zeroTo62Sec", "maxPowerHp", "charge10To80Min", "maxDcKw"].forEach((key) => {
      if (facts[key] === undefined) return;
      const div = document.createElement("div");
      div.innerHTML = `<dt>${factLabel(key)}</dt><dd>${formatFactValue(key, facts[key])}</dd>`;
      factList.appendChild(div);
    });

    const assessmentList = node.querySelector(".assessment-list");
    ["audio", "dashboard", "phoneIntegration", "security"].forEach((key) => {
      if (!facts[key]) return;
      const div = document.createElement("div");
      div.innerHTML = `<dt>${factLabel(key)}</dt><dd>${facts[key]}</dd>`;
      assessmentList.appendChild(div);
    });

    const flagList = node.querySelector(".flag-list");
    const flags = flagItems(vehicle);
    if (!flags.length) {
      const span = document.createElement("span");
      span.className = "flag";
      span.textContent = "No known red flags";
      flagList.appendChild(span);
    } else {
      flags.forEach((flag) => {
        const span = document.createElement("span");
        span.className = `flag ${flag.severity === "bad" ? "bad" : ""}`;
        span.textContent = flag.label;
        flagList.appendChild(span);
      });
    }

    const scoreList = node.querySelector(".score-list");
    state.criteria.forEach((criterion) => {
      const wrapper = document.createElement("div");
      const dt = document.createElement("dt");
      const dd = document.createElement("dd");
      dt.textContent = criterion.label;
      const value = vehicle.scores?.[criterion.id];
      dd.textContent = typeof value === "number" ? `${value}/10` : "TBD";
      wrapper.append(dt, dd);
      scoreList.appendChild(wrapper);
    });

    const notes = node.querySelector(".notes");
    (vehicle.notes || []).forEach((note) => {
      const li = document.createElement("li");
      li.textContent = note;
      notes.appendChild(li);
    });

    const sources = node.querySelector(".sources");
    (vehicle.sources || []).forEach((source) => {
      const li = document.createElement("li");
      li.textContent = source;
      sources.appendChild(li);
    });

    node.querySelector(".confidence").textContent = `Evidence confidence: ${vehicle.evidenceConfidence || "unknown"}. Last checked: ${vehicle.lastChecked || "TBD"}.`;
    container.appendChild(node);
  });
}

function renderChangeLog() {
  const container = document.getElementById("change-log");
  container.innerHTML = "";

  state.changeLog.forEach((entry) => {
    const div = document.createElement("div");
    div.className = "change-entry";
    const details = (entry.details || []).map((item) => `<li>${item}</li>`).join("");
    div.innerHTML = `
      <strong>${entry.date} · ${entry.summary}</strong>
      <ul>${details}</ul>
    `;
    container.appendChild(div);
  });
}

async function init() {
  const [vehiclesData, criteriaData, changeLogData, photosData] = await Promise.all([
    loadJson("data/vehicles.json"),
    loadJson("data/criteria.json"),
    loadJson("data/change-log.json"),
    loadJson("data/photos.json")
  ]);

  state.vehicles = vehiclesData.vehicles;
  state.criteria = criteriaData.criteria;
  state.changeLog = changeLogData.entries;
  state.photoCollections = photosData.collections || {};

  document.getElementById("last-updated").textContent = vehiclesData.lastUpdated;
  const benchmark = state.vehicles.find((vehicle) => vehicle.id === vehiclesData.benchmark);
  document.getElementById("benchmark").textContent = benchmark ? `${benchmark.make} ${benchmark.model}` : vehiclesData.benchmark;

  renderCriteria();
  renderVehicles();
  renderChangeLog();

  document.getElementById("status-filter").addEventListener("change", renderVehicles);
  document.getElementById("sort-mode").addEventListener("change", renderVehicles);
  document.getElementById("show-unknowns").addEventListener("change", renderVehicles);
}

init().catch((error) => {
  document.body.innerHTML = `<main class="panel"><h1>Dashboard failed to load</h1><p>${error.message}</p></main>`;
});
