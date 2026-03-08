import Chart from 'chart.js/auto';

let sportsData = [];
let familyAverages = {};
let chart = null;
let familyChart = null;
let currentSort = { key: 'total_rank', direction: 'desc' };

async function init() {
    try {
        const response = await fetch('./ranked_sports.json');
        sportsData = await response.json();

        calculateFamilyAverages();
        populateTable(sportsData);
        populateSelects();
        populateFamilyFilter();
        initCharts();
        setupModal();

        document.getElementById('sport1-select').addEventListener('change', updateIndividualChart);
        document.getElementById('sport2-select').addEventListener('change', updateIndividualChart);
        document.getElementById('family1-select').addEventListener('change', updateFamilyChart);
        document.getElementById('family2-select').addEventListener('change', updateFamilyChart);
        document.getElementById('sport-search').addEventListener('input', applySortAndPopulate);
        document.getElementById('family-filter').addEventListener('change', applySortAndPopulate);

        document.querySelectorAll('th[data-sort]').forEach(th => {
            th.addEventListener('click', () => {
                const key = th.dataset.sort;
                if (currentSort.key === key) {
                    currentSort.direction = currentSort.direction === 'asc' ? 'desc' : 'asc';
                } else {
                    currentSort.key = key;
                    currentSort.direction = 'desc';
                }
                updateSortUI();
                applySortAndPopulate();
            });
        });

        updateSortUI();

    } catch (error) {
        console.error('Error loading sports data:', error);
    }
}

function calculateFamilyAverages() {
    const families = {};
    sportsData.forEach(sport => {
        sport.families.forEach(family => {
            if (!families[family]) {
                families[family] = {
                    count: 0,
                    scores: {
                        endurance: 0, strength: 0, power: 0, speed: 0, agility: 0,
                        flexibility: 0, nerve: 0, durability: 0, hand_eye: 0, analytic: 0
                    }
                };
            }
            families[family].count++;
            Object.keys(families[family].scores).forEach(cat => {
                families[family].scores[cat] += sport.scores[cat];
            });
        });
    });

    Object.keys(families).forEach(family => {
        familyAverages[family] = { scores: {} };
        Object.keys(families[family].scores).forEach(cat => {
            familyAverages[family].scores[cat] = families[family].scores[cat] / families[family].count;
        });
    });
}

function initCharts() {
    const categories = ["Aerobic Cap.", "Force Prod.", "Power", "Speed", "Agility", "Flexibility", "Resilience", "Durability", "Visual React.", "Tactical Comp."];
    
    const commonOptions = {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
            r: {
                angleLines: { color: 'rgba(255, 255, 255, 0.1)' },
                grid: { color: 'rgba(255, 255, 255, 0.1)' },
                pointLabels: { color: '#a0a0a0', font: { size: 11 } },
                ticks: { display: false, max: 10, min: 0, stepSize: 2 }
            }
        },
        plugins: {
            legend: { labels: { color: '#fff', font: { family: 'Outfit', size: 14, weight: 'bold' } } }
        }
    };

    // 1. Individual Radar Chart
    const ctx = document.getElementById('radarChart');
    chart = new Chart(ctx, {
        type: 'radar',
        data: {
            labels: categories,
            datasets: [
                { label: sportsData[0].name, data: Object.values(sportsData[0].scores), fill: true, backgroundColor: 'rgba(0, 242, 255, 0.2)', borderColor: '#00f2ff', pointBackgroundColor: '#00f2ff' },
                { label: sportsData[1].name, data: Object.values(sportsData[1].scores), fill: true, backgroundColor: 'rgba(255, 0, 110, 0.2)', borderColor: '#ff006e', pointBackgroundColor: '#ff006e' }
            ]
        },
        options: commonOptions
    });

    // 2. Family Radar Chart
    const fCtx = document.getElementById('familyChart');
    const fam1 = sportsData[0].families[0];
    const fam2 = sportsData[1].families[0];

    familyChart = new Chart(fCtx, {
        type: 'radar',
        data: {
            labels: categories,
            datasets: [
                { label: fam1 + " (Avg)", data: Object.values(familyAverages[fam1].scores), fill: true, backgroundColor: 'rgba(0, 242, 255, 0.2)', borderColor: '#00f2ff', borderDash: [5, 5] },
                { label: fam2 + " (Avg)", data: Object.values(familyAverages[fam2].scores), fill: true, backgroundColor: 'rgba(255, 0, 110, 0.2)', borderColor: '#ff006e', borderDash: [5, 5] }
            ]
        },
        options: commonOptions
    });
}

function updateIndividualChart() {
    const s1Name = document.getElementById('sport1-select').value;
    const s2Name = document.getElementById('sport2-select').value;
    const s1Data = sportsData.find(s => s.name === s1Name);
    const s2Data = sportsData.find(s => s.name === s2Name);
    
    chart.data.datasets[0].label = s1Name;
    chart.data.datasets[0].data = Object.values(s1Data.scores);
    chart.data.datasets[1].label = s2Name;
    chart.data.datasets[1].data = Object.values(s2Data.scores);
    chart.update();

    document.getElementById('family1-select').value = s1Data.families[0];
    document.getElementById('family2-select').value = s2Data.families[0];
    updateFamilyChart();
}

function updateFamilyChart() {
    const f1 = document.getElementById('family1-select').value;
    const f2 = document.getElementById('family2-select').value;

    familyChart.data.datasets[0].label = f1 + " (Avg)";
    familyChart.data.datasets[0].data = Object.values(familyAverages[f1].scores);
    familyChart.data.datasets[1].label = f2 + " (Avg)";
    familyChart.data.datasets[1].data = Object.values(familyAverages[f2].scores);
    familyChart.update();
}

function setupModal() {
    const modal = document.getElementById('detail-modal');
    const span = document.getElementsByClassName('close-button')[0];
    span.onclick = () => modal.style.display = 'none';
    window.onclick = (event) => { if (event.target == modal) modal.style.display = 'none'; };
}

function showSportDetail(sportName) {
    const sport = sportsData.find(s => s.name === sportName);
    if (!sport) return;
    const modal = document.getElementById('detail-modal');
    const body = document.getElementById('modal-body');
    body.innerHTML = `
        <div class="detail-header">
            <h2>${sport.name}</h2>
            <div class="multiplier-tag">Matrix Score: ${sport.total_rank.toFixed(1)} / 100</div>
        </div>
        <div class="detail-grid">
            <div class="detail-card">
                <h3>Physiological Base (60%)</h3>
                <div class="stat-row"><span class="stat-label">Aerobic Capacity:</span> <span class="stat-value">${sport.scores.endurance.toFixed(1)}</span></div>
                <div class="stat-row"><span class="stat-label">Force Production:</span> <span class="stat-value">${sport.scores.strength.toFixed(1)}</span></div>
                <div class="stat-row"><span class="stat-label">Power:</span> <span class="stat-value">${sport.scores.power.toFixed(1)}</span></div>
                <div class="stat-row"><span class="stat-label">Speed:</span> <span class="stat-value">${sport.scores.speed.toFixed(1)}</span></div>
                <div class="stat-row"><span class="stat-label">Agility:</span> <span class="stat-value">${sport.scores.agility.toFixed(1)}</span></div>
                <div class="stat-row" style="border:none; margin-top:0.5rem; font-weight:bold;">
                    <span class="stat-label">Weighted Subtotal:</span> <span class="stat-value">${sport.breakdown.physical_base.toFixed(2)}</span>
                </div>
            </div>
            <div class="detail-card">
                <h3>Technical & Nerve (40%)</h3>
                <div class="stat-row"><span class="stat-label">Flexibility:</span> <span class="stat-value">${sport.scores.flexibility.toFixed(1)}</span></div>
                <div class="stat-row"><span class="stat-label">Stress Resilience:</span> <span class="stat-value">${sport.scores.nerve.toFixed(1)}</span></div>
                <div class="stat-row"><span class="stat-label">Durability:</span> <span class="stat-value">${sport.scores.durability.toFixed(1)}</span></div>
                <div class="stat-row"><span class="stat-label">Visual Reaction:</span> <span class="stat-value">${sport.scores.hand_eye.toFixed(1)}</span></div>
                <div class="stat-row"><span class="stat-label">Tactical Complexity:</span> <span class="stat-value">${sport.scores.analytic.toFixed(1)}</span></div>
                <div class="stat-row" style="border:none; margin-top:0.5rem; font-weight:bold;">
                    <span class="stat-label">Weighted Subtotal:</span> <span class="stat-value">${sport.breakdown.skill_base.toFixed(2)}</span>
                </div>
            </div>
            <div class="detail-card">
                <h3>Raw Scientific Benchmarks</h3>
                <div class="stat-row"><span class="stat-label">Peak G-Force:</span> <span class="stat-value">${sport.raw.g_load} Gs</span></div>
                <div class="stat-row"><span class="stat-label">Deg. of Freedom:</span> <span class="stat-value">${sport.raw.dof} DoF</span></div>
                <div class="stat-row"><span class="stat-label">Metabolic Rate:</span> <span class="stat-value">${sport.raw.metabolic_demand} METs</span></div>
                <div class="stat-row"><span class="stat-label">Scarcity Index:</span> <span class="stat-value">${sport.raw.scarcity} / 10</span></div>
            </div>
            <div class="detail-card">
                <h3>Data Reliability</h3>
                <div class="coverage-header">
                    <span>Evidence Quality</span>
                    <span>${sport.confidence}%</span>
                </div>
                <div class="coverage-bar-bg">
                    <div class="coverage-bar-fill" style="width: ${sport.confidence}%"></div>
                </div>
                <div class="evidence-source">Source: ${sport.evidence}</div>
                ${sport.justification ? `<div class="evidence-source" style="margin-top:1rem; color:var(--accent);">Note: ${sport.justification}</div>` : ''}
            </div>
        </div>
    `;
    modal.style.display = 'block';
}

function updateSortUI() {
    document.querySelectorAll('th[data-sort]').forEach(th => {
        th.classList.remove('sort-active', 'sort-asc', 'sort-desc');
        if (th.dataset.sort === currentSort.key) {
            th.classList.add('sort-active', `sort-${currentSort.direction}`);
        }
    });
}

function applySortAndPopulate() {
    const term = document.getElementById('sport-search').value.toLowerCase();
    const selectedFamily = document.getElementById('family-filter').value;
    const sourceData = sportsData.filter(s => {
        const matchesSearch = s.name.toLowerCase().includes(term);
        const matchesFamily = selectedFamily === 'all' || (s.families && s.families.includes(selectedFamily));
        return matchesSearch && matchesFamily;
    });
    const sorted = [...sourceData].sort((a, b) => {
        let valA, valB;
        if (currentSort.key === 'rank') {
            valA = sportsData.findIndex(s => s.name === a.name);
            valB = sportsData.findIndex(s => s.name === b.name);
        } else if (currentSort.key === 'name') {
            valA = a.name; valB = b.name;
        } else if (currentSort.key === 'total_rank') {
            valA = a.total_rank; valB = b.total_rank;
        } else if (currentSort.key === 'confidence') {
            valA = a.confidence; valB = b.confidence;
        } else {
            valA = a.scores[currentSort.key];
            valB = b.scores[currentSort.key];
        }
        if (valA < valB) return currentSort.direction === 'asc' ? -1 : 1;
        if (valA > valB) return currentSort.direction === 'asc' ? 1 : -1;
        return 0;
    });
    populateTable(sorted);
}

function getConfidenceColor(conf) {
    if (conf >= 95) return '#00f2ff';
    if (conf >= 85) return '#00ff88';
    if (conf >= 75) return '#ffcc00';
    return '#ff006e';
}

function populateTable(data) {
    const tbody = document.getElementById('ranking-body');
    tbody.innerHTML = '';
    data.forEach((sport) => {
        const actualRank = sportsData.findIndex(s => s.name === sport.name) + 1;
        const tr = document.createElement('tr');
        const scoreCells = Object.entries(sport.scores).map(([cat, score]) => `<td>${score.toFixed(1)}</td>`).join('');
        const confColor = getConfidenceColor(sport.confidence);
        tr.innerHTML = `
            <td><span class="rank-badge">${actualRank}</span></td>
            <td style="font-weight: 600">${sport.name}</td>
            <td class="score">${sport.total_rank.toFixed(1)}</td>
            ${scoreCells}
            <td style="color: ${confColor}; font-weight: bold; font-size: 0.75rem">${sport.confidence}%</td>
            <td><button class="info-btn">i</button></td>
        `;
        tr.addEventListener('click', () => showSportDetail(sport.name));
        tr.querySelector('.info-btn').addEventListener('click', (e) => { e.stopPropagation(); showSportDetail(sport.name); });
        tbody.appendChild(tr);
    });
}

function populateSelects() {
    const s1 = document.getElementById('sport1-select');
    const s2 = document.getElementById('sport2-select');
    const f1 = document.getElementById('family1-select');
    const f2 = document.getElementById('family2-select');
    sportsData.forEach(sport => {
        s1.add(new Option(sport.name, sport.name));
        s2.add(new Option(sport.name, sport.name));
    });
    Object.keys(familyAverages).sort().forEach(family => {
        f1.add(new Option(family, family));
        f2.add(new Option(family, family));
    });
    s1.value = sportsData[0].name; s2.value = sportsData[1].name;
    f1.value = sportsData[0].families[0]; f2.value = sportsData[1].families[0];
}

function populateFamilyFilter() {
    const familyFilter = document.getElementById('family-filter');
    const allFamilies = new Set();
    sportsData.forEach(sport => { if (sport.families) sport.families.forEach(f => allFamilies.add(f)); });
    Array.from(allFamilies).sort().forEach(family => familyFilter.add(new Option(family, family)));
}

window.addEventListener('DOMContentLoaded', init);
