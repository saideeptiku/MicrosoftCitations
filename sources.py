"""
Describe a source as a datacleass
"""

from dataclasses import dataclass, asdict
from typing import String, List


@dataclass(frozen=True)
class SourceType:
    Journal: String = "JournalArticle"
    Conference: String = "ConferenceProceedings"
    Webpage: String = "InternetArticle"


@dataclass
class Author:
    """
    Class to identify 
    """
    first_name: String
    last_name: String


@dataclass
class Source:
    """
    A source in an MS XML file as a dataclass
    """

    source_type: SourceType
    tag: String
    title: String
    year: String
    authors: List[Author]
    publisher_name: String
    volume: int = None
    issue: int = None
    pages: tuple = None
    url: String = None


    @classmethod
    def from_ieee_txt(cls, txt):
        """Expects a string reference-
        Does not expect to see et al.

        Parameters
        ----------
        txt : str
            Expects a string like following
            Saideep Tiku, Prathmesh Kale, and Sudeep Pasricha, 
            "QuickLoc: Adaptive Deep-Learning for Fast Indoor Localization with Mobile Devices", 
            ACM Trans. Cyber-Phys. Syst. vol. 5, no. 4, pp. 44, 2021
        """
        pass


    def as_xml_element(self):
        raise NotImplementedError