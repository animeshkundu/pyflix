#!/bin/bash
# Description: Run all validation checks (linting, formatting, tests)
# Usage: ./scripts/validate.sh [options]
#
# Options:
#   --lint-only    Run only linting checks
#   --test-only    Run only tests
#   --verbose      Show detailed output
#   --help         Show this help message
#
# Exit codes:
#   0 - All checks passed
#   1 - One or more checks failed

set -euo pipefail

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

# Default options
LINT_ONLY=false
TEST_ONLY=false
VERBOSE=false

# Parse arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --lint-only)
            LINT_ONLY=true
            shift
            ;;
        --test-only)
            TEST_ONLY=true
            shift
            ;;
        --verbose)
            VERBOSE=true
            shift
            ;;
        --help)
            head -20 "$0" | tail -18
            exit 0
            ;;
        *)
            echo -e "${RED}Unknown option: $1${NC}"
            exit 1
            ;;
    esac
done

cd "$PROJECT_ROOT"

echo "🔍 Starting validation checks..."
echo ""

# Track failures
FAILED=0

# Function to run a check
run_check() {
    local name="$1"
    local command="$2"
    
    echo -n "  $name... "
    
    if $VERBOSE; then
        echo ""
        if eval "$command"; then
            echo -e "  ${GREEN}✓ $name passed${NC}"
        else
            echo -e "  ${RED}✗ $name failed${NC}"
            FAILED=$((FAILED + 1))
        fi
    else
        if eval "$command" > /dev/null 2>&1; then
            echo -e "${GREEN}✓${NC}"
        else
            echo -e "${RED}✗${NC}"
            FAILED=$((FAILED + 1))
        fi
    fi
}

# Linting checks
run_linting() {
    echo "📋 Running linting checks..."
    
    # Check if linting tools are installed
    if ! command -v flake8 &> /dev/null; then
        echo -e "${YELLOW}  ⚠ flake8 not installed, skipping...${NC}"
    else
        run_check "flake8" "flake8 torrent utils --max-line-length=120 --extend-ignore=E501"
    fi
    
    if ! command -v black &> /dev/null; then
        echo -e "${YELLOW}  ⚠ black not installed, skipping...${NC}"
    else
        run_check "black" "black --check torrent utils --line-length=120 --quiet"
    fi
    
    if ! command -v isort &> /dev/null; then
        echo -e "${YELLOW}  ⚠ isort not installed, skipping...${NC}"
    else
        run_check "isort" "isort --check-only torrent utils --profile black --quiet"
    fi
    
    echo ""
}

# Testing checks
run_tests() {
    echo "🧪 Running tests..."
    
    if ! command -v pytest &> /dev/null; then
        echo -e "${YELLOW}  ⚠ pytest not installed, skipping tests...${NC}"
        echo -e "${YELLOW}  Install with: pip install pytest pytest-cov${NC}"
        return
    fi
    
    if [ -d "tests" ] && [ "$(ls -A tests 2>/dev/null)" ]; then
        run_check "pytest" "pytest tests/ --cov=torrent --cov=utils --cov-report=term-missing --cov-fail-under=90"
    else
        echo -e "${YELLOW}  ⚠ No tests found in tests/ directory${NC}"
    fi
    
    echo ""
}

# Main execution
if [ "$TEST_ONLY" = true ]; then
    run_tests
elif [ "$LINT_ONLY" = true ]; then
    run_linting
else
    run_linting
    run_tests
fi

# Summary
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
if [ $FAILED -eq 0 ]; then
    echo -e "${GREEN}✓ All validation checks passed!${NC}"
    exit 0
else
    echo -e "${RED}✗ $FAILED check(s) failed${NC}"
    exit 1
fi
