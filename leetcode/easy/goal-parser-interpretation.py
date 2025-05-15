# https://leetcode.com/problems/goal-parser-interpretation/

class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        goal=''
        commmandList=list(command)
        previouchar = ''
        for singleChar in commmandList:
            if singleChar=='(' or singleChar==')':
                if previouchar=="(" and singleChar==")":
                    goal+="o"
            else:
                goal+=singleChar
            previouchar=singleChar
        return goal
