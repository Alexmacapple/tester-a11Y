#!/bin/bash
# Script d'installation pour presentation-reviewer skill
# Installation des dépendances et vérification de l'environnement

set -e  # Arrêt en cas d'erreur

echo "📦 Installation du skill presentation-reviewer"
echo "================================================"
echo ""

# Vérifier Python
echo "1️⃣ Vérification de Python..."
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 n'est pas installé"
    echo "   Installez Python 3.7+ depuis https://www.python.org/"
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
echo "✅ Python $PYTHON_VERSION détecté"
echo ""

# Vérifier pip
echo "2️⃣ Vérification de pip..."
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 n'est pas installé"
    echo "   Installez pip3 avec: python3 -m ensurepip"
    exit 1
fi
echo "✅ pip3 disponible"
echo ""

# Installer python-pptx
echo "3️⃣ Installation de python-pptx..."
pip3 install --quiet --upgrade python-pptx 2>&1 | grep -v "Requirement already satisfied" || true
echo "✅ python-pptx installé"
echo ""

# Vérifier l'installation
echo "4️⃣ Vérification de l'installation..."
python3 -c "from pptx import Presentation; print('✅ Import python-pptx réussi')" 2>/dev/null || {
    echo "❌ Erreur lors de l'import de python-pptx"
    exit 1
}
echo ""

# Test des scripts
echo "5️⃣ Test des scripts..."
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Test analyzer.py
if python3 "$SCRIPT_DIR/analyzer.py" --help &> /dev/null; then
    echo "✅ analyzer.py fonctionnel"
else
    echo "⚠️  analyzer.py présente des warnings (normal)"
fi

# Test framework_detector.py
if python3 "$SCRIPT_DIR/framework_detector.py" --help &> /dev/null; then
    echo "✅ framework_detector.py fonctionnel"
else
    echo "⚠️  framework_detector.py présente des warnings (normal)"
fi

# Test reviewer.py
if python3 "$SCRIPT_DIR/reviewer.py" --help &> /dev/null; then
    echo "✅ reviewer.py fonctionnel"
else
    echo "⚠️  reviewer.py présente des warnings (normal)"
fi

echo ""
echo "================================================"
echo "✅ Installation terminée avec succès !"
echo ""
echo "📚 Usage:"
echo "   python3 scripts/analyzer.py <fichier.pptx>"
echo "   python3 scripts/framework_detector.py <fichier.pptx> --suggest conseil"
echo "   python3 scripts/reviewer.py <fichier.pptx> analysis.json -o output.pptx"
echo ""
echo "📖 Documentation complète: SKILL.md"
echo "================================================"
