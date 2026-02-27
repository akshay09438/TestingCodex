#!/usr/bin/env python3
"""Bhagavad Gita Daily Learning application.

Usage:
  python gita_daily_app.py           # show today's learning
  python gita_daily_app.py --date 2026-02-27
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from datetime import date, datetime
from typing import Sequence


@dataclass(frozen=True)
class Learning:
    chapter_verse: str
    theme: str
    lesson: str
    practice: str


LEARNINGS: Sequence[Learning] = (
    Learning(
        chapter_verse="2.47",
        theme="Focus on action, not outcomes",
        lesson=(
            "You are responsible for your effort, not guaranteed results. "
            "Detach from anxiety around success or failure."
        ),
        practice="Choose one key task today and commit to doing it with full attention.",
    ),
    Learning(
        chapter_verse="2.14",
        theme="Endure change with balance",
        lesson="Pleasure and pain are temporary. Build steadiness instead of reactivity.",
        practice="When discomfort appears, pause for three breaths before responding.",
    ),
    Learning(
        chapter_verse="2.50",
        theme="Yoga is skill in action",
        lesson="Act with presence, clarity, and ethics; that is practical spirituality.",
        practice="Before each meeting, set a one-line intention: 'I will be calm and useful.'",
    ),
    Learning(
        chapter_verse="3.19",
        theme="Do your duty selflessly",
        lesson="Consistent, sincere work without ego purifies the mind.",
        practice="Do one helpful task today without telling anyone.",
    ),
    Learning(
        chapter_verse="3.30",
        theme="Offer actions to a higher purpose",
        lesson="When work is offered in service, mental burden reduces.",
        practice="Dedicate today's work to service, growth, or gratitude.",
    ),
    Learning(
        chapter_verse="4.7-8",
        theme="Dharma is restored through right action",
        lesson="Whenever confusion rises, choose the action that protects truth and compassion.",
        practice="In one decision today, prioritize integrity over convenience.",
    ),
    Learning(
        chapter_verse="4.13",
        theme="Honor your nature and role",
        lesson="Work aligned with your qualities brings deeper fulfillment than imitation.",
        practice="Spend 15 minutes on a strength-based task that energizes you.",
    ),
    Learning(
        chapter_verse="4.38",
        theme="Knowledge purifies",
        lesson="Steady study and reflection dissolve confusion over time.",
        practice="Read one meaningful paragraph and journal one insight.",
    ),
    Learning(
        chapter_verse="5.10",
        theme="Work without attachment",
        lesson="Like a lotus untouched by water, stay inwardly free while active in life.",
        practice="Notice one moment of stress and release the need to control outcomes.",
    ),
    Learning(
        chapter_verse="5.18",
        theme="See with equality",
        lesson="Spiritual vision sees dignity in all beings beyond labels and status.",
        practice="Treat everyone you meet today with equal courtesy and attention.",
    ),
    Learning(
        chapter_verse="6.5",
        theme="Lift yourself by yourself",
        lesson="Your mind can be your ally when trained with discipline and kindness.",
        practice="Replace one self-critical thought with a constructive statement.",
    ),
    Learning(
        chapter_verse="6.26",
        theme="Bring the mind back gently",
        lesson="Meditation is repeated returning, not perfect stillness.",
        practice="For 5 minutes, whenever distracted, softly return to your breath.",
    ),
    Learning(
        chapter_verse="6.35",
        theme="Practice and detachment",
        lesson="A restless mind is managed through repetition and non-attachment.",
        practice="Set a tiny daily habit and keep it for just today.",
    ),
    Learning(
        chapter_verse="7.14",
        theme="Move beyond illusion",
        lesson="Clarity grows when you turn toward the divine instead of impulse.",
        practice="Before a major choice, ask: 'Is this aligned with my deeper values?'",
    ),
    Learning(
        chapter_verse="8.7",
        theme="Remember and act",
        lesson="Spiritual remembrance should accompany worldly responsibility.",
        practice="Take three short pauses today to remember your highest intention.",
    ),
    Learning(
        chapter_verse="9.22",
        theme="Trust and devotion",
        lesson="When your heart is steady in devotion, support appears in unexpected ways.",
        practice="Begin your day with a short prayer or gratitude reflection.",
    ),
    Learning(
        chapter_verse="9.27",
        theme="Make life an offering",
        lesson="Even ordinary actions become sacred when offered consciously.",
        practice="Offer one routine task (cooking, coding, cleaning) with full awareness.",
    ),
    Learning(
        chapter_verse="10.20",
        theme="Divine presence within",
        lesson="The source of life lives in every heart; act with reverence.",
        practice="In conversation, listen as if the divine is speaking through the other person.",
    ),
    Learning(
        chapter_verse="10.41",
        theme="Recognize excellence as divine spark",
        lesson="Beauty, brilliance, and strength can remind us of higher reality.",
        practice="Notice one inspiring quality in someone today and appreciate it.",
    ),
    Learning(
        chapter_verse="11.33",
        theme="Be an instrument",
        lesson="Act courageously; you need not carry the universe alone.",
        practice="Take one postponed courageous step today.",
    ),
    Learning(
        chapter_verse="12.13-14",
        theme="Cultivate devotional character",
        lesson="Compassion, humility, patience, and forgiveness are signs of spiritual maturity.",
        practice="Choose one difficult person and respond with patience today.",
    ),
    Learning(
        chapter_verse="12.15",
        theme="Be a source of peace",
        lesson="Live so others are not disturbed by you, and you remain undisturbed by them.",
        practice="Speak slower and softer in one tense interaction.",
    ),
    Learning(
        chapter_verse="13.8-12",
        theme="True knowledge is inner refinement",
        lesson="Humility, non-violence, and self-control are practical wisdom.",
        practice="Practice one act of restraint today (speech, anger, or impulse).",
    ),
    Learning(
        chapter_verse="14.26",
        theme="Rise beyond the gunas",
        lesson="Steady devotion helps transcend habitual emotional patterns.",
        practice="When mood shifts, observe it without becoming it.",
    ),
    Learning(
        chapter_verse="15.7",
        theme="You are an eternal soul",
        lesson="Your deepest identity is spiritual, not merely social or professional.",
        practice="Write one sentence completing: 'At my core, I am...'.",
    ),
    Learning(
        chapter_verse="16.21",
        theme="Guard against three gates to suffering",
        lesson="Unchecked desire, anger, and greed weaken judgment and peace.",
        practice="Notice which of the three appears today and interrupt it early.",
    ),
    Learning(
        chapter_verse="17.15",
        theme="Discipline your speech",
        lesson="Speak words that are truthful, kind, and beneficial.",
        practice="Before speaking, apply the filter: true, necessary, and kind.",
    ),
    Learning(
        chapter_verse="18.46",
        theme="Serve through your work",
        lesson="Excellence in your natural duty can itself be worship.",
        practice="Do your core responsibility today with extra care and sincerity.",
    ),
    Learning(
        chapter_verse="18.58",
        theme="Take refuge in wisdom",
        lesson="Anchoring your mind in higher guidance helps cross difficulties.",
        practice="When stuck, pause and ask what your wisest self would do.",
    ),
    Learning(
        chapter_verse="18.66",
        theme="Surrender fear",
        lesson="Let go of mental burden and trust divine support with wholeheartedness.",
        practice="Release one recurring worry by writing it down and consciously letting go.",
    ),
)


def learning_for_day(day: date) -> Learning:
    """Return a deterministic learning for the given day."""
    idx = day.toordinal() % len(LEARNINGS)
    return LEARNINGS[idx]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Show one Bhagavad Gita learning for a given day (default: today)."
    )
    parser.add_argument(
        "--date",
        help="Date in ISO format (YYYY-MM-DD). Defaults to today.",
    )
    return parser.parse_args()


def resolve_target_day(raw_date: str | None) -> date:
    if raw_date is None:
        return date.today()
    return datetime.strptime(raw_date, "%Y-%m-%d").date()


def format_learning(day: date, learning: Learning) -> str:
    return (
        f"Bhagavad Gita Learning for {day.isoformat()}\n"
        f"Verse: {learning.chapter_verse}\n"
        f"Theme: {learning.theme}\n"
        f"Lesson: {learning.lesson}\n"
        f"Practice: {learning.practice}\n"
    )


def main() -> None:
    args = parse_args()
    target_day = resolve_target_day(args.date)
    learning = learning_for_day(target_day)
    print(format_learning(target_day, learning))


if __name__ == "__main__":
    main()
