// safety_kpi.js
// Safety KPI Dashboard Metrics

function renderSafetyKPIs(containerId, kpiData) {
    const container = document.getElementById(containerId);
    container.innerHTML = `
        <div class="kpi-grid">
            <div class="kpi-card">
                <h3>Total Hazards</h3>
                <p>${kpiData.totalHazards}</p>
            </div>
            <div class="kpi-card">
                <h3>High Risk Hazards</h3>
                <p>${kpiData.highRiskHazards}</p>
            </div>
            <div class="kpi-card">
                <h3>Near Misses</h3>
                <p>${kpiData.nearMisses}</p>
            </div>
            <div class="kpi-card">
                <h3>Compliance Score</h3>
                <p>${kpiData.complianceScore}%</p>
            </div>
            <div class="kpi-card">
                <h3>Incident Rate</h3>
                <p>${kpiData.incidentRate} / 1000 hrs</p>
            </div>
        </div>
    `;
}

// Example usage:
// const kpiData = {
//     totalHazards: 42,
//     highRiskHazards: 7,
//     nearMisses: 3,
//     complianceScore: 95,
//     incidentRate: 0.8
// };
// renderSafetyKPIs('kpiDashboard', kpiData);

// Add CSS for .kpi-grid and .kpi-card for layout and styling.
