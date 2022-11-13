def solution(mid_scores, final_scores):
    answer = []
    answer.append(max(final-mid for mid,final in list(zip(mid_scores,final_scores))))
    
    answer.append(min(final-mid for mid,final in list(zip(mid_scores,final_scores))))    
    return answer