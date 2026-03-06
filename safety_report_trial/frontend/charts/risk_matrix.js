// risk_matrix.js
// Risk Matrix Visualization for WHS Safety Reports
// Severity vs Likelihood

// Requires Chart.js (or similar library)
// Usage: riskMatrixChart('canvasId', matrixData)

function riskMatrixChart(canvasId, matrixData) {
    const ctx = document.getElementById(canvasId).getContext('2d');
    const severityLabels = matrixData.severity;
    const likelihoodLabels = matrixData.likelihood;
    const values = matrixData.values; // 2D array: values[severity][likelihood]

    new Chart(ctx, {
        type: 'heatmap', // Custom type, fallback to 'matrix' or 'bubble' if not supported
        data: {
            labels: likelihoodLabels,
            datasets: severityLabels.map((sev, i) => ({
                label: sev,
                data: values[i],
                backgroundColor: values[i].map(val => riskColor(val)),
            }))
        },
        options: {
            plugins: {
                title: {
                    display: true,
                    text: 'Risk Matrix (Severity vs Likelihood)'
                }
            },
            scales: {
                x: {
                    title: { display: true, text: 'Likelihood' },
                    ticks: { autoSkip: false }
                },
                y: {
                    title: { display: true, text: 'Severity' },
                    ticks: { autoSkip: false }
                }
            }
        }
    });
}

function riskColor(value) {
    // Example: 1=green, 2=yellow, 3=orange, 4=red
    if (value <= 1) return '#4caf50'; // Low
    if (value == 2) return '#ffeb3b'; // Medium
    if (value == 3) return '#ff9800'; // High
    return '#f44336'; // Extreme
}

// Example matrixData:
// const matrixData = {
//     severity: ['Minor', 'Moderate', 'Major', 'Catastrophic'],
//     likelihood: ['Rare', 'Unlikely', 'Possible', 'Likely', 'Almost Certain'],
//     values: [
//         [1, 1, 2, 2, 3],
//         [1, 2, 2, 3, 3],
//         [2, 2, 3, 3, 4],
//         [2, 3, 3, 4, 4]
//     ]
// };
// riskMatrixChart('riskMatrixCanvas', matrixData);
