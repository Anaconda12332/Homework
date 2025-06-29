import pytest
import app.analyzer as analyzer


def test_contains_urgent(clean_messages):
    assert analyzer.contains_urgent(clean_messages) is True


def test_get_average_length(clean_messages):
    avg = analyzer.get_average_length(clean_messages)
    assert isinstance(avg, float)
    assert avg > 0
    assert round(avg) == round(sum(len(m) for m in clean_messages) / len(clean_messages))


def test_print_summary_output(capsys, default_messages):
    analyzer.print_summary(default_messages)
    captured = capsys.readouterr()
    assert "Total messages: 5" in captured.out
    assert "Empty messages: 2" in captured.out
    assert "Longest message:" in captured.out


def test_count_keywords(clean_messages):
    result = analyzer.count_keywords(clean_messages, 'urgent')
    assert result == 1


def test_count_keywords_empty():
    assert analyzer.count_keywords([], 'urgent') == 0


@pytest.mark.parametrize('kw, expected', [
    ('urgent', 1),
    ('hello', 1),
    ('random', 0),
])
def test_keywords_param(clean_messages, kw, expected):
    assert analyzer.count_keywords(clean_messages, kw) == expected


def test_sum_empty_messages(clean_messages):
    result = analyzer.sum_empty_messages(clean_messages)
    assert result == 2
