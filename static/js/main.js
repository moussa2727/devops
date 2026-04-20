// Convertisseur de Devises - JavaScript principal

// Éléments DOM
const devise1 = document.getElementById('devise1');
const devise2 = document.getElementById('devise2');
const montant1 = document.getElementById('montant1');
const montant2 = document.getElementById('montant2');
const inverserBtn = document.getElementById('inverserBtn');
const infoTaux = document.getElementById('infoTaux');
const tauxDirect = document.getElementById('tauxDirect');
const errorMessage = document.getElementById('errorMessage');
const errorText = document.getElementById('errorText');

// Taux depuis le serveur (injectés par Flask via Jinja)
let TAUX = {};

// Initialisation des taux
function initTaux(tauxData) {
    TAUX = tauxData;
    updateTauxInfo();
}

// Afficher une erreur
function showError(message) {
    if (errorText && errorMessage) {
        errorText.textContent = message;
        errorMessage.classList.remove('hidden');
        setTimeout(function () {
            errorMessage.classList.add('hidden');
        }, 3000);
    }
}

// Mettre à jour les informations des taux
function updateTauxInfo() {
    if (!TAUX || Object.keys(TAUX).length === 0) return;

    const d1 = devise1 ? devise1.value : '';
    const d2 = devise2 ? devise2.value : '';

    if (!d1 || !d2) return;
    if (!TAUX[d1] || !TAUX[d2]) return;

    const taux1 = TAUX[d1].taux;
    const taux2 = TAUX[d2].taux;
    const tauxDirectValue = (taux2 / taux1).toFixed(4);

    if (infoTaux) {
        infoTaux.innerHTML = '<span class="font-medium">' + d1 + '</span> → <span class="font-medium">' + d2 + '</span>';
    }
    if (tauxDirect) {
        tauxDirect.innerHTML = '1 ' + d1 + ' = ' + tauxDirectValue + ' ' + d2;
    }
}

// Effectuer la conversion
async function convertir() {
    if (!montant1 || !montant2) return;

    const montant = parseFloat(montant1.value);

    if (isNaN(montant) || montant1.value === '') {
        montant2.value = '';
        return;
    }

    try {
        const response = await fetch('/api/convert', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                montant: montant,
                devise1: devise1.value,
                devise2: devise2.value
            })
        });

        const data = await response.json();

        if (data.success) {
            montant2.value = data.resultat.toLocaleString('fr-FR', {
                minimumFractionDigits: 2,
                maximumFractionDigits: 2
            });
            if (errorMessage) {
                errorMessage.classList.add('hidden');
            }
        } else {
            showError(data.error);
            montant2.value = '';
        }
    } catch (err) {
        showError('Erreur de connexion au serveur');
        montant2.value = '';
    }
}

// Inverser les devises
function inverser() {
    if (!devise1 || !devise2) return;

    const tempDevise = devise1.value;
    const tempMontant = montant2 ? montant2.value : '';

    devise1.value = devise2.value;
    devise2.value = tempDevise;

    if (tempMontant && tempMontant !== '') {
        if (montant1) {
            montant1.value = tempMontant.replace(',', '.');
        }
        convertir();
    } else {
        if (montant1) montant1.value = '';
        if (montant2) montant2.value = '';
    }

    updateTauxInfo();
}

// Attacher les événements
function attachEvents() {
    if (montant1) {
        montant1.addEventListener('input', convertir);
    }

    if (devise1) {
        devise1.addEventListener('change', function () {
            convertir();
            updateTauxInfo();
        });
    }

    if (devise2) {
        devise2.addEventListener('change', function () {
            convertir();
            updateTauxInfo();
        });
    }

    if (inverserBtn) {
        inverserBtn.addEventListener('click', inverser);
    }
}

// Initialisation quand le DOM est chargé
document.addEventListener('DOMContentLoaded', function () {
    attachEvents();
    updateTauxInfo();
});

// Exporter les fonctions pour une utilisation globale
window.convertisseur = {
    initTaux: initTaux,
    convertir: convertir,
    inverser: inverser,
    updateTauxInfo: updateTauxInfo
};