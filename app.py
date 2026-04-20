from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = 'votre-cle-secrete-pour-production'

# Taux de change (1 euro comme base)
TAUX = {
    "Euro": {"code": "EUR", "taux": 1, "symbole": "€"},
    "Dirham (MAD)": {"code": "MAD", "taux": 11.0, "symbole": "DH"},
    "CFA (XOF)": {"code": "XOF", "taux": 655.96, "symbole": "CFA"}
}

@app.route('/')
def index():
    """Page principale du convertisseur"""
    return render_template('index.html', taux=TAUX)

@app.route('/api/convert', methods=['POST'])
def convert():
    """
    API de conversion de devises
    Attend: {montant, devise1, devise2}
    Retourne: {success, resultat, info}
    """
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({'success': False, 'error': 'Données invalides'}), 400
        
        montant = float(data.get('montant', 0))
        devise1 = data.get('devise1')
        devise2 = data.get('devise2')
        
        if devise1 not in TAUX or devise2 not in TAUX:
            return jsonify({'success': False, 'error': 'Devise inconnue'}), 400
        
        taux1 = TAUX[devise1]['taux']
        taux2 = TAUX[devise2]['taux']
        en_euro = montant / taux1
        resultat = en_euro * taux2
        
        return jsonify({
            'success': True,
            'resultat': round(resultat, 2),
            'devise1': devise1,
            'devise2': devise2,
            'taux_direct': round(taux2 / taux1, 4)
        })
        
    except ValueError:
        return jsonify({'success': False, 'error': 'Montant invalide'}), 400
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/taux', methods=['GET'])
def get_taux():
    """Retourne les taux de change actuels"""
    return jsonify({
        'success': True,
        'taux': {devise: info['taux'] for devise, info in TAUX.items()}
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)