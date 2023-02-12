"""
문제 설명
고객의 약관 동의를 얻어서 수집된 1~n번으로 분류되는 개인정보 n개가 있습니다. 약관 종류는 여러 가지 있으며 각 약관마다 개인정보 보관 유효기간이 정해져 있습니다. 
당신은 각 개인정보가 어떤 약관으로 수집됐는지 알고 있습니다. 수집된 개인정보는 유효기간 전까지만 보관 가능하며, 유효기간이 지났다면 반드시 파기해야 합니다.

예를 들어, A라는 약관의 유효기간이 12 달이고, 2021년 1월 5일에 수집된 개인정보가 A약관으로 수집되었다면 
해당 개인정보는 2022년 1월 4일까지 보관 가능하며 2022년 1월 5일부터 파기해야 할 개인정보입니다.
당신은 오늘 날짜로 파기해야 할 개인정보 번호들을 구하려 합니다.

모든 달은 28일까지 있다고 가정합니다.

다음은 오늘 날짜가 2022.05.19일 때의 예시입니다.

약관 종류	유효기간
A	6 달
B	12 달
C	3 달
번호	개인정보 수집 일자	약관 종류
1	2021.05.02	A
2	2021.07.01	B
3	2022.02.19	C
4	2022.02.20	C
입출력 예         
today	                 terms	                                      privacies	                                                 result
"2022.05.19"	["A 6", "B 12", "C 3"]	["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]	                     [1, 3]
"2020.01.01"	["Z 3", "D 5"]	        ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]        [1, 4, 5]
"""

today = "2022.05.19"
terms = ["A 6", "B 12", "C 3"]
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]

def solution(today, terms, privacies):
    answer = []
    time_dict = dict()
    year, month, day = int(today[0:4]), int(today[5:7]), int(today[8:])
    
    for term in terms : 
        case = term[0]
        time_dict[case] = int(term[2:])
        # 딕셔너리로 약관 종류에 따른 기간 구분합니다
    
    for i in range(len(privacies)):
        date, case = privacies[i].split()
        p_year, p_month, p_day = int(privacies[i][0:4]), int(privacies[i][5:7]), int(privacies[i][8:10])
        
        p_month += time_dict[case]
        
        # if p_month > 12 : print(p_year,p_month, p_day, case)
        while p_month > 12 : 
            p_month -= 12
            p_year +=1
            
            
        if p_year > year :
            continue
            
        elif p_year == year :
            if p_month > month :
                continue
                
            elif p_month == month :
                if p_day > day :
                    continue
                    
        answer.append(i+1)
        # 배열사용을 위해 i는 0부터 시작하므로 정답에 +1 하여 추가합니다
        # print(p_year,p_month,p_day,case)
    
    return answer

print(solution(today, terms, privacies))