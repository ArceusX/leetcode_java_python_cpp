class Solution:
    def reformatDate(self, date: str) -> str:
           return datetime.datetime.strptime(re.sub('rd|nd|th|st|','',date),'%d %b %Y').strftime('%Y-%m-%d')
        