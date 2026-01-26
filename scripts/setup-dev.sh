#!/bin/bash
# Description: Set up development environment for pyflix
# Usage: ./scripts/setup-dev.sh
#
# This script:
#   1. Creates a Python virtual environment
#   2. Installs project dependencies
#   3. Installs development dependencies
#   4. Sets up pre-commit hooks (if available)

set -euo pipefail

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

# Script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

cd "$PROJECT_ROOT"

echo "🚀 Setting up pyflix development environment..."
echo ""

# Check Python version
PYTHON_VERSION=$(python3 --version 2>&1 | cut -d' ' -f2 | cut -d'.' -f1,2)
echo "📦 Python version: $PYTHON_VERSION"

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
    echo -e "${GREEN}✓ Virtual environment created${NC}"
else
    echo -e "${YELLOW}⚠ Virtual environment already exists${NC}"
fi

# Activate virtual environment
echo "📦 Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "📦 Upgrading pip..."
pip install --upgrade pip > /dev/null

# Install project dependencies
echo "📦 Installing project dependencies..."
pip install -r requirements.txt > /dev/null
echo -e "${GREEN}✓ Project dependencies installed${NC}"

# Install development dependencies
echo "📦 Installing development dependencies..."
pip install \
    pytest \
    pytest-cov \
    flake8 \
    black \
    isort \
    mypy \
    > /dev/null
echo -e "${GREEN}✓ Development dependencies installed${NC}"

# Create tests directory if it doesn't exist
if [ ! -d "tests" ]; then
    echo "📦 Creating tests directory..."
    mkdir -p tests
    touch tests/__init__.py
    echo -e "${GREEN}✓ Tests directory created${NC}"
fi

# Set up pre-commit if config exists
if [ -f ".pre-commit-config.yaml" ]; then
    if command -v pre-commit &> /dev/null; then
        echo "📦 Setting up pre-commit hooks..."
        pre-commit install > /dev/null
        echo -e "${GREEN}✓ Pre-commit hooks installed${NC}"
    else
        echo -e "${YELLOW}⚠ pre-commit not installed, skipping hook setup${NC}"
    fi
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo -e "${GREEN}✓ Development environment ready!${NC}"
echo ""
echo "To activate the virtual environment:"
echo "  source venv/bin/activate"
echo ""
echo "To run validation checks:"
echo "  ./scripts/validate.sh"
echo ""
