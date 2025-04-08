function formatRecommendations(recommendations) {
    let html = '<div class="space-y-6">';
    const query = elements.queryInput.value.trim();

    // Medications Section
    if (recommendations.medications?.length > 0) {
        html += `
            <div class="medication-card p-4 rounded-xl border border-amber-500/20">
                <h3 class="text-lg font-semibold text-amber-400 mb-3">
                    💊 Medications for "${query}"
                </h3>
                <div class="space-y-4">
                    ${recommendations.medications.map(med => `
                        <div class="bg-gray-900/30 p-3 rounded-lg">
                            <div class="font-medium text-white">${med.name}</div>
                            ${med.dosage ? `<div class="text-sm text-amber-300">Dosage: ${med.dosage}</div>` : ''}
                            ${med.purpose ? `<div class="text-sm text-gray-400 mt-1">Purpose: ${med.purpose}</div>` : ''}
                        </div>
                    `).join('')}
                </div>
            </div>`;
    }

    // Treatment Plan Section
    if (recommendations.treatments?.length > 0) {
        html += `
            <div class="treatment-card p-4 rounded-xl border border-green-500/20 bg-green-900/10">
                <h3 class="text-lg font-semibold text-green-400 mb-3">🏥 Treatment Plan</h3>
                <ul class="list-disc pl-6 space-y-2 text-white">
                    ${recommendations.treatments.map(t => `<li>${t}</li>`).join('')}
                </ul>
            </div>`;
    }

    // Precautions Section
    if (recommendations.precautions?.length > 0) {
        html += `
            <div class="precaution-card p-4 rounded-xl border border-red-500/20 bg-red-900/10">
                <h3 class="text-lg font-semibold text-red-400 mb-3">⚠️ Precautions</h3>
                <ul class="list-disc pl-6 space-y-2 text-white">
                    ${recommendations.precautions.map(p => `<li>${p}</li>`).join('')}
                </ul>
            </div>`;
    }

    // Follow-Up Protocol Section
    if (recommendations.follow_up?.length > 0) {
        html += `
            <div class="followup-card p-4 rounded-xl border border-blue-500/20 bg-blue-900/10">
                <h3 class="text-lg font-semibold text-blue-400 mb-3">📅 Follow-Up Protocol</h3>
                <ul class="list-disc pl-6 space-y-2 text-white">
                    ${recommendations.follow_up.map(f => `<li>${f}</li>`).join('')}
                </ul>
            </div>`;
    }

    html += '</div>';
    return html;
}
