from dataclasses import dataclass


@dataclass
class Course:
    name: str
    desc: str
    course_no: int
    subject: str
    restrict: list
    pre_req: list
    credit_hrs: int
    cross_list: list
    recently_offered: list
    pertains_to: list


@dataclass
class Program:
    name: str
    desc: str
    total_credits: int
    admis_req: list


@dataclass
class Option:
    name: str
    desc: str
    courses: list
    no_of_choices: int
    min_credit: int
    max_credit: int
    options: list


@dataclass
class Requirement:
    name: str
    desc: str
    min_credit: int
    max_credit: int
    options: list


name = '//*[@id="acalog-page-title"]'
desc = '//*[@id="gateway-page"]/body/table/tbody/tr[3]/td[2]/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr[1]/td/p'
admis_req = '//*[@id="gateway-page"]/body/table/tbody/tr[3]/td[2]/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr[2]/td/div/div[1]'
deg_req = '//*[@id="gateway-page"]/body/table/tbody/tr[3]/td[2]/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr[2]/td/div/div[2]'
