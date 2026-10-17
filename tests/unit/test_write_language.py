"""write.language: an optional output-language instruction for the distill sheet."""

from agent_memory.core import prompts
from agent_memory.core.config import Config


def _sheet(**kwargs):
    return prompts.distill_sheet("types", "sheet", "conversation", **kwargs)


def test_no_language_by_default_keeps_the_prompt_unchanged():
    assert "Write every abstract and body in" not in _sheet()
    assert Config.default().write.language == ""


def test_language_adds_one_instruction_and_protects_identifiers():
    rendered = _sheet(language="简体中文")
    assert "Write every abstract and body in 简体中文" in rendered
    assert "Keep code identifiers" in rendered


def test_blank_language_is_treated_as_unset():
    assert _sheet(language="   ") == _sheet()
