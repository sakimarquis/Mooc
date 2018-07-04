import string

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



class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        raise NotImplementedError

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

class PhraseTrigger(Trigger):
    def __init__(self,Phrase):
        self.Phrase = Phrase

    def evaluate(self,story):
        if self.Phrase in story.getSubject() \
                or self.Phrase in story.getTitle() \
                or self.Phrase in story.getSummary():
            return True
        return False

pt = PhraseTrigger("New York City")
a = NewsStory('', "asfdNew York Cityasfdasdfasdf", '', '', '')
b = NewsStory('', '', "asdfasfdNew York Cityasfdasdfasdf", '', '')
c = NewsStory('', '', '', "asdfasfdNew York Cityasfdasdfasdf", '')
noa = NewsStory('', "something something new york city", '', '', '')
nob = NewsStory('', '', "something something new york city", '', '')
noc = NewsStory('', '', '', "something something new york city", '')

triggers = [pt]
stories = [a, b, c, noa, nob, noc]



for story in stories:
    print story