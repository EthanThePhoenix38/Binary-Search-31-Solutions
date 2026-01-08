<div align="center">

# 🔍 Binary Search Solutions

### Professional implementations of binary search algorithms

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Tests](https://github.com/EthanThePhoenix38/Binary-Search-31-Solutions/actions/workflows/tests.yml/badge.svg)](https://github.com/EthanThePhoenix38/Binary-Search-31-Solutions/actions/workflows/tests.yml)

**Forked from:** [super30admin/Binary-Search-31](https://github.com/super30admin/Binary-Search-31)

[Features](#features) •
[Installation](#installation) •
[Usage](#usage) •
[Problems](#problems) •
[Testing](#testing) •
[Contributing](#contributing)

</div>

---

## 🎯 Overview

This repository contains **production-ready, optimized solutions** for binary search algorithm problems from the [super30admin/Binary-Search-31](https://github.com/super30admin/Binary-Search-31) bootcamp. Each solution includes:

- ✅ **Optimal time/space complexity**
- ✅ **Comprehensive documentation**
- ✅ **Full test coverage with pytest**
- ✅ **Type hints and docstrings**
- ✅ **CI/CD with GitHub Actions**
- ✅ **Automated dependency management**

## 📊 Repository Stats

![Stars](https://img.shields.io/github/stars/EthanThePhoenix38/Binary-Search-31-Solutions?style=social)
![Forks](https://img.shields.io/github/forks/EthanThePhoenix38/Binary-Search-31-Solutions?style=social)
![Issues](https://img.shields.io/github/issues/EthanThePhoenix38/Binary-Search-31-Solutions)
![Last Commit](https://img.shields.io/github/last-commit/EthanThePhoenix38/Binary-Search-31-Solutions)
![Repo Size](https://img.shields.io/github/repo-size/EthanThePhoenix38/Binary-Search-31-Solutions)

## ✨ Features

- **🚀 Optimized Algorithms**: All solutions use the most efficient approach
- **📝 Clean Code**: Follows PEP 8 style guide and best practices  
- **🧪 100% Test Coverage**: Comprehensive unit and E2E tests
- **🤖 Auto-Updates**: Dependabot automatically updates dependencies
- **🔒 Security**: No vulnerabilities, all dependencies pinned
- **📚 Documentation**: Every function has detailed docstrings
- **⚡ CI/CD Pipeline**: Automated testing on every commit

## 🛠️ Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Quick Start

```bash
# Clone the repository
git clone https://github.com/EthanThePhoenix38/Binary-Search-31-Solutions.git
cd Binary-Search-31-Solutions

# Install dependencies
pip install -r requirements.txt

# Install the package in development mode
pip install -e .
```

## 💻 Usage

### Problem 1: Optimize Air Routes

```python
from src.problem1_optimize_routes import optimize_air_routes

# Amazon Prime Air routing problem
max_distance = 7000
forward_routes = [[1, 2000], [2, 4000], [3, 6000]]
return_routes = [[1, 2000]]

result = optimize_air_routes(max_distance, forward_routes, return_routes)
print(result)  # Output: [[2, 1]]
```

### Problem 2: H-Index II

```python
from src.problem2_h_index_ii import h_index

# Calculate h-index from sorted citations
citations = [0, 1, 3, 5, 6]
result = h_index(citations)
print(result)  # Output: 3
```

## 📋 Problems

### Problem 1: Optimize Air Routes

**Description**: Find optimal forward and return route pairs that maximize travel distance without exceeding aircraft capacity.

**Complexity**:
- **Time**: `O(n log n + m log m + n*m)`
- **Space**: `O(1)` auxiliary

**Key Concepts**: Two-pointer technique, sorting, greedy algorithm

**LeetCode Link**: [Amazon OA Discussion](https://leetcode.com/discuss/interview-question/1025705/Amazon-or-OA-or-Prime-Air-time/824897)

### Problem 2: H-Index II

**Description**: Calculate the h-index of a researcher given a sorted array of citations.

**Complexity**:
- **Time**: `O(log n)` - Binary search
- **Space**: `O(1)` - Constant space

**Key Concepts**: Binary search, sorted array optimization

**LeetCode Link**: [#275 H-Index II](https://leetcode.com/problems/h-index-ii/)

## 🧪 Testing

### Run All Tests

```bash
# Run all tests with coverage
pytest tests/ --cov=src --cov-report=html

# Run specific test file
pytest tests/test_problem1.py -v

# Run with detailed output
pytest tests/ -vv
```

### Test Structure

```
tests/
├── __init__.py
├── test_problem1.py    # Problem 1 unit + E2E tests
└── test_problem2.py    # Problem 2 unit + E2E tests
```

### Coverage Report

After running tests, open `htmlcov/index.html` to view the detailed coverage report.

## 🏗️ Project Structure

```
Binary-Search-31-Solutions/
├── .github/
│   ├── workflows/
│   │   ├── tests.yml           # CI/CD pipeline
│   │   └── auto-merge.yml      # Dependabot auto-merge
│   └── dependabot.yml          # Dependency updates config
├── src/
│   ├── __init__.py
│   ├── problem1_optimize_routes.py
│   └── problem2_h_index_ii.py
├── tests/
│   ├── __init__.py
│   ├── test_problem1.py
│   └── test_problem2.py
├── .gitignore
├── requirements.txt            # Pinned dependencies
├── setup.py                    # Package configuration
└── README.md                   # This file
```

## 🤖 CI/CD & Automation

### GitHub Actions Workflows

1. **Tests Workflow** (`.github/workflows/tests.yml`)
   - Runs on every push and pull request
   - Tests on Python 3.8, 3.9, 3.10, 3.11
   - Generates coverage report
   - Fails if coverage < 90%

2. **Auto-Merge Workflow** (`.github/workflows/auto-merge.yml`)
   - Automatically approves Dependabot PRs
   - Auto-merges after tests pass
   - No manual intervention needed

### Dependabot Configuration

- **Daily dependency checks**
- **Automatic security updates**
- **No email notifications** (silent updates)
- **Auto-merge enabled** for patch and minor updates

## 🔒 Security

- ✅ **No known vulnerabilities**
- ✅ **All dependencies pinned** to specific versions
- ✅ **Dependabot enabled** for automatic security patches
- ✅ **Regular security audits**

## 📈 Performance

All solutions are benchmarked against standard test cases:

| Problem | Time Complexity | Space Complexity | Avg Runtime |
|---------|----------------|------------------|-------------|
| Optimize Air Routes | O(n log n + m*n) | O(1) | ~0.5ms |
| H-Index II | O(log n) | O(1) | ~0.1ms |

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Setup

```bash
# Install development dependencies
pip install -r requirements.txt
pip install pytest pytest-cov black flake8

# Run code formatter
black src/ tests/

# Run linter
flake8 src/ tests/

# Run tests
pytest tests/ --cov=src
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**EthanThePhoenix38**

- GitHub: [@EthanThePhoenix38](https://github.com/EthanThePhoenix38)
- Original Course: [super30admin/Binary-Search-31](https://github.com/super30admin/Binary-Search-31)

## 🙏 Acknowledgments

- Thanks to [super30admin](https://github.com/super30admin) for the original problem set
- Inspired by real interview questions from top tech companies
- Built with ❤️ using Python

---

<div align="center">

**⭐ Star this repository if you found it helpful! ⭐**

 Made with 🔥 by [EthanThePhoenix38](https://github.com/EthanThePhoenix38)

</div>
