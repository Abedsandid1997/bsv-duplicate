import pytest
from src.util.parser import parse, Article
from src.util.detector import detect_duplicates

# Test data
SINGLE_ARTICLE = """
@article{key1,
  author = {Author},
  title = {Title}
}
"""

DUPLICATE_KEYS_NO_DOI = """
@article{key1,
  author = {Author},
  title = {Title}
}
@article{key1,
  author = {Author},
  title = {Title}
}
"""

DIFFERENT_KEYS_NO_DOI = """
@article{key1,
  author = {Author},
  title = {Title}
}
@article{key2,
  author = {Author},
  title = {Title}
}
"""

DUPLICATE_KEYS_AND_DOIS = """
@article{key1,
  author = {Author},
  title = {Title},
  doi = {10.1234/5678}
}
@article{key1,
  author = {Author},
  title = {Title},
  doi = {10.1234/5678}
}
"""

DIFFERENT_KEYS_DIFFERENT_DOIS = """
@article{key1,
  author = {Author},
  title = {Title},
  doi = {10.1234/5678}
}
@article{key2,
  author = {Author},
  title = {Title},
  doi = {10.1234/9999}
}
"""

DIFFERENT_KEYS_SAME_DOIS = """
@article{key1,
  author = {Author},
  title = {Title},
  doi = {10.1234/5678}
}
@article{key2,
  author = {Author},
  title = {Title},
  doi = {10.1234/5678}
}
"""

SAME_KEYS_DIFFERENT_DOIS = """
@article{key1,
  author = {Author},
  title = {Title},
  doi = {10.1234/5678}
}
@article{key1,
  author = {Author},
  title = {Title},
  doi = {10.1234/9999}
}
"""

# Test cases
def test_empty_input():
    """TC1: Test with 0 articles (should raise ValueError)"""
    with pytest.raises(ValueError):
        detect_duplicates("")

def test_duplicate_keys_no_doi():
    """TC2: 2 articles, no DOIs, same keys -> duplicates"""
    result = detect_duplicates(DUPLICATE_KEYS_NO_DOI)
    assert len(result) > 0

def test_different_keys_no_doi():
    """TC3: 2 articles, no DOIs, different keys -> no duplicates"""
    result = detect_duplicates(DIFFERENT_KEYS_NO_DOI)
    assert len(result) == 0

def test_duplicate_keys_and_dois():
    """TC4: 2 articles, both have DOIs, same keys and DOIs -> duplicates"""
    result = detect_duplicates(DUPLICATE_KEYS_AND_DOIS)
    assert len(result) > 0

def test_different_keys_and_dois():
    """TC5: 2 articles, both have DOIs, different keys and DOIs -> no duplicates"""
    result = detect_duplicates(DIFFERENT_KEYS_DIFFERENT_DOIS)
    assert len(result) == 0

def test_different_keys_same_dois():
    """TC6: 2 articles, both have DOIs, different keys but same DOIs -> duplicates"""
    result = detect_duplicates(DIFFERENT_KEYS_SAME_DOIS)
    assert len(result) > 0

def test_same_keys_different_dois():
    """TC7: 2 articles, both have DOIs, same keys but different DOIs -> duplicates"""
    result = detect_duplicates(SAME_KEYS_DIFFERENT_DOIS)
    assert len(result) > 0

"""
Test Structure Explanation:
1. I created separate test data strings for each test case scenario
2. Each test function corresponds to one test case from the table
3. Tests are named descriptively to match the test case conditions

Test Independence:
1. Each test uses its own test data
2. No shared state between tests
3. No test depends on the execution of another test

Challenges Faced:
1. Creating valid BibTeX format strings for each test case
2. Determining the exact expected output format (used simple length checks)
3. Handling the DOI comparison logic correctly in test cases
"""