from dataclasses import dataclass


@dataclass
class Course:
    name: str = None
    desc: str = None
    course_no: int = None
    subject: str = None
    restrict: list = None
    pre_req: list = None
    credit_hrs: int = None
    cross_list: list = None
    recently_offered: list = None
    pertains_to: list = None


@dataclass
class Program:
    name: str = None
    desc: str = None
    total_credits: int = None
    admis_req: list = None
    deg_req: list = None
    requirements: list = None
    data: list = None


@dataclass
class Option:
    name: str = None
    desc: str = None
    courses: list = None
    no_of_choices: int = None
    min_credit: int = None
    max_credit: int = None
    options: list = None


@dataclass
class Requirement:
    name: str = None
    desc: str = None
    min_credit: int = None
    max_credit: int = None
    options: list = None


name = '//*[@id="acalog-page-title"]'
desc = '//*[@id="gateway-page"]/body/table/tbody/tr[3]/td[2]/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr[1]/td/p'
admis_req = '//*[@id="gateway-page"]/body/table/tbody/tr[3]/td[2]/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr[2]/td/div/div[1]'
deg_req = '//*[@id="gateway-page"]/body/table/tbody/tr[3]/td[2]/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr[2]/td/div/div[2]'


def next_big_thing(current):
    if isinstance(current, Requirement):
        return Option()
    if isinstance(current, Option):
        return Option()
    if isinstance(current, Program):
        return Requirement()
