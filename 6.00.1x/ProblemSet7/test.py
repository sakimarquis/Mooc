# 6.00.1x Problem Set 7
# RSS Feed Filter

import feedparser
import string
import time
from project_util import translate_html
from Tkinter import *


#-----------------------------------------------------------------------
#
# Problem Set 7

#======================
# Code for retrieving and parsing RSS feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        summary = translate_html(entry.summary)
        try:
            subject = translate_html(entry.tags[0]['term'])
        except AttributeError:
            subject = ""
        newsStory = NewsStory(guid, title, subject, summary, link)
        ret.append(newsStory)
    return ret
#======================

#======================
# Part 1
# Data structure design
#======================

# Problem 1

class NewsStory(object):
    def __init__(self,guid, title, subject, summary, link):
        self.guid = guid
        self.title = title
        self.subject = subject
        self.summary = summary
        self.link = link

    def getGuid(self):
        return self.guid

    def getTitle(self):
        return self.title

    def getSubject(self):
        return self.subject

    def getSummary(self):
        return self.summary

    def getLink(self):
        return self.link

#======================
# Part 2
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        raise NotImplementedError


# Whole Word Triggers
# Problems 2-5

class WordTrigger(Trigger):
    def __init__(self,word):
        self.word = word

    def isWordIn(self,text):
        for i in string.punctuation:
            text = text.replace(str(i), ' ')
        for i in text.split(' '):
            if self.word.lower() == i.lower():
                return True
        else:
            return False


class TitleTrigger(WordTrigger):
    def evaluate(self,story):
        return self.isWordIn(story.getTitle())


class SubjectTrigger(WordTrigger):
    def evaluate(self,story):
        return self.isWordIn(story.getSubject())


class SummaryTrigger(WordTrigger):
    def evaluate(self,story):
        return self.isWordIn(story.getSummary())


# Composite Triggers
# Problems 6-8
class NotTrigger(Trigger):
    def __init__(self,Trigger):
        self.Trigger = Trigger

    def evaluate(self,story):
        return not self.Trigger.evaluate(story)


class AndTrigger(Trigger):
    def __init__(self,Trigger1,Trigger2):
        self.Trigger1 = Trigger1
        self.Trigger2 = Trigger2

    def evaluate(self,story):
        return self.Trigger1.evaluate(story) and self.Trigger2.evaluate(story)


class OrTrigger(Trigger):
    def __init__(self,Trigger1,Trigger2):
        self.Trigger1 = Trigger1
        self.Trigger2 = Trigger2

    def evaluate(self,story):
        return self.Trigger1.evaluate(story) or self.Trigger2.evaluate(story)


# Phrase Trigger
# Question 9

class PhraseTrigger(Trigger):
    def __init__(self,Phrase):
        self.Phrase = Phrase

    def evaluate(self,story):
        if self.Phrase in story.getSubject() \
                or self.Phrase in story.getTitle() \
                or self.Phrase in story.getSummary():
            return True
        return False

#======================
# Part 3
# Filtering
#======================

def filterStories(stories,triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    filteredStories = []
    for story in stories:
        flag = 0
        for trigger in triggerlist:
            if trigger.evaluate(story):
                flag = 1
        if flag == 1:
            filteredStories.append(story)
    return filteredStories

#======================
# Part 4
# User-Specified Triggers
#======================

def makeTrigger(triggerMap, triggerType, params, name):
    """
    Takes in a map of names to trigger instance, the type of trigger to make,
    and the list of parameters to the constructor, and adds a new trigger
    to the trigger map dictionary.

    triggerMap: dictionary with names as keys (strings) and triggers as values
    triggerType: string indicating the type of trigger to make (ex: "TITLE")
    params: list of strings with the inputs to the trigger constructor (ex: ["world"])
    name: a string representing the name of the new trigger (ex: "t1")

    Modifies triggerMap, adding a new key-value pair for this trigger.

    Returns a new instance of a trigger (ex: TitleTrigger, AndTrigger).
    """
    #trigger = Trigger()
    if triggerType == "TITLE":
        trigger = TitleTrigger(params[0])
    elif triggerType == "SUBJECT":
        trigger = SubjectTrigger(params[0])
    elif triggerType == "SUMMARY":
        trigger = SummaryTrigger(params[0])
    elif triggerType == "PHRASE":
        trigger = PhraseTrigger(" ".join(params))
    elif triggerType == "NOT":
        trigger = NotTrigger(triggerMap[params[0]])
    elif triggerType == "AND":
        trigger = AndTrigger(triggerMap[params[0]],triggerMap[params[1]])
    elif triggerType == "OR":
        trigger = OrTrigger(triggerMap[params[0]],triggerMap[params[1]])
    triggerMap[name] = trigger
    return trigger

def readTriggerConfig(filename):
    """
    Returns a list of trigger objects
    that correspond to the rules set
    in the file filename
    """

    # Here's some code that we give you
    # to read in the file and eliminate
    # blank lines and comments
    triggerfile = open(filename, "r")
    all = [ line.rstrip() for line in triggerfile.readlines() ]
    lines = []
    for line in all:
        if len(line) == 0 or line[0] == '#':
            continue
        lines.append(line)

    triggers = []
    triggerMap = {}

    # Be sure you understand this code - we've written it for you,
    # but it's code you should be able to write yourself
    for line in lines:

        linesplit = line.split(" ")

        # Making a new trigger
        if linesplit[0] != "ADD":
            trigger = makeTrigger(triggerMap, linesplit[1],
                                  linesplit[2:], linesplit[0])

        # Add the triggers to the list
        else:
            for name in linesplit[1:]:
                triggers.append(triggerMap[name])

    return triggers

print readTriggerConfig("triggers.txt")