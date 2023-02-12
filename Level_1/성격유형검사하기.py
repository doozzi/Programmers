"""
나만의 카카오 성격 유형 검사지를 만들려고 합니다.
성격 유형 검사는 다음과 같은 4개 지표로 성격 유형을 구분합니다. 성격은 각 지표에서 두 유형 중 하나로 결정됩니다.

지표 번호	성격 유형
1번 지표	라이언형(R), 튜브형(T)
2번 지표	콘형(C), 프로도형(F)
3번 지표	제이지형(J), 무지형(M)
4번 지표	어피치형(A), 네오형(N)

각 질문은 1가지 지표로 성격 유형 점수를 판단합니다.

예를 들어, 어떤 한 질문에서 4번 지표로 아래 표처럼 점수를 매길 수 있습니다.

선택지	     성격 유형 점수
매우 비동의	   네오형 3점
비동의	       네오형 2점
약간 비동의	   네오형 1점
모르겠음	어떤 성격 유형도 점수를 얻지 않습니다
약간 동의	  어피치형 1점
동의	      어피치형 2점
매우 동의	  어피치형 3점
이때 검사자가 질문에서 약간 동의 선택지를 선택할 경우 어피치형(A) 성격 유형 1점을 받게 됩니다. 만약 검사자가 매우 비동의 선택지를 선택할 경우 네오형(N) 성격 유형 3점을 받게 됩니다.
  
survey	                                 choices	      result
["AN", "CF", "MJ", "RT", "NA"]	     [5, 3, 2, 7, 5]	  "TCMA"
["TR", "RT", "TR"]	                    [7, 1, 3]	      "RCJA"
"""

survey = ["AN", "CF", "MJ", "RT", "NA"]
choices = [5, 3, 2, 7, 5]

def solution(survey, choices):
    answer = ''
    dic= {"R" : 0,"T" : 0,"C" : 0,"F" : 0,"J" : 0,"M" : 0,"A" : 0,"N" : 0 }
    
    for s,c in zip(survey,choices):
        if int(c)>4:     dic[s[1]] += c-4
        elif int(c)<4:   dic[s[0]] += 4-c
    
    li = list(dic.items())
    
    for i in range(0,8,2):
        if li[i][1] < li[i+1][1]: answer += li[i+1][0]
        else:   answer += li[i][0]
        
    return answer

print(solution(survey, choices))