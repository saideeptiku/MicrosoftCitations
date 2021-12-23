"""
Describe a source as a datacleass
"""

from dataclass import dataclass, asdict

@dataclass(frozen=True)
class SourceType:
    Journal: string = "JournalArticle"
    Conference: string = "ConferenceProceedings"
    Webpage: string = "InternetArticle"

@dataclass
class Author:
    first_name: string
    last_name: string


@dataclass
class Source:
    """
    A source in an MS XML file as a dataclass
    """

    source_type: SourceType
    tag: string
    title: string
    year: string
    authors: string,
    publisher_name: string
    volume: int = None
    issue: int = None
    pages: tuple: None
    url: string = None


